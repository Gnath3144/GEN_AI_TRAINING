# Day 05 — Advanced RAG, Grounding & Retrieval Evaluation

**Delivery Status**: `PLANNED`  
**Supporting Reference**: Derived from `ed-donner/llm_engineering` Week 5 (`day4.ipynb`, `day5.ipynb`, `evaluator.py`).

---

## 1. Session Overview
Building a prototype RAG system is easy; making it accurate and reliable in enterprise production is hard. Naive vector search frequently retrieves irrelevant noise, suffers from the "lost-in-the-middle" effect, and yields confident hallucinations.

Day 05 covers **Advanced RAG** techniques: hybrid search (BM25 lexical + dense vector), reciprocal rank fusion (RRF), cross-encoder re-ranking, and automated evaluation metrics (Context Precision, Faithfulness/Groundedness, Answer Relevance).

---

## 2. Learning Objectives
- Identify the 4 major failure modes of naive RAG.
- Implement Hybrid Retrieval combining lexical keyword search (BM25) with vector similarity.
- Implement Reciprocal Rank Fusion (RRF) to merge multiple ranked retrieval lists.
- Build an automated RAG evaluation harness measuring:
  - **Context Relevance**: Did the retriever fetch the right document?
  - **Groundedness (Faithfulness)**: Is every claim in the answer backed by the context?
  - **Answer Completeness**: Did the model answer the user's question directly?
- Benchmark a baseline retriever against an improved hybrid retriever.

---

## 3. Directory Contents
- **[`concepts.md`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-05/concepts.md)**: Deep dive into Hybrid RAG, re-ranking algorithms, and automated LLM evaluation.
- **[`demo.ipynb`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-05/demo.ipynb)**: Interactive notebook implementing hybrid retrieval and evaluation scoring.
- **[`exercises.md`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-05/exercises.md)**: Lab specifications for building an evaluation harness.
- **[`solutions/rag_evaluation.py`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-05/solutions/rag_evaluation.py)**: Reference solution implementing automated RAG evaluation.

---

## 4. How to Run Day 05 Materials
```bash
python day-05/solutions/rag_evaluation.py
```
