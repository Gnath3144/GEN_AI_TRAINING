# Day 05 Exercises: Quantitative RAG Evaluation

## Exercise 1: Reciprocal Rank Fusion (Warm-up)
1. Write a function `compute_rrf(list1, list2, k=60)` that takes two ranked lists of document identifiers and produces a unified score.
2. Verify with test assertions that an item appearing near the top of both lists receives higher priority than an item appearing at rank 1 in only one list.

---

## Exercise 2: Automated RAG Evaluation Benchmark (Core Project)
### User Story
As an AI QA Engineer, I need an automated test suite that evaluates our insurance RAG pipeline against a ground-truth benchmark dataset to quantitatively score:
1. **Hit Rate @ K**: Was the ground-truth document retrieved in top-$K$?
2. **Context Precision**: Ratio of relevant retrieved documents over total retrieved.
3. **Groundedness Score**: Did the answer contain hallucinated claims?

### Acceptance Criteria
1. Define a benchmark test set with questions and expected ground-truth document IDs.
2. Execute the RAG pipeline over the test set.
3. Automatically evaluate each query and log pass/fail status.
4. Output a final evaluation scorecard displaying overall Hit Rate @ 2 and Mean Reciprocal Rank (MRR).

### Reference Solution
See `solutions/rag_evaluation.py`.
