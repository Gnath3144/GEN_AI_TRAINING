"""Day 01 Reference Solution: Command-Line Web Page Summarizer."""

import sys
import os
import argparse
import logging
from typing import Optional
import requests
from bs4 import BeautifulSoup

# Ensure access to shared utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from shared.utils import UnifiedLLMClient, count_tokens, estimate_cost
from shared.common_prompts.system_prompts import WEB_SUMMARIZER_PROMPT

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

OFFLINE_FALLBACK_ARTICLE = """
Title: Autonomous Robot Swarms Deploy in Disaster Relief Testing
Geneva, October 2026 — Disaster response teams have completed live field simulations deploying autonomous aerial and terrestrial robot swarms in search-and-rescue operations.
Coordinated by lightweight decentralized mesh networking, the drones scan collapsed structural debris using thermal imaging sensors and LIDAR to pinpoint trapped survivors without relying on cellular towers or satellite links.
During trials, the swarm mapped a multi-story collapsed structure in under 12 minutes, identifying five simulated victim locations with zero human operator intervention.
Commercial rollout of the emergency swarm platform is scheduled for late 2027 following civil aviation regulatory clearances.
"""


def fetch_and_clean_webpage(url: str, timeout: int = 10) -> Optional[str]:
    """Fetches a web page and strips boilerplates to produce clean readable text."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Strip unhelpful elements
        for element in soup(["script", "style", "nav", "footer", "header", "noscript", "aside"]):
            element.decompose()

        text = " ".join(soup.stripped_strings)
        return text
    except requests.RequestException as e:
        logger.error(f"Failed to fetch webpage ({url}): {e}")
        return None


def summarize_content(text: str, client: UnifiedLLMClient) -> str:
    """Invokes LLM to generate an executive briefing."""
    # Truncate text if it exceeds 10,000 characters to stay within modest context budgets
    truncated_text = text[:8000] if len(text) > 8000 else text
    prompt = f"Please analyze and summarize the following web document:\n\n{truncated_text}"

    return client.complete(
        prompt=prompt,
        system_prompt=WEB_SUMMARIZER_PROMPT,
        temperature=0.3,
        max_tokens=600,
    )


def main():
    parser = argparse.ArgumentParser(description="Day 01: Command-Line Web Page Summarizer")
    parser.add_argument("--url", type=str, help="Target website URL to scrape and summarize")
    parser.add_argument("--model", type=str, default=None, help="LLM model identifier")
    args = parser.parse_args()

    client = UnifiedLLMClient(model=args.model)
    logger.info(f"Initialized LLM Client using provider='{client.provider}' model='{client.model}'")

    if args.url:
        logger.info(f"Fetching URL: {args.url}")
        content = fetch_and_clean_webpage(args.url)
        if not content:
            logger.warning("Using offline fallback article due to fetch failure.")
            content = OFFLINE_FALLBACK_ARTICLE
    else:
        logger.info("No URL provided. Running in offline demonstration mode with sample article.")
        content = OFFLINE_FALLBACK_ARTICLE

    input_tokens = count_tokens(content)
    logger.info(f"Extracted document length: {len(content)} characters (~{input_tokens} tokens)")

    print("\n" + "=" * 60)
    print("GENERATING EXECUTIVE SUMMARY...")
    print("=" * 60 + "\n")

    summary = summarize_content(content, client)
    output_tokens = count_tokens(summary)
    cost = estimate_cost(input_tokens, output_tokens, model=client.model)

    print(summary)
    print("\n" + "-" * 60)
    print(f"Metrics: Input Tokens: {input_tokens} | Output Tokens: {output_tokens} | Estimated Cost: ${cost['total_cost_usd']}")
    print("-" * 60)


if __name__ == "__main__":
    main()
