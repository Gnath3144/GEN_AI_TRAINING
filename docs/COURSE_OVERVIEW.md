# Course Overview: LLM Engineering Masterclass

## 1. Vision & Objectives
Generative AI engineering requires moving beyond toy chat interfaces into robust, reliable, and scalable software systems. This 10-day training curriculum equips engineers with the end-to-end skills needed to build production-grade LLM applications:

- **Day 01**: Foundational execution models & local offline inference.
- **Day 02**: API orchestration, prompt engineering patterns & structured data extraction.
- **Day 03**: Resilient application wrappers & function calling / tool use.
- **Day 04**: Dense vector embeddings, chunking strategies & vector search with ChromaDB.
- **Day 05**: Advanced RAG patterns (re-ranking, hybrid search) & automated RAG evaluation.
- **Day 06**: Open-source Hugging Face ecosystem & multimodal computer vision.
- **Day 07**: Production guardrails, prompt injection security & latency caching.
- **Day 08**: Autonomous agent loops (ReAct), state management & controlled tool iteration.
- **Day 09**: Full-stack application assembly with interactive Web UIs and observability.
- **Day 10**: Capstone integration, system testing, and architecture defense.

---

## 2. Pedagogy & Classroom Rhythm
Each training day is designed around a 4-part rhythm:
1. **Concept Briefing (30-45 mins)**: Core theoretical foundations, failure modes, and architectural trade-offs.
2. **Instructor Live Demonstration (30-45 mins)**: Step-by-step walkthrough of the day's demo notebook or Python application.
3. **Learner Hands-on Lab (60-90 mins)**: Practical exercises where students implement solutions against clear validation criteria.
4. **Debrief & Solution Analysis (30 mins)**: Code review, edge cases, and industry best practices.

---

## 3. Dual-Track Architecture
To ensure accessibility regardless of corporate firewall restrictions or paid API budgets:
- **Track A (Zero-Cost Local Track)**: Uses Ollama (`llama3.2:1b`, `llama3.2:3b`), local sentence transformers, and ChromaDB. Fully functional offline.
- **Track B (Cloud Frontier Track)**: Uses OpenAI (GPT-4o / GPT-4o-mini), Google Gemini, or Anthropic Claude for high-throughput enterprise scale.
All code examples include automated fallback detection.
