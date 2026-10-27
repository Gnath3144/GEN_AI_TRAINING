# 10-Day LLM Engineering Training Curriculum

## Program Overview
*Codealytica — CODE. ANALYZE. BUILD. GROW.*

- **Trainer**: **Gopinath** — Data Engineer | Generative AI & LLM Engineering
- **Course Name**: Generative AI & LLM Engineering: 10-Day Practical Training Program
- **Format**: 10-Day Intensive Practical Training (Lectures, Live Demos, Guided Labs, and Capstone Project)
- **Target Audience**: Software Engineers, Data Engineers, and Technical Practitioners transitioning into Generative AI engineering
- **Core Pedagogy**: "Code-First, Theory-Supported" — Every concept is immediately validated with runnable Python code or interactive notebooks. Dual-track support for local open models (Ollama) and commercial cloud APIs (OpenAI / Gemini / Anthropic).
- **Attribution & Reference**: Curated and adapted from Ed Donner's 8-Week *LLM Engineering* reference curriculum (MIT License).

---

## Program Delivery Status Board

| Day | Title | Delivery Status | Date / Timeline |
| :---: | :--- | :---: | :---: |
| **Day 01** | LLM Engineering Foundations, Application Lifecycle & Local Models | **COMPLETED** | Yesterday (Delivered Oct 26, 2026) |
| **Day 02** | Model APIs, Prompt Engineering & Structured JSON Outputs | **IN_PROGRESS** | Today (Active Session Oct 27, 2026) |
| **Day 03** | Resilient LLM Application Architecture & Tool / Function Calling | **PLANNED** | Day 03 Delivery |
| **Day 04** | Embeddings, Vector Stores & Foundational RAG Architectures | **PLANNED** | Day 04 Delivery |
| **Day 05** | Advanced RAG, Contextual Grounding & Retrieval Evaluation | **PLANNED** | Day 05 Delivery |
| **Day 06** | Open-Source Models, Transformers & Multimodal AI | **PLANNED** | Day 06 Delivery |
| **Day 07** | LLM Application Quality, Cost Optimization & Security Guardrails | **PLANNED** | Day 07 Delivery |
| **Day 08** | Autonomous Agents, Workflow Orchestration & State Machines | **PLANNED** | Day 08 Delivery |
| **Day 09** | Production Engineering: UI Dashboards, Logging & Automated Testing | **PLANNED** | Day 09 Delivery |
| **Day 10** | Capstone System Integration, Evaluation & Defense Presentation | **PLANNED** | Day 10 Delivery |

---

## Detailed Day-by-Day Specifications

### Day 01 — LLM Engineering Foundations, Application Lifecycle & Local Models
- **Status**: **COMPLETED** (Delivered yesterday; all artifacts preserved)
- **Learning Objectives**:
  - Understand the end-to-end lifecycle of an LLM-powered software application.
  - Distinguish between traditional software engineering, classical ML, and LLM engineering.
  - Set up a reproducible local environment using Python 3.11+, UV / venv, and Ollama.
  - Run small local open-weights models (`llama3.2:1b`, `llama3.2:3b`, or `phi3`) offline.
  - Perform zero-cost local inference and build a command-line assistant.
- **Key Concepts**:
  - Prompt -> Model -> Completion execution cycle.
  - Latency, memory footprint, and parameter quantizations (Q4_K_M).
  - Web scraping for dynamic context ingestion.
- **Practical Activities**:
  - Lab 1: Verify Ollama installation and local model inference via CLI.
  - Lab 2: Run `demo.ipynb` exploring prompt execution through local Ollama API.
  - Lab 3: Build a command-line Web Page Summarizer that fetches a website and generates a structured summary.
- **Required Tools & Dependencies**: `python>=3.11`, `ollama`, `beautifulsoup4`, `requests`, `python-dotenv`.
- **Expected Deliverables**: Working CLI summarizer (`day-01/solutions/web_summarizer.py`) and verified local model runtime.
- **Source Derivation**: `week1/day1.ipynb`, `week1/scraper.py`, `setup/`.

