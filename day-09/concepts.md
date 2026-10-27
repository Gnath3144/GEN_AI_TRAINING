# Day 09 Concepts: Production Engineering & Testing

## 1. Clean Architecture for LLM Applications

```
┌────────────────────────────────────────────────────────┐
│           Presentation Layer (UI / API)                │
│     Streamlit Dashboard / FastAPI Endpoints / CLI      │
└──────────────────────────┬─────────────────────────────┘
                           │ Dispatches
                           ▼
┌────────────────────────────────────────────────────────┐
│           Application & Orchestration Layer            │
│     Agent Controller / Guardrails / RAG Pipeline       │
└──────────────┬───────────────────────────┬─────────────┘
               │ Calls                     │ Logs Telemetry
               ▼                           ▼
┌───────────────────────────┐  ┌─────────────────────────┐
│     Model Service Layer   │  │  Telemetry & Audit Log  │
│  UnifiedLLMClient / Tools │  │  Latency, Tokens, Cost  │
└───────────────────────────┘  └─────────────────────────┘
```

---

## 2. Testing Non-Deterministic Stochastic Systems
Traditional tests assert `assert calculate(2, 2) == 4`. LLMs do not produce identical byte-for-byte strings across runs.

**Strategies for Testing LLMs**:
1. **Mocking**: For deterministic CI/CD, mock the model completion and test that the application handles errors, schema parsing, and database transactions correctly.
2. **Schema & Contract Assertions**: Assert that the output adheres to the expected Pydantic model (`isinstance(result, TargetModel)`).
3. **Property-Based Assertions**:
   - Assert `len(response) > 20`.
   - Assert required keywords or cited source tags (e.g., `"[KB-101]"` in answer).
   - Assert latency does not exceed timeout budgets.

---

## 3. Observability & Telemetry
In production, every single generation must record a structured telemetry event:
```json
{
  "timestamp": "2026-10-27T23:00:00Z",
  "request_id": "REQ-9921",
  "model": "gpt-4o-mini",
  "input_tokens": 142,
  "output_tokens": 68,
  "cost_usd": 0.000062,
  "latency_ms": 380,
  "cache_hit": false,
  "guardrail_status": "CLEAN"
}
```
This enables financial forecasting, anomalous usage alerts, and debugging user issues.
