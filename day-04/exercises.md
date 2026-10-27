# Day 04 Exercises: Enterprise Knowledge RAG Pipeline

## Exercise 1: Embedding Geometry & Similarity (Warm-up)
1. Write a script that encodes 3 sentences using `sentence-transformers` (`all-MiniLM-L6-v2`):
   - Sentence A: "The feline rested quietly on the wool rug."
   - Sentence B: "A small cat was sleeping on the carpet."
   - Sentence C: "Quarterly corporate revenue exceeded financial projections."
2. Compute cosine similarity between $(A, B)$ and $(A, C)$. Verify that $(A, B)$ has a significantly higher similarity score despite sharing almost zero identical words.

---

## Exercise 2: Insurance Policy Question-Answering RAG (Core Project)
### User Story
As an insurance underwriter, I need an AI knowledge worker that answers complex policy questions by retrieving exact matching clauses from our knowledge base and citing the clause ID in every response.

### Acceptance Criteria
1. Ingest `shared/sample_data/knowledge_base.json` into a ChromaDB collection (`insurellm_kb`).
2. Implement semantic search with top-$K$ retrieval ($K=2$).
3. Inject the retrieved documents into the `RAG_GROUNDING_PROMPT` system template.
4. If the question cannot be answered by the knowledge base (e.g. *"What is the policy for alien abductions?"*), the assistant must state that the information is unavailable rather than hallucinating an answer.
5. Every valid answer must cite the source ID (e.g. `[KB-101]`).

### Reference Solution
See `solutions/rag_pipeline.py`.
