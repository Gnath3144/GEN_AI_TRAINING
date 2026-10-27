"""Unified LLM Client with dual-track support for Cloud APIs and Local Ollama."""

import os
import json
import logging
from typing import Optional, Dict, Any, List
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)


class UnifiedLLMClient:
    """Provides a seamless interface across OpenAI, Ollama (local), and Mock fallback."""

    def __init__(self, provider: Optional[str] = None, model: Optional[str] = None):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434")

        # Determine default provider
        if provider:
            self.provider = provider.lower()
        elif self.openai_api_key and not self.openai_api_key.startswith("your_"):
            self.provider = "openai"
        else:
            self.provider = "ollama"

        # Determine default model
        if model:
            self.model = model
        elif self.provider == "openai":
            self.model = "gpt-4o-mini"
        else:
            self.model = os.getenv("OLLAMA_MODEL", "llama3.2:1b")

    def complete(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1000,
        json_mode: bool = False,
    ) -> str:
        """Execute a text completion across the configured provider."""
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        return self.chat(messages, temperature=temperature, max_tokens=max_tokens, json_mode=json_mode)

    def chat(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 1000,
        json_mode: bool = False,
    ) -> str:
        """Execute a multi-turn chat completion."""
        if self.provider == "openai":
            try:
                from openai import OpenAI
                client = OpenAI(api_key=self.openai_api_key)
                kwargs = {
                    "model": self.model,
                    "messages": messages,
                    "temperature": temperature,
                    "max_tokens": max_tokens,
                }
                if json_mode:
                    kwargs["response_format"] = {"type": "json_object"}
                response = client.chat.completions.create(**kwargs)
                return response.choices[0].message.content or ""
            except Exception as e:
                logger.warning(f"OpenAI call failed ({e}). Falling back to Ollama.")
                return self._call_ollama(messages, json_mode)

        elif self.provider == "ollama":
            return self._call_ollama(messages, json_mode)

        return self._mock_response(messages, json_mode)

    def _call_ollama(self, messages: List[Dict[str, str]], json_mode: bool = False) -> str:
        """Calls local Ollama instance via HTTP API or ollama python client."""
        try:
            import requests
            url = f"{self.ollama_host}/api/chat"
            payload = {
                "model": self.model,
                "messages": messages,
                "stream": False,
            }
            if json_mode:
                payload["format"] = "json"
            resp = requests.post(url, json=payload, timeout=60)
            if resp.status_code == 200:
                data = resp.json()
                return data.get("message", {}).get("content", "")
            else:
                logger.warning(f"Ollama returned HTTP {resp.status_code}: {resp.text}")
                return self._mock_response(messages, json_mode)
        except Exception as e:
            logger.warning(f"Could not reach Ollama at {self.ollama_host}: {e}")
            return self._mock_response(messages, json_mode)

    def _mock_response(self, messages: List[Dict[str, str]], json_mode: bool = False) -> str:
        """Deterministic fallback when no external LLM service is currently reachable."""
        last_user_msg = messages[-1]["content"] if messages else ""
        if json_mode:
            return json.dumps({
                "status": "success",
                "extracted_entities": ["Sample Entity A", "Sample Entity B"],
                "summary": f"Structured extraction for input: {last_user_msg[:50]}...",
                "confidence_score": 0.95,
                "note": "Deterministic fallback mock response (Ollama/API offline)"
            }, indent=2)
        return f"[Simulated LLM Output] Processed query: '{last_user_msg[:60]}...'. System operational."
