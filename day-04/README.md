# Day 04 — Embeddings, Semantic Search & Foundational RAG

**Delivery Status**: `PLANNED`  
**Supporting Reference**: Derived from `ed-donner/llm_engineering` Week 5 (`day1.ipynb`, `day2.ipynb`, `day3.ipynb`).

---

## 1. Session Overview
Retrieval-Augmented Generation (RAG) is the foundational architecture of enterprise AI. It solves the three biggest shortcomings of Large Language Models: knowledge cutoff, hallucinations, and inability to access private internal company data.

Day 04 teaches the core RAG lifecycle: converting unstructured text into dense mathematical embeddings, storing them in ChromaDB, retrieving relevant context via cosine similarity, and injecting grounded context into the LLM prompt.

---

## 2. Learning Objectives
- Understand mathematical vector embeddings (semantic geometry, dot product, cosine distance).
- Implement document chunking strategies (chunk size, overlap, semantic boundary).
- Ingest documents and manage collections in **ChromaDB**.
- Build an end-to-end question-answering pipeline with strict source citation grounding.
- Query an enterprise insurance knowledge base and verify source attribution.

---

## 3. Directory Contents
- **[`concepts.md`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-04/concepts.md)**: Vector mathematics, chunking tradeoffs, and the RAG architecture.
- **[`demo.ipynb`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-04/demo.ipynb)**: Step-by-step notebook ingesting documents into ChromaDB and running semantic queries.
- **[`exercises.md`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-04/exercises.md)**: Lab assignments building a document QA system.
- **[`solutions/rag_pipeline.py`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-04/solutions/rag_pipeline.py)**: Production-ready reference RAG pipeline.

---

## 4. How to Run Day 04 Materials
```bash
python day-04/solutions/rag_pipeline.py
```
