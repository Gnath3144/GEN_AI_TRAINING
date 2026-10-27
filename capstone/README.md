# Capstone Project: The Enterprise AI Intelligence Desk

## 1. Project Overview
The Enterprise AI Intelligence Desk is a unified, multi-service Generative AI platform that serves enterprise analysts, customer support agents, and operations teams.

It consolidates the 10-day curriculum into an integrated production architecture:
1. **Security & Governance Gateway**: Sanitizes PII, blocks prompt injections, and manages exact hash caching.
2. **Grounded Policy Knowledge Base (RAG)**: Retrieves verified company documentation with strict source citations.
3. **Operational Tool Dispatcher**: Executes live database queries and calculations (flight status, baggage fee calculations).
4. **Autonomous Shopping & Deal Intelligence Agent**: Executes bounded ReAct reasoning loops to verify pricing anomalies and deal integrity.
5. **Observability & Telemetry Engine**: Logs latency, token volume, and estimated dollar costs per transaction.

---

## 2. Directory Structure
```
capstone/
├── README.md                   # Project overview & documentation
├── src/                        # Core application source code
│   ├── __init__.py
│   └── intelligence_desk.py    # Production platform service orchestrator
├── tests/                      # Automated regression test suite
│   ├── __init__.py
│   └── test_capstone.py        # Pytest test cases
└── docs/                       # Architectural documentation
    ├── ARCHITECTURE.md         # Deep-dive architecture & dataflow
    └── DEPLOYMENT.md           # Production deployment runbook
```

---

## 3. Quick Start & Execution

### Run the Capstone Orchestrator
```bash
python capstone/src/intelligence_desk.py
```

### Run Automated Tests
```bash
pytest capstone/tests/test_capstone.py -v
```
