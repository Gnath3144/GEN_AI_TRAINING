# Day 08 Exercises: Autonomous ReAct Deal Agent

## Exercise 1: State Machine & Loop Detector (Warm-up)
1. Write a Python class `AgentLoopGuard` that tracks tool invocations.
2. If the same tool is called with the exact same arguments 2 times consecutively, throw a `LoopDetectedException`.
3. Test with both cyclic and non-cyclic tool sequences.

---

## Exercise 2: Autonomous Product Deal & Price Verification Agent (Core Project)
### User Story
As an e-commerce bargain hunter, I want an autonomous agent that can evaluate whether an advertised product discount is genuine by:
1. Searching catalog pricing.
2. Checking historical lowest price.
3. Checking competitor matching policies.
4. Formulating a strategic buy/wait recommendation.

### Acceptance Criteria
1. Define a ReAct loop with a hard ceiling of `max_steps = 4`.
2. Available tools:
   - `search_catalog(query: str) -> dict`
   - `get_historical_lowest_price(product_id: str) -> dict`
   - `check_competitor_price(product_id: str) -> dict`
3. Maintain an execution trace recording Thought, Action, and Observation at each step.
4. Return a structured final deal assessment.

### Reference Solution
See `solutions/autonomous_agent.py`.
