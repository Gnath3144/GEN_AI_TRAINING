# Trainer Delivery Guide

## 1. Instructor Role & Responsibilities
As the instructor, your goal is to bridge the gap between AI hype and practical engineering rigor. Keep sessions active, code-centric, and focused on production failure modes rather than idealized benchmarks.

---

## 2. Session Delivery Checklist

### Before Each Day
- [ ] Ensure local Ollama is running (`ollama list`) or verify cloud API quotas.
- [ ] Review the `concepts.md` and run the `demo.ipynb` / demo script in advance.
- [ ] Ensure students have activated their virtual environment (`.venv`).
- [ ] Verify that sample datasets exist in `shared/sample_data/`.

### During the Live Demonstration
- Code live whenever possible rather than just stepping through pre-computed cells.
- Intentionally trigger common errors (e.g., malformed JSON output, hallucinated dates, rate limits) to demonstrate debugging techniques.
- Emphasize the **Token Budget** and cost implications of prompt designs.

### During Hands-on Exercises
- Point learners to `exercises.md` in the current day's folder.
- Solutions are housed in `solutions/` — do not reveal these prematurely.
- Encourage students to test edge cases (e.g., empty strings, adversarial inputs, unexpected schema keys).

---

## 3. Pacing & Time Allocation

| Segment | Allocated Time | Objective |
| :--- | :--- | :--- |
| **Recap & Warm-up** | 15 mins | Review previous day's key concepts and answer lingering questions. |
| **New Concept Lecture** | 45 mins | Present architecture diagrams, trade-offs, and theory. |
| **Live Demo** | 45 mins | Walk through interactive demo code step-by-step. |
| **Break** | 15 mins | Rest and allow background installs if needed. |
| **Learner Lab** | 75 mins | Independent or pair coding on assigned exercises. |
| **Solution Debrief** | 30 mins | Live code review of reference solution and edge-case discussion. |

---

## 4. Handling Classroom Friction
- **"My API Key failed / rate limited"**: Switch student to the local Ollama fallback (`OLLAMA_HOST=http://localhost:11434`).
- **"My laptop is slow with Ollama"**: Downgrade the local model from `llama3.2:3b` to `llama3.2:1b` (runs smoothly on 8GB RAM).
- **"The model returned invalid JSON"**: Walk through Day 02 Pydantic schema enforcement and retry wrappers.
