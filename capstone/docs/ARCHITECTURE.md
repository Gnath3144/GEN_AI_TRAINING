# Capstone Architecture Specification

## 1. High-Level System Architecture

The Enterprise AI Intelligence Desk implements a layered, modular architecture designed for high availability, zero API lock-in, and strict security boundaries:

```
+-------------------------------------------------------------------------+
|                        Client & Presentation Layer                      |
|                  Streamlit Web UI  /  CLI Orchestrator                  |
+------------------------------------+------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|                      Layer 1: Security Gateway                          |
|  - Deterministic Regex Filter (Prompt Injection, Jailbreak Interception)|
|  - PII Masking Engine (Redacts Emails, SSNs, Credit Cards)              |
|  - In-Memory Exact Hash Cache (SHA-256 for 0-latency / 0-cost hits)     |
+------------------------------------+------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|                      Layer 2: Intent Router                             |
|          Directs clean prompts to the appropriate AI Subsystem          |
+------------------+-----------------+-------------------+----------------+
                   |                 |                   |
                   v                 v                   v
+----------------------+ +-----------------------+ +---------------------+
|  Subsystem A: RAG    | |  Subsystem B: Tools   | | Subsystem C: Agents |
| - ChromaDB / TF-IDF  | | - Real-time Flight DB | | - Bounded ReAct     |
| - Grounded Citations | | - Baggage Calculator  | |   Deal Hunter       |
| - InsureLLM Policies | | - Schema Validations  | | - Max 4 Steps Cap   |
+----------+-----------+ +-----------+-----------+ +----------+----------+
           |                         |                        |
           +-------------------------+------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|                      Layer 3: Telemetry & Auditing                      |
|  - Tiktoken Token Accountant                                            |
|  - Financial Cost Projector (USD)                                       |
|  - Latency Millisecond Timers                                           |
+-------------------------------------------------------------------------+
```

---

## 2. Design Principles
1. **Graceful Degradation**: If commercial cloud APIs are unreachable or unpaid, the platform automatically switches to local Ollama or deterministic fallback mocks.
2. **Defensive Prompting**: Prompts use role demarcation and strict JSON schemas, preventing model outputs from breaking downstream applications.
3. **Bounded Autonomy**: All agentic loops carry a hard maximum execution budget (4 steps) and cycle detection to prevent runaway API spend.
