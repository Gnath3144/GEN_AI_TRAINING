# Day 03 — Resilient LLM Application Architecture & Tool Calling

**Delivery Status**: `PLANNED`  
**Supporting Reference**: Derived from `ed-donner/llm_engineering` Week 2 (`day4.ipynb`, `week1/solution.py`).

---

## 1. Session Overview
Language models cannot natively query databases, check live flight departures, or calculate complex dynamic mathematical formulas. Tool Calling (Function Calling) bridges this divide by turning the LLM into a reasoning engine that chooses *which* function to call, *what arguments* to pass, and *how to interpret* the returned result.

In Day 03, we build resilient application architectures that declare tool schemas, dispatch functions, handle rate limits with exponential backoff (`tenacity`), and synthesize user-facing responses.

---

## 2. Learning Objectives
- Design resilient LLM service wrappers with timeout and retry policies.
- Understand the 2-turn Tool Calling cycle (`user prompt -> model tool_call -> client executes function -> client passes tool_result -> model synthesizes response`).
- Declare strict JSON Schemas for Python functions.
- Securely execute functions without exposing arbitrary code execution vulnerabilities.
- Build an AI Airline Customer Service Assistant that executes flight status checks and baggage fee calculations.

---

## 3. Directory Contents
- **[`concepts.md`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-03/concepts.md)**: Two-turn function calling protocols, schema declarations, and resilience patterns.
- **[`demo.ipynb`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-03/demo.ipynb)**: Walkthrough of tool schema declarations and execution loops.
- **[`exercises.md`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-03/exercises.md)**: Airline Assistant lab specifications and challenges.
- **[`solutions/tool_calling_assistant.py`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-03/solutions/tool_calling_assistant.py)**: Full reference solution for the tool-calling assistant.

---

## 4. How to Run Day 03 Materials
```bash
python day-03/solutions/tool_calling_assistant.py
```
