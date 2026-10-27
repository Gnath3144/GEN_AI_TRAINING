# Day 03 Exercises: Airline Customer Service Assistant

## Exercise 1: Resilient Wrapper with Tenacity (Warm-up)
1. Write a function that calls `client.complete()` with simulated random 500 errors (1 in 2 chance of failure).
2. Apply `@retry` from the `tenacity` library with exponential backoff (e.g., wait 1s, 2s, 4s).
3. Confirm that the function successfully recovers after transient failures.

---

## Exercise 2: Airline Customer Support Assistant (Core Project)
### User Story
As an airline passenger, I want to ask questions in natural language such as:
- *"Is flight SK-204 on time and what gate is it?"*
- *"I have 2 bags weighing 48kg on flight SK-419, how much will I be charged?"*

### Acceptance Criteria
1. Load flight and baggage data from `shared/sample_data/flight_data.json`.
2. Define two Python tools:
   - `lookup_flight(flight_number: str) -> dict`
   - `calculate_baggage_fee(bag_count: int, total_weight_kg: float) -> dict`
3. Implement a dispatcher that detects user intent, parses necessary arguments, runs the tool, and feeds the output back into the LLM for natural language response generation.
4. Handle edge cases gracefully: unknown flight numbers, negative baggage counts, missing data.
5. Provide sample interactive queries demonstrating successful flight lookup and baggage calculation.

### Reference Solution
See `solutions/tool_calling_assistant.py`.
