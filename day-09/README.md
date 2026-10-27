# Day 09 — Production Engineering: Web Dashboards, Observability & Testing

**Delivery Status**: `PLANNED`  
**Supporting Reference**: Derived from `ed-donner/llm_engineering` Week 2 (`day2.ipynb`, `day3.ipynb`) and Week 8 (`day5.ipynb`).

---

## 1. Session Overview
A Jupyter notebook is an experimentation sandbox, not a deployable product. To deliver real enterprise value, LLM components must be bundled into production-oriented applications with clean user interfaces, structured logging/telemetry, and automated regression test suites.

Day 09 bridges the transition from prototypes to deployable software. We build an interactive Web Application (using Streamlit or Gradio) that exposes RAG search, tool calling, and deal inspection in a responsive UI with structured latency tracking and unit tests.

---

## 2. Learning Objectives
- Architect full-stack LLM applications separating frontend presentation from core AI service layers.
- Build interactive web UIs featuring live response streaming and session history.
- Implement structured JSON telemetry logging (audit token count, latency, and cost per request).
- Write automated unit tests and regression suites using `pytest` (mocking stochastic LLM outputs).
- Prepare applications for containerization and local/cloud deployment.

---

## 3. Directory Contents
- **[`concepts.md`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-09/concepts.md)**: Web interface paradigms (Streamlit vs Gradio), token telemetry, and testing stochastic systems.
- **[`demo.ipynb`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-09/demo.ipynb)**: Walkthrough of application configuration and mocked test assertions.
- **[`exercises.md`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-09/exercises.md)**: Full-stack dashboard building and unit testing lab.
- **[`solutions/app.py`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-09/solutions/app.py)**: Production Streamlit / CLI Web Dashboard application.
- **[`solutions/test_app.py`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-09/solutions/test_app.py)**: Automated pytest regression suite.

---

## 4. How to Run Day 09 Materials

### Run Automated Unit Tests
```bash
pytest day-09/solutions/test_app.py -v
```

### Run the Web Dashboard
```bash
# Via Streamlit:
streamlit run day-09/solutions/app.py

# Or run directly in headless/CLI test mode:
python day-09/solutions/app.py --test
```
