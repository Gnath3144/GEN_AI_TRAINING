# Model Selection, API Cost & Local Runtime Options

This course offers dual-track flexibility: you can complete the entire curriculum without spending a cent using local models, or use commercial APIs for cloud-scale throughput.

---

## 1. Provider Comparison Matrix

| Provider / Model | Execution Type | Cost Per Million Tokens (Input / Output) | RAM / Hardware Needed | Best Used For |
| :--- | :---: | :---: | :---: | :--- |
| **Ollama: `llama3.2:1b`** | Local CPU/GPU | **$0.00 (Free)** | 4 GB - 8 GB RAM | Fast local development, offline labs, simple extraction. |
| **Ollama: `llama3.2:3b`** | Local CPU/GPU | **$0.00 (Free)** | 8 GB - 16 GB RAM | High-quality local reasoning, function calling. |
| **OpenAI: `gpt-4o-mini`** | Cloud API | ~$0.15 / $0.60 | Standard internet connection | High-volume production, evaluation judge, RAG baseline. |
| **OpenAI: `gpt-4o`** | Cloud API | ~$2.50 / $10.00 | Standard internet connection | Complex agent reasoning, multimodal vision. |
| **Google Gemini: `gemini-1.5-flash`** | Cloud API | Free tier / ~$0.075 / $0.30 | Standard internet connection | Massive context window (1M tokens), fast response. |
| **Anthropic: `claude-3-5-sonnet`** | Cloud API | ~$3.00 / $15.00 | Standard internet connection | Advanced coding, structured reasoning. |

---

## 2. Managing API Costs in Practice
- **Use Small Models for Development**: Test prompt templates and JSON schemas against `llama3.2:1b` or `gpt-4o-mini` before switching to `gpt-4o`.
- **Set Spend Hard Limits**: In OpenAI and Anthropic billing consoles, set a monthly hard limit of $5–$10 for the duration of the course.
- **Cache Vector Embeddings**: In RAG modules, compute document embeddings once and save them to disk (ChromaDB) rather than recalculating them on every run.
- **Monitor Token Usage**: Use the `tiktoken` utility from Day 02 to calculate exact costs before sending requests.
