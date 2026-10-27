# Day 08 Concepts: Autonomous Agents & ReAct Loops

## 1. The Taxonomy of AI Systems

```
Level 1: Prompt Pipeline
[User Input] ──> [LLM] ──> [Output]

Level 2: Deterministic Workflow (Router / Chain)
[User Input] ──> [Classifier] ──┬──> [Branch A] ──> [Output]
                                └──> [Branch B] ──> [Output]

Level 3: Autonomous Agent (Dynamic Loop)
                 ┌────────────────────────────────┐
                 │                                │
                 ▼                                │
[User Goal] ──> [Thought] ──> [Action (Tool)] ──> [Observation]
                 │
                 └──> If Goal Accomplished / Max Steps Reached ──> [Final Answer]
```

---

## 2. The ReAct (Reason + Act) Paradigm
Introduced by Yao et al. (2022), ReAct interleaves verbal reasoning ("Thought") with domain-specific tool execution ("Action"):

```
Thought 1: To find if the price is fair, I must first look up the current market listing.
Action 1: search_product_catalog("SmartBrew Pro")
Observation 1: {"model": "SmartBrew Pro", "msrp_usd": 599.00, "current_sale_usd": 420.00}

Thought 2: The current sale price is $420.00 vs $599.00 MSRP (a 30% discount). Now check warranty coverage.
Action 2: check_warranty_terms("SmartBrew Pro")
Observation 2: {"warranty_years": 2, "covers_leakage": true}

Thought 3: I have verified both price discount and warranty. I can now formulate the final recommendation.
Action 3: FINISH("The SmartBrew Pro is currently at a 30% discount ($420 vs $599) and includes 2-year warranty.")
```

---

## 3. Protecting Against Runaway Agent Loops
Autonomous agents can easily enter infinite cycles when tools return ambiguous data or errors.
**Mandatory Safety Boundaries**:
1. `max_iterations`: Hard cap (e.g., 5 steps max). If exceeded, synthesize best-effort answer and terminate.
2. `timeout_seconds`: Wall-clock timeout (e.g., 30s).
3. `repetition_penalty`: Detect if the agent issues the identical tool call twice consecutively.
