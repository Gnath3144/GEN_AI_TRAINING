# Day 10 Exercises: Capstone Project & Architectural Defense

## Capstone Deliverable Checklist
Every student or team must deliver and present a fully functional **Enterprise AI Intelligence Desk**:

- [ ] **Dual-Track Execution**: Verified to run against either local Ollama or cloud frontier APIs without code modifications.
- [ ] **Grounded Knowledge Retrieval**: RAG search over enterprise documentation with strict source citations.
- [ ] **Deterministic Tool Calling**: Controlled Python tool execution with input validation and graceful failure handling.
- [ ] **Autonomous ReAct Agent**: Dynamic multi-step reasoning bounded by maximum iteration limits.
- [ ] **Defense-in-Depth Security**: Prompt injection detection, PII sanitization, and exact-match caching.
- [ ] **Automated Regression Suite**: Passing `pytest` test suite covering core deterministic contracts.
- [ ] **Observability Telemetry**: Structured JSON telemetry recording latency, token volume, and estimated dollar costs.

## Final Defense Presentation Guidelines
Prepare a 10-minute presentation covering:
1. System Architecture Diagram and Component Flow (2 mins).
2. Live Interactive Demonstration across RAG, Tools, and Agent (4 mins).
3. Security Guardrail and Caching Defense Demonstration (2 mins).
4. Engineering Trade-offs and Lessons Learned (2 mins).
