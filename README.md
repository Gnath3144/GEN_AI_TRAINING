# Generative AI & LLM Engineering: 10-Day Training Program

*Codealytica — CODE. ANALYZE. BUILD. GROW.*

---

### Trainer
**Gopinath** — Data Engineer | Generative AI & LLM Engineering

> Gopinath is a Data Engineer at Deloitte with experience in data engineering, analytics, and Generative AI. He focuses on building practical data solutions and exploring how large language models can be used to develop intelligent applications. This training takes learners from foundational LLM concepts to hands-on AI application development through practical demonstrations, coding exercises, and real-world use cases.

---

## 1. Course Focus & Engineering Journey
This repository contains a practical, code-first 10-day training program designed to teach engineers how to design, build, evaluate, and deploy production-grade Large Language Model (LLM) applications using Python.

The curriculum centers strictly on real-world engineering:
- **Python-based LLM application development**: Structuring clean services, managing environments, and handling errors.
- **LLM APIs and prompt engineering**: System framing, parameter controls, few-shot patterns, and token economics.
- **Structured outputs and tool calling**: Enforcing Pydantic schemas and executing controlled Python functions.
- **Embeddings, semantic search, and RAG**: Document chunking, ChromaDB vector stores, and citation-grounded answering.
- **Open-source models and multimodal AI**: Self-hosted models via Ollama and vision-language diagnostics.
- **LLM evaluation, reliability, and safety**: Mitigating prompt injection, PII sanitization, caching, and quantitative RAG metrics.
- **Agents and workflow orchestration**: Implementing bounded ReAct (Reason + Act) autonomous loops.
- **Building and demonstrating working applications**: Delivering web dashboards and an end-to-end Capstone project.

### Dual-Track Architecture (Local & Cloud)
- **Local Track (Zero Cost)**: Run models offline using [Ollama](https://ollama.com/) (`llama3.2:1b`, `llama3.2:3b`), local sentence transformers, and ChromaDB.
- **Cloud Track (Frontier APIs)**: Connect seamlessly to OpenAI (GPT-4o / GPT-4o-mini), Google Gemini, or Anthropic Claude.
- **Graceful Fallbacks**: All codebases feature automated fallback detection — if cloud API keys are absent, scripts degrade gracefully to local Ollama or deterministic mock fixtures without crashing.

---

## 2. 10-Day Schedule & Delivery Status

| Day | Module Title | Status | Core Hands-On Deliverable |
| :---: | :--- | :---: | :--- |
| **[Day 01](day-01/)** | **LLM Foundations & Local Models** | `COMPLETED` *(Delivered Oct 26)* | [CLI Web Page Summarizer](day-01/solutions/web_summarizer.py) |
| **[Day 02](day-02/)** | **Model APIs & Structured Outputs** | `IN_PROGRESS` *(Active Oct 27)* | [Pydantic Customer Review Extractor](day-02/solutions/structured_extractor.py) |
| **[Day 03](day-03/)** | **Resilient Architecture & Tool Calling** | `PLANNED` | [Airline Customer Service Assistant](day-03/solutions/tool_calling_assistant.py) |
| **[Day 04](day-04/)** | **Embeddings, Vector Stores & RAG** | `PLANNED` | [Grounded Policy QA Pipeline](day-04/solutions/rag_pipeline.py) |
| **[Day 05](day-05/)** | **Advanced RAG & Retrieval Evaluation** | `PLANNED` | [Quantitative RAG Benchmark & MRR Scorecard](day-05/solutions/rag_evaluation.py) |
| **[Day 06](day-06/)** | **Open-Source Models & Multimodal AI** | `PLANNED` | [Hardware Defect VLM Auditor](day-06/solutions/multimodal_analyzer.py) |
| **[Day 07](day-07/)** | **LLM Quality, Safety & Guardrails** | `PLANNED` | [Security Guardrail & Caching Middleware](day-07/solutions/security_guardrails.py) |
| **[Day 08](day-08/)** | **Autonomous Agents & ReAct Loops** | `PLANNED` | [Bounded Autonomous ReAct Deal Agent](day-08/solutions/autonomous_agent.py) |
| **[Day 09](day-09/)** | **Production Web App & Observability** | `PLANNED` | [Multi-Feature Dashboard & Pytest Suite](day-09/solutions/app.py) |
| **[Day 10](day-10/)** | **Capstone Integration & Defense** | `PLANNED` | [The Enterprise AI Intelligence Desk](capstone/) |

---

## 3. Quick Start & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Gnath3144/GEN_AI_TRAINING.git
cd GEN_AI_TRAINING
```

### 2. Set Up Virtual Environment & Dependencies
```bash
# On macOS / Linux:
python3 -m venv .venv
source .venv/bin/activate

# On Windows (PowerShell):
python -m venv .venv
.venv\Scripts\Activate.ps1

# Install requirements:
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
For complete platform setup instructions, see **[`SETUP.md`](SETUP.md)**.

---

## 4. Running Daily Labs and Verification

### Interactive Notebooks
Launch Jupyter to explore daily demos:
```bash
jupyter lab
```
Navigate to `demo.ipynb` inside each day folder (e.g. `day-01/demo.ipynb`).

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

## 5. Capstone Project: Enterprise AI Intelligence Desk
The program culminates in **[The Enterprise AI Intelligence Desk](capstone/)**, an integrated operations platform uniting:
- Pre-execution security gateway and PII sanitizer.
- Semantic RAG over company policies with citation provenance.
- Live database tool calling (flight schedules, baggage fees).
- Autonomous ReAct market intelligence agent.
- Structured JSON telemetry and latency metrics.

---

## 6. Documentation Quick Links
- **[`10_DAY_CURRICULUM.md`](10_DAY_CURRICULUM.md)**: Full syllabus, learning outcomes, and assessment rubrics.
- **[`SOURCE_REPOSITORY_ANALYSIS.md`](SOURCE_REPOSITORY_ANALYSIS.md)**: Analysis of the reference repository and curriculum conversion rationale.
- **[`docs/COURSE_OVERVIEW.md`](docs/COURSE_OVERVIEW.md)**: Course vision, objectives, and pedagogical rhythm.
- **[`docs/TRAINER_GUIDE.md`](docs/TRAINER_GUIDE.md)**: Instructor delivery notes, pacing, and debrief guidelines.
- **[`docs/LEARNER_GUIDE.md`](docs/LEARNER_GUIDE.md)**: Student study handbook and best practices.
- **[`docs/API_COST_AND_MODEL_OPTIONS.md`](docs/API_COST_AND_MODEL_OPTIONS.md)**: Model selection matrix and cost management guidance.
- **[`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md)**: Solutions for common setup, API, and JSON decoding issues.

---

## 7. Attribution & Licensing
This training program is curated and adapted from the 8-week *LLM Engineering* reference curriculum created by **[Ed Donner](https://github.com/ed-donner/llm_engineering)**, licensed under the **MIT License**.

All adapted and newly created materials in this repository preserve copyright notices, license compliance, and educational attribution.