---

### Day 02 — Model APIs, Prompt Engineering & Structured JSON Outputs
- **Status**: **IN_PROGRESS** (Active delivery today)
- **Learning Objectives**:
  - Integrate frontier and open LLM APIs (OpenAI, Gemini, Anthropic, or LiteLLM / local Ollama API).
  - Master role separation: `system`, `user`, `assistant`, and `tool` messages.
  - Control generation parameters: `temperature`, `top_p`, `max_tokens`, `frequency_penalty`.
  - Enforce schema-constrained outputs using Pydantic and JSON mode.
  - Calculate token consumption and cost modeling using `tiktoken`.
- **Key Concepts**:
  - The "illusion of memory" in stateless HTTP completions.
  - Few-shot prompting, chain-of-thought prompting, and delimiter hygiene.
  - Structured extraction vs. unstructured generation.
- **Practical Activities**:
  - Lab 1: Token counting and cost calculator across model providers.
  - Lab 2: Build a Structured Information Extractor that ingests unstructured customer reviews or invoices and outputs validated Pydantic JSON schemas.
- **Required Tools & Dependencies**: `openai`, `google-genai`, `tiktoken`, `pydantic>=2.0`, `python-dotenv`.
- **Expected Deliverables**: Schema-validated JSON extraction engine (`day-02/solutions/structured_extractor.py`).
- **Source Derivation**: `week1/day2.ipynb`, `week1/day4.ipynb`, `week1/day5.ipynb`.

---

### Day 03 — Resilient LLM Application Architecture & Tool / Function Calling
- **Status**: **PLANNED**
- **Learning Objectives**:
  - Design resilient LLM service wrappers with retry policies, rate limit handling, and graceful degradation.
  - Understand the mechanics of Tool/Function Calling: JSON Schema declaration, tool dispatch, execution loop, and response synthesis.
  - Securely manage API credentials and prevent tool permission leakage.
- **Key Concepts**:
  - Two-turn Tool Calling lifecycle (`model -> tool_call -> local execution -> tool_result -> final response`).
  - Idempotent tools vs. side-effecting operations.
  - Fallback cascades (e.g., Cloud API -> Local Ollama fallback).
- **Practical Activities**:
  - Implement a Customer Support / Flight Assistance agent with controlled Python tools (calculating baggage fees, looking up flight status).
- **Required Tools & Dependencies**: `openai`, `pydantic`, `tenacity`.
- **Expected Deliverables**: Python tool-calling assistant (`day-03/solutions/tool_calling_assistant.py`).
- **Source Derivation**: `week2/day4.ipynb`, `week1/solution.py`.

---

### Day 04 — Embeddings, Vector Stores & Foundational RAG Architectures
- **Status**: **PLANNED**
- **Learning Objectives**:
  - Understand dense vector embeddings and semantic similarity metrics (Cosine, Dot Product, Euclidean).
  - Implement document loading and chunking strategies (fixed size, recursive character, markdown aware).
  - Store and query high-dimensional embeddings using ChromaDB.
  - Build an end-to-end Retrieval-Augmented Generation (RAG) pipeline with grounded citation references.
- **Key Concepts**:
  - The Chunking Dilemma: Chunk size vs. semantic coherence vs. context window budget.
  - Bi-encoder embedding models (`all-MiniLM-L6-v2`, `text-embedding-3-small`).
  - Context grounding and preventing out-of-domain hallucinations.
- **Practical Activities**:
  - Ingest an Enterprise Knowledge Base (PDF / Markdown manuals) into ChromaDB and build a grounded Question-Answering system.
- **Required Tools & Dependencies**: `chromadb>=0.5.0`, `sentence-transformers`, `numpy`.
- **Expected Deliverables**: Document RAG pipeline with source attribution (`day-04/solutions/rag_pipeline.py`).
- **Source Derivation**: `week5/day1.ipynb`, `week5/day2.ipynb`, `week5/day3.ipynb`.

