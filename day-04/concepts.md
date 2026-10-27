# Day 04 Concepts: Embeddings & RAG Architecture

## 1. What is an Embedding?
An embedding model maps textual strings of arbitrary length to dense vectors in $\mathbb{R}^D$ (e.g., $D=384$ for `all-MiniLM-L6-v2` or $D=1536$ for `text-embedding-3-small`).

Semantically related concepts are situated near each other in this high-dimensional vector space:
$$\text{Cosine Similarity}(A, B) = \frac{A \cdot B}{\|A\| \|B\|}$$

Unlike keyword matching (which fails when synonyms are used, e.g., "doctor" vs. "physician"), vector search matches conceptual intent.

---

## 2. The Chunking Dilemma
Raw documents are too long to fit or perform well inside embedding representations. We must divide them into smaller chunks:
- **Chunk Size Too Large (e.g. 2,000 words)**: The vector embedding becomes diluted and generalized; specific factual sentences are lost.
- **Chunk Size Too Small (e.g. 20 words)**: The chunk lacks context (e.g., "It costs $50" — what is "It"?).
- **Chunk Overlap (e.g., 10-20%)**: Ensures facts spanning across the split point are preserved in both adjacent chunks.

---

## 3. The RAG Prompt Pattern
```python
RAG_TEMPLATE = """You are an AI research assistant.
Answer the user's question using ONLY the retrieved facts below.
If the answer is not contained in the context, say "I don't know based on provided docs".

CONTEXT:
{retrieved_chunks}

QUESTION:
{user_question}

ANSWER (with source citations):"""
```
This forces the model to base its reasoning on the injected context, preventing hallucinated knowledge cutoff dates or fabricated policies.
