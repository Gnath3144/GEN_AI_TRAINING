# Day 05 Concepts: Advanced RAG & Quantitative Evaluation

## 1. Why Naive Vector Search Fails in Production
1. **The Exact-Match Blindspot**: Vector embeddings often struggle with exact alphanumeric part numbers, error codes, and legal clause numbers (e.g., searching for `KB-102` or `RFC 7540`).
2. **The "Lost-in-the-Middle" Phenomenon**: LLM attention heads favor tokens at the extreme beginning and end of long prompts. Crucial facts buried in middle chunks are frequently ignored.
3. **Out-of-Domain Retrieval**: The retriever returns the "closest" document in embedding space even when no relevant document exists, leading to context contamination.

---

## 2. Hybrid Search & Reciprocal Rank Fusion (RRF)
Hybrid search executes two parallel retrieval passes:
1. **Lexical Pass**: BM25 keyword matching (high precision for specific terminology, codes, names).
2. **Dense Semantic Pass**: Vector cosine distance (high recall for synonyms and conceptual intent).

We merge both ranked lists using **Reciprocal Rank Fusion (RRF)**:
$$RRF(d) = \sum_{m \in M} \frac{1}{k + r_m(d)}$$
Where $r_m(d)$ is the rank position of document $d$ in method $m$, and $k$ is a smoothing constant (typically $k=60$).

---

## 3. The Triad of RAG Evaluation Metrics

```
      [ User Question ]
       /             \
      /               \
Context Relevance   Answer Relevance
    /                   \
   v                     v
[ Retrieved Context ] ───> [ Generated Answer ]
        ^                      |
        └──── Groundedness ────┘
              (Faithfulness)
```

1. **Context Relevance**: What fraction of retrieved text was actually necessary to answer the question?
2. **Groundedness (Faithfulness)**: What percentage of claims in the generated answer can be mathematically traced back to the retrieved context? (Target: 100%).
3. **Answer Relevance**: Did the model answer the question directly without digression?