---

### Day 05 — Advanced RAG, Contextual Grounding & Retrieval Evaluation
- **Status**: **PLANNED**
- **Learning Objectives**:
  - Identify failure modes in naive RAG: lost-in-the-middle, poor recall, false positives.
  - Implement advanced retrieval techniques: hybrid search (BM25 + Dense vector), cross-encoder re-ranking, and query decomposition.
  - Implement automated RAG evaluation metrics: Context Relevance, Groundedness (Faithfulness), and Answer Relevance.
- **Key Concepts**:
  - Lexical vs. Semantic retrieval strengths and reciprocal rank fusion (RRF).
  - Synthetic test set generation and automated LLM-as-a-Judge evaluation.
- **Practical Activities**:
  - Benchmark baseline vector search vs. re-ranked hybrid search on an insurance policy benchmark dataset.
- **Required Tools & Dependencies**: `chromadb`, `rank-bm25`, `sentence-transformers`, `pandas`.
- **Expected Deliverables**: Comparative RAG evaluation benchmark notebook (`day-05/solutions/rag_evaluation.py`).
- **Source Derivation**: `week5/day4.ipynb`, `week5/day5.ipynb`, `week5/evaluator.py`.

---

### Day 06 — Open-Source Models, Transformers & Multimodal AI
- **Status**: **PLANNED**
- **Learning Objectives**:
  - Explore the Hugging Face ecosystem and the `transformers` pipeline.
  - Understand trade-offs between self-hosted open models (Llama 3, Mistral, Qwen) and proprietary APIs.
  - Integrate Vision-Language Models (VLM) for multimodal image understanding and document OCR analysis.
- **Key Concepts**:
  - Quantization techniques: FP16, INT8, INT4 (GGUF, AWQ, GPTQ).
  - Image tokenization and visual prompt construction.
- **Practical Activities**:
  - Build a Multimodal Inspector that analyzes hardware images / receipts and extracts structured defect or itemization reports.
- **Required Tools & Dependencies**: `transformers`, `torch`, `pillow`, `google-genai` / `openai`.
- **Expected Deliverables**: Multimodal image audit application (`day-06/solutions/multimodal_analyzer.py`).
- **Source Derivation**: `week2/day5.ipynb`, `week3/day2.ipynb`, `week3/day4.ipynb`.

---

### Day 07 — LLM Application Quality, Cost Optimization & Security Guardrails
- **Status**: **PLANNED**
- **Learning Objectives**:
  - Detect and mitigate prompt injection, jailbreaks, and indirect prompt injection attacks.
  - Implement deterministic input sanitization, PII redaction, and output guardrails.
  - Optimize application performance through semantic caching and prompt compression.
- **Key Concepts**:
  - OWASP Top 10 for LLM Applications (Prompt Injection, Insecure Output Handling, Data Poisoning).
  - Exact match vs. semantic caching.
- **Practical Activities**:
  - Red-team an LLM application with malicious prompt injections and harden it with a multi-layered guardrail validator.
- **Required Tools & Dependencies**: `pydantic`, `hashlib`, `scikit-learn`.
- **Expected Deliverables**: Hardened security middleware with attack test suites (`day-07/solutions/security_guardrails.py`).
- **Source Derivation**: `week1/day4.ipynb`, `week2/day1.ipynb`, industry safety standards.

---

### Day 08 — Autonomous Agents, Workflow Orchestration & State Machines
- **Status**: **PLANNED**
- **Learning Objectives**:
  - Understand the continuum: Prompt -> Pipeline -> Deterministic DAG -> Autonomous Agent.
  - Implement bounded ReAct (Reason + Act) loop architectures with strict termination conditions.
  - Manage agent state, memory scratchpads, and human-in-the-loop approvals.
