# Day 06 Concepts: Vision-Language Models & Multimodality

## 1. How Vision-Language Models Work
A Vision-Language Model (VLM) combines a visual perception encoder with an autoregressive language backbone:

```
[ Input Image (e.g. 512x512) ]
             │
             ▼
[ Patch Extraction (14x14 or 16x16 pixel tiles) ]
             │
             ▼
[ Vision Encoder (ViT / SigLIP) ] -> Converts patches to visual embeddings
             │
             ▼
[ Linear Projection / Cross-Attention Adapter ] -> Projects visual tokens into LLM embedding space
             │
             ▼
[ Autoregressive LLM Transformer ] -> Ingests [Visual Tokens] + [Text Prompt Tokens] -> Generates Text
```

---

## 2. Image Tokenization Cost & Resolution Trade-offs
- A $1024 \times 1024$ image split into $16 \times 16$ patches yields $64 \times 64 = 4096$ visual tokens.
- Most APIs downsample or tile high-resolution images into standardized grids.
- **Cost Impact**: In frontier APIs (e.g. GPT-4o), high-detail image evaluation typically consumes ~800 to 1,200 tokens per image.

---

## 3. Base64 Encoding vs Direct URL
In production REST APIs, images are passed as data URLs:
```python
import base64

def encode_image(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
```
The payload is delivered inside the user message:
```python
messages = [{
    "role": "user",
    "content": [
        {"type": "text", "text": "Describe the physical defect on this server rack component."},
        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_str}"}}
    ]
}]
```
