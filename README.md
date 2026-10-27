# Generative AI & LLM Engineering: 10-Day Masterclass

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python: 3.11+](https://img.shields.io/badge/Python-3.11%2B-brightgreen.svg)](https://www.python.org/)
[![Status: Instructor-Ready](https://img.shields.io/badge/Status-Instructor--Ready-orange.svg)]()
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing%20(16%2F16)-success.svg)]()

> A practical, code-first, 10-day training curriculum designed to transition software engineers, data scientists, and technical architects into proficient Generative AI and LLM Engineers.

---

## 1. Course Overview & Philosophy
Modern Generative AI is rapidly evolving from conversational toy demos into mission-critical production software. Building resilient enterprise applications requires deep engineering rigor: deterministic schema enforcement, bounded autonomy, vector retrieval evaluation, and defense-in-depth security guardrails.

This repository provides an instructor-led, hands-on 10-day training program. Every single day couples theoretical architectural concepts with runnable code, lab exercises, and verified reference implementations.

### The Dual-Track Guarantee
- **Local Track (Zero API Cost)**: Run fully functional open-source models offline using [Ollama](https://ollama.com/) (`llama3.2:1b`, `llama3.2:3b`), local sentence transformers, and ChromaDB.
- **Cloud Track (Frontier APIs)**: Connect to OpenAI (GPT-4o / GPT-4o-mini), Google Gemini, or Anthropic Claude for cloud-scale throughput.
- All codebases feature **automatic graceful degradation** — if API keys are absent, code executes safely with built-in resilient fallbacks.

---

## 2. Complete 10-Day Training Schedule & Progress Board

| Day | Module Title | Status | Primary Focus & Deliverables |
| :---: | :--- | :---: | :--- |
| **[Day 01](day-01/)** | **LLM Foundations & Local Models** | `COMPLETED` | Lifecycle, Ollama local setup, prompt loops, [CLI Web Page Summarizer](day-01/solutions/web_summarizer.py). |
| **[Day 02](day-02/)** | **Model APIs & Structured Outputs** | `IN_PROGRESS` | Chat completion mechanics, token budgets (`tiktoken`), Pydantic [Review Extractor](day-02/solutions/structured_extractor.py). |
| **[Day 03](day-03/)** | **Resilient Architecture & Tool Calling** | `PLANNED` | 2-turn function execution, tenacity backoff, [Airline AI Assistant](day-03/solutions/tool_calling_assistant.py). |
| **[Day 04](day-04/)** | **Embeddings, Vector Stores & RAG** | `PLANNED` | Semantic similarity, ChromaDB indexing, grounded citations, [Insurance RAG](day-04/solutions/rag_pipeline.py). |
| **[Day 05](day-05/)** | **Advanced RAG & Retrieval Evaluation** | `PLANNED` | Hybrid search, Reciprocal Rank Fusion, [Quantitative RAG Benchmark](day-05/solutions/rag_evaluation.py). |
| **[Day 06](day-06/)** | **Open-Source Models & Multimodal AI** | `PLANNED` | Vision-Language Models, base64 pipelines, [Hardware Defect Auditor](day-06/solutions/multimodal_analyzer.py). |
| **[Day 07](day-07/)** | **LLM Quality, Safety & Guardrails** | `PLANNED` | Prompt injection defense, PII sanitization, exact caching, [Security Middleware](day-07/solutions/security_guardrails.py). |
| **[Day 08](day-08/)** | **Autonomous Agents & ReAct Loops** | `PLANNED` | Reason+Act state loops, cycle boundaries, [Bounded Deal Hunter Agent](day-08/solutions/autonomous_agent.py). |
| **[Day 09](day-09/)** | **Production Web App & Observability** | `PLANNED` | Streamlit Dashboard, telemetry metrics, [Automated Pytest Regression Suite](day-09/solutions/test_app.py). |
| **[Day 10](day-10/)** | **Capstone Integration & Defense** | `PLANNED` | End-to-end integration, evaluation, architecture defense, [Capstone Platform](capstone/). |

---

## 3. Target Audience & Prerequisites
- **Target Audience**: Software Engineers, Data Engineers, Solution Architects, Tech Leads.
- **Prerequisites**:
  - Proficiency in Python (functions, OOP, exceptions, virtual environments).
  - Basic familiarity with Git, command-line interfaces, and JSON data structures.
  - No deep machine learning or GPU CUDA programming background required.

---

## 4. Quick Start & Setup Instructions

### 1. Clone the Training Repository
```bash
git clone https://github.com/Gnath3144/GEN_AI_TRAINING.git
cd GEN_AI_TRAINING
```

### 2. Set Up Virtual Environment & Dependencies
```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate       # On macOS / Linux
.venv\Scripts\Activate.ps1      # On Windows PowerShell

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Optional Local Ollama Setup (Free Local Inference)
Download and install Ollama from [ollama.com](https://ollama.com/).
```bash
ollama run llama3.2:1b
```

### 4. Optional Cloud API Configuration
Copy `.env.example` to `.env` and insert your API keys:
```bash
cp .env.example .env
```

For complete platform guides, see **[`SETUP.md`](SETUP.md)**.

---

## 5. Running Notebooks and Applications

### Interactive Jupyter Notebooks
Launch Jupyter Lab or VS Code to step through daily interactive notebooks:
```bash
jupyter lab
```
Explore `demo.ipynb` inside any day folder (e.g. `day-01/demo.ipynb`).

### Running Daily Production Scripts
```bash
# Day 01: Web Page Summarizer CLI
python day-01/solutions/web_summarizer.py

# Day 02: Schema-Validated Review Extractor
python day-02/solutions/structured_extractor.py

# Day 03: Airline Customer Service Tool Calling Assistant
python day-03/solutions/tool_calling_assistant.py

# Day 04: Grounded Policy RAG Pipeline
python day-04/solutions/rag_pipeline.py

# Day 05: Automated RAG Benchmark & MRR Evaluation
python day-05/solutions/rag_evaluation.py

# Day 06: Multimodal Hardware Defect Auditor
python day-06/solutions/multimodal_analyzer.py

# Day 07: Security Guardrail & Caching Middleware
python day-07/solutions/security_guardrails.py

# Day 08: Bounded Autonomous ReAct Deal Agent
python day-08/solutions/autonomous_agent.py

# Day 09: Production Web Dashboard (CLI mode or Streamlit)
python day-09/solutions/app.py --test
streamlit run day-09/solutions/app.py

# Day 10: Capstone Multi-Service System
python day-10/solutions/capstone_orchestrator.py
```

### Running Automated Test Verification
```bash
pytest -v
```

---

## 6. Model Selection & Cost-Conscious Guidance
- **Local Ollama Models (`llama3.2:1b`, `llama3.2:3b`)**: $0.00 cost, private, offline. Ideal for rapid iteration, testing prompts, and lab exercises.
- **Cloud Models (`gpt-4o-mini`, `gemini-1.5-flash`)**: Extremely low cost (<$0.15 per million tokens).
- **Exact Hash Caching**: Repeated prompt executions hit the Day 07 in-memory cache at **0 ms latency and 0 tokens**.
For a detailed cost matrix, consult **[`docs/API_COST_AND_MODEL_OPTIONS.md`](docs/API_COST_AND_MODEL_OPTIONS.md)**.

---

## 7. Capstone Project: Enterprise AI Intelligence Desk
The program culminates in **[The Enterprise AI Intelligence Desk](capstone/)**, an integrated operations platform uniting:
- Pre-execution security gateway and PII sanitizer.
- Semantic RAG over company policies with citation provenance.
- Live database tool calling (flight schedules, baggage fees).
- Autonomous ReAct market intelligence agent.
- Structured JSON telemetry and latency metrics.

---

## 8. Documentation Quick Links
- **[`10_DAY_CURRICULUM.md`](10_DAY_CURRICULUM.md)**: Full syllabus, learning outcomes, and assessment rubrics.
- **[`SOURCE_REPOSITORY_ANALYSIS.md`](SOURCE_REPOSITORY_ANALYSIS.md)**: Analysis of the reference repository and curriculum conversion rationale.
- **[`docs/TRAINER_GUIDE.md`](docs/TRAINER_GUIDE.md)**: Instructor delivery notes, pacing, and debrief guidelines.
- **[`docs/LEARNER_GUIDE.md`](docs/LEARNER_GUIDE.md)**: Student study handbook and best practices.
- **[`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md)**: Solutions for common setup, API, and JSON decoding issues.

---

## 9. Attribution & Licensing
This training program is adapted and redesigned from the 8-week *LLM Engineering* masterclass created by **[Ed Donner](https://github.com/ed-donner/llm_engineering)**, licensed under the **MIT License**.

All adapted and newly created materials in this repository preserve copyright notices, license compliance, and educational attribution.
