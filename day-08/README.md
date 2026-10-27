# Day 08 — Autonomous Agents & Workflow Orchestration

**Delivery Status**: `PLANNED`  
**Supporting Reference**: Derived from `ed-donner/llm_engineering` Week 8 (`day1.ipynb` – `day4.ipynb`, `deal_agent_framework.py`).

---

## 1. Session Overview
What separates a standard LLM completion from an **Autonomous Agent**?
A standard completion runs a single fixed pass. A workflow (DAG) runs a predetermined deterministic sequence. An **Agent**, by contrast, dynamically determines its own trajectory: it reasons about a goal, selects an action/tool, observes the result, updates its internal state scratchpad, and iterates until the objective is accomplished or a stopping boundary is hit.

Day 08 demystifies agentic architectures. We implement the **ReAct (Reason + Act)** pattern and build a bounded autonomous research and price deal-finding agent with strict loop limits and error recovery.

---

## 2. Learning Objectives
- Distinguish between Single-turn LLM calls, Deterministic DAG Workflows, and Autonomous Agents.
- Implement the **ReAct Loop** (Thought -> Action -> Observation -> Reflection).
- Maintain an append-only agent scratchpad and manage state transitions.
- Enforce strict termination conditions (maximum iteration steps, token budget cap) to prevent infinite loops.
- Build a Multi-Tool Deal Hunting Agent that searches products, compares competitor prices, and summarizes discount opportunities.

---

## 3. Directory Contents
- **[`concepts.md`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-08/concepts.md)**: Agent taxonomies, ReAct state machines, and infinite loop prevention.
- **[`demo.ipynb`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-08/demo.ipynb)**: Walkthrough of ReAct execution traces and state transitions.
- **[`exercises.md`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-08/exercises.md)**: Autonomous agent building and loop restriction exercises.
- **[`solutions/autonomous_agent.py`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-08/solutions/autonomous_agent.py)**: Reference solution for a bounded ReAct multi-tool agent.

---

## 4. How to Run Day 08 Materials
```bash
python day-08/solutions/autonomous_agent.py
```
