# Day 01 Concepts: LLM Foundations & Local Runtimes

## 1. What is an LLM Really?
At its computational core, an autoregressive Large Language Model is a probability distribution over sequences of text tokens:
$$P(w_1, w_2, \dots, w_n) = \prod_{i=1}^n P(w_i \mid w_1, \dots, w_{i-1})$$

When an application invokes an LLM, the model does not "think" or "search a database"; it computes dot products across billions of parameter weights to predict the most statistically probable next token given the context window.

---

## 2. The LLM Application Lifecycle
```
[User Problem / Input]
         │
         ▼
[Deterministic Pre-processing] (Sanitization, Document Fetching, Template Formatting)
         │
         ▼
[Context Assembly & Prompting] (System Instructions, Dynamic Data, Few-shot Examples)
         │
         ▼
[Inference Engine] (Local Ollama / Cloud API)
         │
         ▼
[Post-Processing & Validation] (JSON Parsing, Schema Check, Fallback Logic)
         │
         ▼
[User Output / Application State Update]
```

---

## 3. Why Run Local Models with Ollama?
- **Zero API Incurred Cost**: Run thousands of experiment cycles during development without burning cloud credits.
- **Data Privacy & Compliance**: Sensitive corporate data never traverses third-party network boundaries.
- **Offline Reliability**: Code runs seamlessly on airplanes, disconnected branches, or inside strict VPCs.
- **Model Quantization (GGUF)**: Ollama compresses 16-bit floating point weights into 4-bit integers (`Q4_K_M`), allowing a 3-billion parameter model like `llama3.2:3b` to operate inside ~2.2 GB of RAM with negligible loss in practical reasoning quality.
