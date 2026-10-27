# Source Repository Analysis: ed-donner/llm_engineering

## 1. Executive Summary
The reference repository `https://github.com/ed-donner/llm_engineering` is an 8-week masterclass created by Ed Donner (released under the MIT License). It covers the full lifecycle of Large Language Model (LLM) application development, ranging from running local inference with Ollama up to building a 7-agent collaborative system deployed on cloud serverless infrastructure.

This document analyzes the original repository's architecture, dependencies, weekly modules, educational trade-offs, and provides the architectural rationale for condensing and refining it into an intensive, practical **10-Day Training Program**.

---

## 2. Source Repository Overview
- **Repository URL**: `https://github.com/ed-donner/llm_engineering.git`
- **License**: MIT License (Copyright (c) 2024 Ed Donner)
- **Primary Languages & Tools**: Python (>=3.11), Jupyter Notebooks, Gradio, LangChain, ChromaDB, HuggingFace Transformers, PyTorch, LiteLLM, Ollama, Modal, OpenAI / Anthropic / Gemini SDKs.
- **Repository Scale**: 8 Weekly folders, 14 Guides, 34 Jupyter notebooks, standalone Python utility modules, and multi-agent scripts.

---

## 3. Structural Decomposition of Original Curriculum

### Week 1 — Getting Started & Frontier APIs
- **Core Topics**:
  - Environment setup (Cursor, UV, Python virtual environment, Ollama).
  - Calling frontier LLMs via chat completions API (`openai`).
  - Web scraping with `BeautifulSoup4` + summarization.
  - Tokenization mechanics (`tiktoken`), token counting, cost tracking.
  - Context windows and the "illusion of memory" in stateless LLM APIs.
  - Building a company brochure generator from live website URLs.
- **Key Artifacts**: `week1/day1.ipynb`, `day2.ipynb`, `day4.ipynb`, `day5.ipynb`, `scraper.py`, `solution.py`.
- **Strengths**: Immediate practical payoff; hands-on web extraction; clear introduction to prompt engineering.
- **Limitations**: Excessive emphasis on specific IDEs (Cursor); redundant installation guides across platforms.

### Week 2 — User Interfaces, Conversations & Function Calling
- **Core Topics**:
  - Frontier Model APIs comparison (OpenAI, Anthropic Claude, Google Gemini).
  - Building interactive Web UIs using Gradio.
  - Multi-turn conversational chatbots with stateful history management.
  - Tool/Function Calling: JSON schemas, executing Python functions, passing execution results back to the LLM.
  - Multimodal inputs: analyzing images with GPT-4o / Claude 3.5 Sonnet.
  - Milestone Project: Airline Customer Service Assistant with flight lookup, baggage tracking, and image luggage verification.
- **Key Artifacts**: `week2/day1.ipynb` – `day5.ipynb`, `week2 EXERCISE.ipynb`.
- **Strengths**: Outstanding project-driven progression; realistic function calling architecture; clean Gradio UI demo.
- **Limitations**: Heavy reliance on paid frontier API keys without offline fallbacks.

### Week 3 — Open Source Models & Hugging Face
- **Core Topics**:
  - Google Colab GPU environment setup.
  - Hugging Face `transformers` high-level `pipeline` API (sentiment, generation, summarization).
  - Tokenizer internals: BPE, WordPiece, byte-pair tokenizers, padding, truncation.
  - Model architectures: CausalLM, Seq2Seq, encoder-only models.
  - Audio processing with Whisper for speech-to-text meeting minutes.
- **Key Artifacts**: `week3/day1.ipynb` – `day5.ipynb`, `visualizer.py`.
- **Strengths**: Strong conceptual demystification of open-source model architectures.
- **Limitations**: Many notebooks are thin wrappers redirecting to external Google Colab links; high hardware requirements for local execution.

### Week 4 — Frontier Model Code Generation & Benchmarking
- **Core Topics**:
  - LLM-assisted code generation: converting Python functions to optimized C++.
  - Execution benchmarking, runtime comparisons, and correctness validation.
- **Key Artifacts**: `week4/day3.ipynb`, `day4.ipynb`, `day5.ipynb`, `system_info.py`.
- **Strengths**: Highlights practical latency speedups achieved by combining LLMs with compiled languages.
- **Limitations**: Highly specialized use case (Python to C++ transpilation); requires local C++ toolchains; does not justify full week in an enterprise GenAI training schedule.

### Week 5 — Retrieval-Augmented Generation (RAG)
- **Core Topics**:
  - Document parsing, semantic chunking strategies, overlap management.
  - Embedding models (`all-MiniLM-L6-v2`, OpenAI `text-embedding-3-small`).
  - Vector database storage and similarity querying using ChromaDB.
  - End-to-end RAG pipeline using LangChain 0.3.
  - RAG Evaluation: measuring context relevance, answer faithfulness, hallucination metrics.
  - "Pro RAG": native chunking without framework bloat, LLM-based boundary extraction, hybrid lexical/semantic search.
  - Practical Domain: "InsureLLM" corporate insurance policy question answering.
