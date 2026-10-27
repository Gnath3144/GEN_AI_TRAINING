"""Day 04 Reference Solution: Enterprise Insurance Knowledge Base RAG Pipeline."""

import sys
import os
import json
import logging
import math
import re
from typing import List, Dict, Any, Optional

# Link to shared libraries
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from shared.utils import UnifiedLLMClient, count_tokens, estimate_cost
from shared.common_prompts.system_prompts import RAG_GROUNDING_PROMPT

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


class LightweightVectorStore:
    """Zero-dependency fallback vector store using TF-IDF and Cosine Similarity."""
    def __init__(self):
        self.documents = []
        self.doc_ids = []
        self.vocab = {}
        self.tfidf_matrix = []

    def add(self, documents: List[str], ids: List[str]):
        self.documents.extend(documents)
        self.doc_ids.extend(ids)
        self._build_index()

    def _tokenize(self, text: str) -> List[str]:
        return re.findall(r"\b[a-zA-Z0-9_]{2,}\b", text.lower())

    def _build_index(self):
        # Build vocabulary
        df = {}
        tokenized_docs = [self._tokenize(d) for d in self.documents]
        for tokens in tokenized_docs:
            for t in set(tokens):
                df[t] = df.get(t, 0) + 1

        self.vocab = {term: idx for idx, term in enumerate(df.keys())}
        num_docs = max(1, len(self.documents))
        self.idf = {term: math.log((num_docs + 1) / (count + 1)) + 1.0 for term, count in df.items()}

        # Compute TF-IDF vectors
        self.tfidf_matrix = []
        for tokens in tokenized_docs:
            vec = [0.0] * len(self.vocab)
            tf = {}
            for t in tokens:
                tf[t] = tf.get(t, 0) + 1
            for t, count in tf.items():
                if t in self.vocab:
                    vec[self.vocab[t]] = count * self.idf[t]
            norm = math.sqrt(sum(x * x for x in vec)) or 1.0
            self.tfidf_matrix.append([x / norm for x in vec])

    def query(self, query_text: str, top_k: int = 2) -> List[Dict[str, Any]]:
        tokens = self._tokenize(query_text)
        query_vec = [0.0] * len(self.vocab)
        tf = {}
        for t in tokens:
            tf[t] = tf.get(t, 0) + 1
        for t, count in tf.items():
            if t in self.vocab:
                query_vec[self.vocab[t]] = count * self.idf[t]
        norm = math.sqrt(sum(x * x for x in query_vec)) or 1.0
        query_vec = [x / norm for x in query_vec]

        # Calculate cosine similarity with all documents
        scores = []
        for i, doc_vec in enumerate(self.tfidf_matrix):
            sim = sum(q * d for q, d in zip(query_vec, doc_vec))
            scores.append((sim, i))

        scores.sort(key=lambda x: x[0], reverse=True)
        results = []
        for score, idx in scores[:top_k]:
            results.append({
                "id": self.doc_ids[idx],
                "content": self.documents[idx],
                "score": round(score, 4)
            })
        return results


class InsuranceRAGPipeline:
    def __init__(self, data_file: Optional[str] = None):
        if not data_file:
            data_file = os.path.join(os.path.dirname(__file__), "..", "..", "shared", "sample_data", "knowledge_base.json")
        with open(data_file, "r", encoding="utf-8") as f:
            self.raw_docs = json.load(f)

        self.client = UnifiedLLMClient()
        self.use_chroma = False

        # Try initializing ChromaDB if installed, otherwise use lightweight vector store
        try:
            import chromadb
            self.chroma = chromadb.Client()
            self.collection = self.chroma.get_or_create_collection("insurellm_kb")
            self.use_chroma = True
            logger.info("Using ChromaDB vector store.")
        except ImportError:
            logger.info("ChromaDB not installed in current environment. Using LightweightVectorStore fallback.")
            self.store = LightweightVectorStore()

        self._index_documents()

    def _index_documents(self):
        """Indexes knowledge base items into the active vector store."""
        docs = []
        ids = []
        for item in self.raw_docs:
            full_text = f"Title: {item['title']}\nCategory: {item['category']}\nContent: {item['content']}"
            docs.append(full_text)
            ids.append(item["id"])

        if self.use_chroma:
            if self.collection.count() == 0:
                self.collection.add(documents=docs, ids=ids)
        else:
            self.store.add(documents=docs, ids=ids)

        logger.info(f"Successfully indexed {len(docs)} documents.")

    def retrieve(self, query: str, top_k: int = 2) -> List[Dict[str, Any]]:
        """Performs vector similarity search against the active vector store."""
        if self.use_chroma:
            results = self.collection.query(query_texts=[query], n_results=top_k)
            retrieved = []
            if results and "documents" in results and results["documents"]:
                for i in range(len(results["documents"][0])):
                    retrieved.append({
                        "id": results["ids"][0][i],
                        "content": results["documents"][0][i]
                    })
            return retrieved
        else:
            return self.store.query(query, top_k=top_k)

    def answer_question(self, user_question: str) -> str:
        """Retrieves context and synthesizes grounded answer."""
        retrieved_docs = self.retrieve(user_question, top_k=2)

        # Assemble context block
        context_blocks = []
        for doc in retrieved_docs:
            context_blocks.append(f"Source ID: [{doc['id']}]\n{doc['content']}")
        formatted_context = "\n\n---\n\n".join(context_blocks)

        prompt = (
            f"RELEVANT VERIFIED POLICY DOCUMENTS:\n\n{formatted_context}\n\n"
            f"CUSTOMER QUESTION:\n{user_question}\n\n"
            "DETAILED GROUNDED ANSWER:"
        )

        response = self.client.complete(
            prompt=prompt,
            system_prompt=RAG_GROUNDING_PROMPT,
            temperature=0.1
        )
        return response


def main():
    rag = InsuranceRAGPipeline()

    test_questions = [
        "What is the deductible for collision claims, and how does the vanishing deductible program work?",
        "Does standard homeowners insurance cover water damage if a pipe leaks continuously for 3 weeks?",
        "What is the reimbursement policy if my spacecraft is captured by alien extraterrestrials?"
    ]

    print("\n" + "=" * 75)
    print("INSURELLM ENTERPRISE RAG KNOWLEDGE BASE")
    print("=" * 75)

    for q in test_questions:
        print(f"\n>> QUESTION: {q}")
        docs = rag.retrieve(q, top_k=2)
        print(f"   [Retrieved Sources: {', '.join([d['id'] for d in docs])}]")
        answer = rag.answer_question(q)
        print(f">> ANSWER:\n{answer}\n" + "-" * 75)


if __name__ == "__main__":
    main()
