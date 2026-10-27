# Day 06 — Open-Source Models & Multimodal AI

**Delivery Status**: `PLANNED`  
**Supporting Reference**: Derived from `ed-donner/llm_engineering` Week 2 (`day5.ipynb`) and Week 3 (`day2.ipynb`, `day4.ipynb`).

---

## 1. Session Overview
Language models are no longer purely text-in, text-out engines; modern frontier and open-weights models are multimodal Vision-Language Models (VLMs). They can inspect user-uploaded photographs, analyze equipment for physical defects, transcribe receipts, read architectural schematics, and parse messy whiteboard notes.

In Day 06, we explore the open-source model landscape (Hugging Face Transformers), understand quantization formats (GGUF / AWQ), and implement a Multimodal Image Inspection tool that accepts image inputs and produces structured audit reports.

---

## 2. Learning Objectives
- Compare hosted frontier multimodal APIs (GPT-4o, Claude 3.5 Sonnet, Gemini Flash) vs. self-hosted open vision models (Llama 3.2-Vision, Qwen2-VL, Moondream).
- Understand image tokenization: patches, visual encoders (CLIP / SigLIP), and projection layers.
- Encode and pass images via Base64 or direct file streams into multimodal LLM requests.
- Build a hardware defect and receipt inspector that produces structured JSON diagnostics from images.

---

## 3. Directory Contents
- **[`concepts.md`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-06/concepts.md)**: Multimodal architectures, patch projection, and open-source trade-offs.
- **[`demo.ipynb`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-06/demo.ipynb)**: Walkthrough of image preprocessing, base64 encoding, and VLM inspection.
- **[`exercises.md`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-06/exercises.md)**: Hardware inspection and document OCR lab specifications.
- **[`solutions/multimodal_analyzer.py`](file:///C:/Users/gnath/SJBIT_DSA/GEN_AI_TRAINING/day-06/solutions/multimodal_analyzer.py)**: Reference solution for multimodal image auditing.

---

## 4. How to Run Day 06 Materials
```bash
python day-06/solutions/multimodal_analyzer.py
```