- **Key Artifacts**: `week5/day1.ipynb` – `day5.ipynb`, `evaluator.py`, `implementation/`, `pro_implementation/`.
- **Strengths**: Exceptional enterprise relevance; clear progression from basic RAG to evaluation and production nuances.
- **Limitations**: Some code tightly couples older LangChain abstractions with newer native approaches, creating conceptual overlap.

### Week 6 — "The Price is Right" Part 1: Baselines & Fine-Tuning Setup
- **Core Topics**:
  - Business problem: predicting product prices from ecommerce descriptions.
  - Dataset preparation: Amazon metadata scraping, data cleaning, train/validation/test splits.
  - Baselines: Mean baseline, Ridge regression, Random Forest, XGBoost.
  - Deep Learning baseline: PyTorch MLP with embeddings.
  - Prompted LLM zero-shot and few-shot price predictions.
  - OpenAI fine-tuning: preparing JSONL formatted datasets, launching fine-tuning jobs.
- **Key Artifacts**: `week6/day1.ipynb` – `day5.ipynb`, `redemption_run.ipynb`, `pricer/`.
- **Strengths**: Rigorous ML mindset: proves that LLMs must be benchmarked against simple classical models.
- **Limitations**: Extensive time spent on traditional tabular ML and data munging, which is out of scope for a focused 10-day LLM training course.

### Week 7 — "The Price is Right" Part 2: Open Source Model Fine-Tuning
- **Core Topics**:
  - Parameter-Efficient Fine-Tuning (PEFT): LoRA and QLoRA.
  - Unsloth acceleration library on Colab GPUs.
  - Weights & Biases (WandB) experiment tracking.
  - Quantization (4-bit, 8-bit NF4) and inference deployment.
- **Key Artifacts**: `week7/day1.ipynb` – `day5.ipynb`, Colab external links.
- **Strengths**: Modern techniques for adapting open-source weights cost-effectively.
- **Limitations**: Requires GPU compute (Google Colab T4/A100 or RunPod); fine-tuning runs can take hours, causing unpredictability in an instructor-led classroom.

### Week 8 — "The Price is Right" Part 3: Multi-Agent Systems & Deployment
- **Core Topics**:
  - Micro-agents with specialized roles:
    - `SpecialistAgent`: estimates prices using specialized rules / fine-tuned model.
    - `FrontierAgent`: estimates prices using frontier reasoning LLMs.
    - `EnsembleAgent`: combines specialist and frontier opinions into weighted predictions.
    - `ScannerAgent`: crawls product deals and flags anomalies.
    - `MessengerAgent`: dispatches notifications and summaries.
    - `AutonomousPlannerAgent`: orchestrates workflow execution based on goal directives.
  - Serverless cloud execution via Modal.com.
  - Full Gradio UI dashboard connecting all agents.
- **Key Artifacts**: `week8/day1.ipynb` – `day5.ipynb`, `deal_agent_framework.py`, `price_is_right.py`, `pricer_service.py`.
- **Strengths**: Demonstrates realistic multi-agent collaboration and real-world system architecture.
- **Limitations**: Modal.com setup adds third-party platform friction; multi-agent complexity can overwhelm learners if introduced prematurely.

---

## 4. Synthesis & Gap Analysis for a 10-Day Training Format

| Evaluation Dimension | Source Repository Status | 10-Day Requirement & Adaptation Strategy |
| :--- | :--- | :--- |
| **Duration & Pacing** | 8 Weeks (40 study days) | Streamline to 10 high-impact, focused training days. |
| **Prerequisites & Tooling** | Relies on Cursor IDE, Google Colab GPUs, Modal cloud | Standardize on VS Code / Cursor + standard Python venv + local Ollama / lightweight APIs. |
| **Cost & API Keys** | Requires OpenAI, Anthropic, Gemini, Modal, WandB accounts | Provide dual-track options: Free local execution (Ollama + SentenceTransformers + Chroma) alongside commercial APIs. |
| **Redundant Content** | Lengthy platform setup, repetitive scraper variations, C++ transpilation | Eliminate Weeks 4 (C++) and condense Week 6 (classical ML) into a concise evaluation segment. |
| **RAG Treatment** | Split across basic and "pro" with scattered files | Combine into a unified 2-day sequence: Foundations (Day 04) and Advanced RAG + Evaluation (Day 05). |
| **Agentic AI** | Deferred until Week 8 with 7 complex agents | Introduce bounded agent workflows in Day 08 and deploy production full-stack apps in Day 09 & 10. |

---

## 5. Licensing & Attribution Notice
- All material adapted from `ed-donner/llm_engineering` is credited to **Ed Donner** under the **MIT License**.
- Derivative materials in `GEN_AI_TRAINING` preserve copyright notices and document structural transformations made for classroom delivery.