- **Key Concepts**:
  - ReAct thought-action-observation cycles.
  - Preventing infinite execution loops and cascading failures.
  - Specialized role collaboration (Planner, Executor, Reviewer).
- **Practical Activities**:
  - Build a Multi-Step Research & Deal Finder Agent that plans, queries multiple tools, cross-checks findings, and synthesizes a recommendation.
- **Required Tools & Dependencies**: `python-dotenv`, `pydantic`.
- **Expected Deliverables**: Bounded autonomous research agent (`day-08/solutions/autonomous_agent.py`).
- **Source Derivation**: `week8/day1.ipynb` – `day4.ipynb`, `week8/deal_agent_framework.py`.

---

### Day 09 — Production Engineering: UI Dashboards, Logging & Automated Testing
- **Status**: **PLANNED**
- **Learning Objectives**:
  - Wrap backend LLM pipelines into interactive, user-friendly web interfaces using Streamlit or Gradio.
  - Implement structured JSON telemetry, token auditing, and latency logging.
  - Write unit tests and deterministic regression suites for stochastic LLM systems.
- **Key Concepts**:
  - Asynchronous streaming responses (`yield` / SSE) for optimal perceived latency.
  - Mocking LLM responses for CI/CD test automation.
- **Practical Activities**:
  - Build a complete Streamlit / Gradio web application with live response streaming, session state management, and telemetry logs.
- **Required Tools & Dependencies**: `streamlit>=1.30.0` or `gradio>=4.0`, `pytest`, `structlog`.
- **Expected Deliverables**: Production web interface with automated test suite (`day-09/solutions/app.py`).
- **Source Derivation**: `week2/day2.ipynb`, `week2/day3.ipynb`, `week8/day5.ipynb`.

---

### Day 10 — Capstone System Integration, Evaluation & Defense Presentation
- **Status**: **PLANNED**
- **Learning Objectives**:
  - Integrate concepts from Days 01–09 into an end-to-end Enterprise AI solution:
    - Multi-provider model configuration (Local Ollama / Cloud API).
    - Grounded RAG knowledge retrieval with source attribution.
    - Controlled tool execution and guardrail validation.
    - Interactive web interface with streaming and observability telemetry.
  - Execute automated evaluation benchmarks.
  - Document architecture, trade-offs, security considerations, and deployment guidelines.
- **Capstone Project**: "The Enterprise AI Intelligence Desk" (or customized domain application such as InsureTech or Retail Intelligence).
- **Deliverables**:
  - Full codebase in `capstone/` with `src/`, `tests/`, and documentation.
  - Architecture diagram and benchmark evaluation report.
- **Source Derivation**: `week8/price_is_right.py`, `week5/pro_implementation/`.

---

## 5. Topics Intentionally Removed, Shortened, or Made Optional

| Topic from Original 8-Week Course | Modification | Justification for 10-Day Training Program |
| :--- | :---: | :--- |
| **Python to C++ Code Generation (Week 4)** | **Removed** | Niche optimization topic requiring local C++ compilers; minimal relevance to mainstream GenAI enterprise application development. |
| **Classical ML / Tabular Baselines (Week 6)** | **Shortened** | Extensive EDA, Random Forests, and XGBoost take excessive time; condensed into Day 05 evaluation principles. |
| **Full Open-Source Fine-Tuning (Week 7)** | **Made Optional** | Fine-tuning 7B+ parameter models requires expensive GPU instances and several hours of training runs, which risk stalling interactive classroom sessions. Covered conceptually in Day 06. |
| **Modal.com Cloud Serverless Infrastructure (Week 8)** | **Optional Extension** | Cloud serverless orchestration requires third-party accounts and credit cards; replaced with portable local container / standard Python architecture. |
| **Excessive Setup Guides (14 Guides)** | **Streamlined** | Consolidated into a single, bulletproof `SETUP.md` with explicit scripts for Mac, Windows, and Linux. |
