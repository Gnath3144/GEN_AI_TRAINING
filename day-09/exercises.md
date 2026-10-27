# Day 09 Exercises: Full-Stack Web Application & Test Suite

## Exercise 1: Structured Telemetry Logger (Warm-up)
1. Write a decorator `@log_llm_telemetry` that measures function execution time, token volume, and logs a JSON structured event to `stdout`.
2. Apply the decorator to `client.complete()` and inspect the logged telemetry payload.

---

## Exercise 2: Production Web Dashboard & Pytest Suite (Core Project)
### User Story
As an operations team lead, I need a unified Web Dashboard that allows analysts to:
1. Search the Insurance Policy Knowledge Base (RAG).
2. Check Flight Status and calculate baggage fees (Tool Calling).
3. Evaluate Product Deals (Autonomous Agent).
4. View real-time token telemetry and latency metrics.

### Acceptance Criteria
1. Implement the multi-feature dashboard in `solutions/app.py`.
2. Support both interactive browser mode and automated command-line evaluation mode (`--test`).
3. Create `solutions/test_app.py` with unit tests for:
   - Tool calling calculation correctness.
   - Guardrail injection interception.
   - RAG citation presence.
4. All unit tests must pass with `pytest`.

### Reference Solution
See `solutions/app.py` and `solutions/test_app.py`.
