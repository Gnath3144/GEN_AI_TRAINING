# Day 02 Concepts: Prompt Engineering & Structured Outputs

## 1. The Anatomy of an API Request
Modern chat completion endpoints are stateless. Every invocation must bundle the entire conversation history:
```python
messages = [
    {"role": "system", "content": "You are a specialized legal document parser."},
    {"role": "user", "content": "Extract liabilities from clause 4."},
    {"role": "assistant", "content": "Clause 4 specifies a $50,000 indemnity cap."},
    {"role": "user", "content": "Does this cover third-party claims?"}
]
```
The "memory" of an LLM assistant is purely an architectural illusion maintained by client-side application state.

---

## 2. Generation Hyperparameters

| Parameter | Type | Default | Impact & Best Practice |
| :--- | :---: | :---: | :--- |
| `temperature` | Float (0.0 – 2.0) | 0.7 | Controls output randomness. Use `0.0 – 0.2` for deterministic JSON extraction, coding, and classification. Use `0.7 – 1.0` for creative writing. |
| `top_p` (Nucleus) | Float (0.0 – 1.0) | 1.0 | Alternative to temperature; considers only tokens comprising the top $P$ cumulative probability mass. (Do not adjust both `temperature` and `top_p` simultaneously). |
| `max_tokens` | Integer | Model max | Hard cutoff on generated output tokens. Critical for protecting against runaway generation loops and surprise billing. |

---

## 3. Structured Outputs with Pydantic
Unconstrained LLM outputs frequently break software parsers due to conversational filler (*"Sure, here is your data..."*) or markdown fences (` ```json `).

To ensure deterministic reliability, modern LLM engineering enforces typed data structures using **Pydantic**:
```python
from pydantic import BaseModel, Field
from typing import List, Optional

class ProductReview(BaseModel):
    product_name: str = Field(description="Exact brand and model name")
    sentiment: str = Field(description="Positive, Negative, or Mixed")
    rating: int = Field(ge=1, le=5, description="Numerical rating 1-5")
    price_paid: Optional[float] = Field(default=None, description="Purchased price in USD")
    pros: List[str] = Field(default_factory=list)
    cons: List[str] = Field(default_factory=list)
```
When paired with Native JSON mode (`response_format={"type": "json_object"}`), the model restricts its vocabulary sampling specifically to tokens conforming to JSON syntax.
