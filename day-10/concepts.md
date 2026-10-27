# Day 10 Concepts: System Integration & Architectural Defense

## 1. The Capstone Architecture

```
                                  [ User / Client ]
                                          │
                                          ▼
                         ┌─────────────────────────────────┐
                         │   Security Guardrail Gateway    │
                         │   - PII Sanitization            │
                         │   - Prompt Injection Blocking   │
                         │   - Exact Hash Cache            │
                         └────────────────┬────────────────┘
                                          │ Forward Clean Request
                                          ▼
                         ┌─────────────────────────────────┐
                         │   Intent Router & Dispatcher    │
                         └───────┬────────┬─────────┬──────┘
                                 │        │         │
                 ┌───────────────┘        │         └──────────────┐
                 ▼                        ▼                        ▼
        ┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
        │  Enterprise RAG  │    │  Airline Flight  │    │ Autonomous ReAct │
        │  Knowledge Base  │    │  Tools Service   │    │  Shopping Agent  │
        └────────┬─────────┘    └────────┬─────────┘    └────────┬─────────┘
                 │                       │                       │
                 └───────────────────────┼───────────────────────┘
                                         ▼
                         ┌─────────────────────────────────┐
                         │  Telemetry & Audit Aggregator   │
                         │  - Token Counting & Cost        │
                         │  - Latency Milliseconds         │
                         │  - Structured Output Validation │
                         └─────────────────────────────────┘
```

---

## 2. Architectural Trade-offs Matrix

| Component | Design Choice | Alternative Considered | Engineering Trade-off Justification |
| :--- | :--- | :--- | :--- |
| **Model Runtime** | Dual-Track (Local Ollama + Cloud API) | Cloud-Only API | Guarantees zero-cost offline development while maintaining production upgrade path. |
| **Vector Storage** | ChromaDB with In-Memory TF-IDF Fallback | Pinecone / Weaviate Cloud | Avoids mandatory external SaaS subscriptions and complex IAM setup. |
| **Tool Execution** | Deterministic Python Functions | Arbitrary `eval()` / Code Interpreter | Eliminates remote code execution vulnerabilities; enforces strict schema contracts. |
| **Agent Paradigm** | Bounded ReAct (Max 4 Steps) | Unbounded Multi-Agent Swarm | Prevents infinite execution loops, runaway API token bills, and debugging complexity. |
| **Security Layer** | Pre-execution Regex + Sanitizer | LLM-as-a-Judge for all inputs | Pre-execution filtering runs in under 1ms with 0 tokens consumed vs. adding 500ms latency to every call. |

---

## 3. Capstone Presentation Rubric
1. **Architectural Rigor (30%)**: Clear separation of concerns, defensive error handling, schema contracts.
2. **Subsystem Integration (30%)**: Successful interaction between RAG, tools, agent loops, and security.
3. **Observability & Testing (20%)**: Test coverage across tools and telemetry tracking for cost and latency.
4. **Defense & Explanation (20%)**: Ability to articulate design decisions, trade-offs, and failure mode mitigations.
