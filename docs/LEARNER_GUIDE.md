# Learner Guide & Study Handbook

Welcome to the 10-Day LLM Engineering Program! This guide helps you navigate the course materials and maximize your learning.

---

## 1. How Each Day is Structured
Inside each `day-XX/` directory, you will find:
- **`README.md`**: Day overview, agenda, prerequisites, and expected deliverables.
- **`concepts.md`**: Core theoretical explanations and architectural patterns.
- **`demo.ipynb` / demo script**: Hands-on walkthrough designed for instructor demonstration and personal exploration.
- **`exercises.md`**: Practical lab specifications with user stories, test cases, and acceptance criteria.
- **`solutions/`**: Reference code solutions provided by the instructor for post-lab review.

---

## 2. Recommended Study Routine
1. **Read `concepts.md`** before or immediately following the lecture.
2. **Execute the demo code cell-by-cell**, modifying inputs to observe how the LLM reacts.
3. **Attempt the exercises in `exercises.md` independently** before looking at the `solutions/` folder.
4. **Log your token usage and latency** to develop an intuitive feel for cost and performance.

---

## 3. Core Golden Rules of LLM Engineering
1. **Never trust unstructured text**: Always validate LLM responses with schemas (Pydantic / JSON).
2. **Handle errors defensively**: Assume network timeouts, rate limits, and occasional hallucinations will happen.
3. **Guard your API keys**: Never hardcode secrets in notebooks or commit `.env` to Git.
4. **Measure before optimizing**: Benchmark simple baselines before adding complex agent loops or multi-stage RAG pipelines.
