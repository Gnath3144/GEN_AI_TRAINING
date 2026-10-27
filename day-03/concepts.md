# Day 03 Concepts: Application Resilience & Tool Calling

## 1. The Anatomy of Tool Calling (2-Turn Cycle)

Unlike deterministic programming where code calls a function directly, Tool Calling uses the LLM as an **orchestrator**:

```
Turn 1:
User -> "What is the status of flight SK-204?"
Client -> Sends messages + list of available tool JSON Schemas to LLM.
LLM -> Recognizes need for external data; responds with tool_call:
       { "name": "get_flight_status", "arguments": { "flight_number": "SK-204" } }

Turn 2:
Client -> Executes local Python function `get_flight_status("SK-204")` -> returns `{"status": "On Time", "gate": "B12"}`.
Client -> Appends `tool_call` and `tool` result message to history and calls LLM again.
LLM -> Ingests tool result and synthesizes natural response:
       "Flight SK-204 is on time and departing from Gate B12."
```

---

## 2. JSON Schema Declaration
Every tool must be defined as a JSON schema so the model knows its argument types and descriptions:
```python
flight_tool_schema = {
    "type": "function",
    "function": {
        "name": "lookup_flight",
        "description": "Look up current departure status, gate, and schedule for a flight",
        "parameters": {
            "type": "object",
            "properties": {
                "flight_number": {
                    "type": "string",
                    "description": "The airline flight code, e.g. SK-204"
                }
            },
            "required": ["flight_number"]
        }
    }
}
```

---

## 3. Resilience & Rate Limiting
Production LLM calls fail frequently due to:
- HTTP 429: Rate Limit / Quota Exceeded.
- HTTP 503 / 500: Server-side provider transient outage.
- Network socket timeouts.

We wrap critical API calls using exponential backoff with jitter via the `tenacity` library:
```python
from tenacity import retry, stop_after_attempt, wait_random_exponential

@retry(wait=wait_random_exponential(min=1, max=30), stop=stop_after_attempt(3))
def resilient_call(prompt):
    return client.complete(prompt)
```
