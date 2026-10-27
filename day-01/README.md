# Day 01 — LLM Engineering Foundations & Local Models

**Delivery Status**: `COMPLETED`  
**Delivered Date**: Yesterday (October 26, 2026)  
**Supporting Reference**: Derived from `ed-donner/llm_engineering` Week 1 (`day1.ipynb`, `scraper.py`, `setup/`).

---

## 1. Session Overview
Day 01 introduces software engineers to the modern LLM Engineering lifecycle. Rather than treating LLMs as mystical chatbots, we treat them as stochastic text-in, text-out transformation engines that can be embedded into deterministic software architectures.

We establish the foundation of our course by executing models locally using **Ollama**, ensuring all participants can build, test, and iterate without API credit dependencies.

---

## 2. Learning Objectives Achieved
- [x] Contrasted classical software engineering vs. LLM-augmented engineering.
- [x] Installed and configured the local Python development environment with Ollama.
- [x] Pulled and ran `llama3.2:1b` (and `llama3.2:3b`) on local CPU/GPU hardware.
- [x] Implemented raw HTTP / SDK inference requests against local model endpoints.
- [x] Combined live HTML web fetching (`beautifulsoup4`) with LLM prompt pipelines.
- [x] Built and demonstrated a runnable command-line Web Page Summarizer.

---

## 3. Directory Contents
- **[`concepts.md`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-01/concepts.md)**: Deep dive into the LLM engineering lifecycle, quantization, and local runtimes.
- **[`demo.ipynb`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-01/demo.ipynb)**: Interactive notebook demonstrating local Ollama inference and web scraping.
- **[`exercises.md`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-01/exercises.md)**: Practical student lab instructions and challenge scenarios.
- **[`solutions/web_summarizer.py`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-01/solutions/web_summarizer.py)**: Instructor reference solution for the Web Page Summarizer CLI.

---

## 4. How to Run Day 01 Materials

### 1. Ensure Ollama is running
```bash
ollama run llama3.2:1b
```

### 2. Run the Solution CLI
```bash
python day-01/solutions/web_summarizer.py --url https://en.wikipedia.org/wiki/Artificial_intelligence
```
*(If no network or offline, omitting `--url` defaults to built-in sample text).*
