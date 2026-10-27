# Day 02 — Model APIs, Prompt Engineering & Structured Outputs

**Delivery Status**: `IN_PROGRESS`  
**Active Session Date**: Today (October 27, 2026)  
**Supporting Reference**: Derived from `ed-donner/llm_engineering` Week 1 (`day2.ipynb`, `day4.ipynb`, `day5.ipynb`).

---

## 1. Session Overview
Today's session focuses on turning natural language into structured, predictable data models. While natural language text is great for humans, enterprise software systems require schema-validated JSON, typed data models, and deterministic contracts.

We cover frontier model APIs, the mechanics of system/user messages, prompt engineering principles (few-shot, delimiter isolation, chain-of-thought), and programmatic schema validation using **Pydantic**.

---

## 2. Learning Objectives
- Master the `system`, `user`, `assistant`, and `tool` message taxonomy.
- Understand generation hyperparameters: `temperature`, `top_p`, `max_tokens`, `presence_penalty`.
- Measure context token length and project financial costs using `tiktoken`.
- Enforce structured JSON schemas using Pydantic models and Native JSON mode.
- Build a resilient entity and sentiment extractor that parses unstructured reviews into type-safe objects.

---

## 3. Directory Contents
- **[`concepts.md`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-02/concepts.md)**: Deep dive into API architectures, prompt mechanics, and schema enforcement.
- **[`demo.ipynb`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-02/demo.ipynb)**: Interactive notebook exploring prompt templates, token counting, and Pydantic validation.
- **[`exercises.md`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-02/exercises.md)**: Lab assignments on prompt engineering and structured schema extraction.
- **[`solutions/structured_extractor.py`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-02/solutions/structured_extractor.py)**: Reference solution parsing customer feedback into validated Pydantic models.

---

## 4. How to Run Day 02 Materials
```bash
# Run the structured extractor over sample review data:
python day-02/solutions/structured_extractor.py
```
