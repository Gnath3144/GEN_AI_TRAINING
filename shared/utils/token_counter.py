"""Utility to count tokens and estimate generation costs across models."""

from typing import Dict, Any

# Approximate pricing per 1M tokens (as of late 2024 / 2025)
PRICING_TABLE = {
    "gpt-4o-mini": {"input": 0.15, "output": 0.60},
    "gpt-4o": {"input": 2.50, "output": 10.00},
    "claude-3-5-sonnet": {"input": 3.00, "output": 15.00},
    "gemini-1.5-flash": {"input": 0.075, "output": 0.30},
    "llama3.2:1b": {"input": 0.00, "output": 0.00},
    "llama3.2:3b": {"input": 0.00, "output": 0.00},
}


def count_tokens(text: str, model: str = "gpt-4o-mini") -> int:
    """Calculates token length using tiktoken with standard cl100k_base or o200k_base fallback."""
    if not text:
        return 0
    try:
        import tiktoken
        try:
            encoding = tiktoken.encoding_for_model(model)
        except Exception:
            encoding = tiktoken.get_encoding("cl100k_base")
        return len(encoding.encode(text))
    except ImportError:
        # Heuristic fallback: ~4 characters per token in English
        return max(1, len(text) // 4)


def estimate_cost(input_tokens: int, output_tokens: int, model: str = "gpt-4o-mini") -> Dict[str, Any]:
    """Computes dollar cost estimate for a given token volume."""
    rates = PRICING_TABLE.get(model, PRICING_TABLE["gpt-4o-mini"])
    input_cost = (input_tokens / 1_000_000) * rates["input"]
    output_cost = (output_tokens / 1_000_000) * rates["output"]
    total_cost = input_cost + output_cost

    return {
        "model": model,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": input_tokens + output_tokens,
        "input_cost_usd": round(input_cost, 6),
        "output_cost_usd": round(output_cost, 6),
        "total_cost_usd": round(total_cost, 6),
        "is_free": rates["input"] == 0.0,
    }
