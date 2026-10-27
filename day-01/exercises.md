# Day 01 Exercises: Local Inference & Web Page Summarizer

## Exercise 1: Local Model Exploration (Warm-up)
1. Ensure your local Ollama runtime is responsive.
2. Execute a curl or python script sending a prompt to `http://localhost:11434/api/generate`.
3. Experiment with temperature parameters (e.g., `0.1` vs `0.9`) on a creative vs factual prompt. Note the differences.

---

## Exercise 2: Command-Line Web Page Summarizer (Core Project)
### User Story
As a technical analyst, I want to provide a website URL via the command line and receive an executive briefing summarizing:
- The product/organization mission (1-2 sentences).
- 3 to 5 key features or announcements.
- Estimated reading time and token cost.

### Acceptance Criteria
1. The script must accept a `--url` argument via `argparse`.
2. It must fetch the URL using `requests` with a valid User-Agent header and a timeout.
3. It must clean the HTML using `BeautifulSoup`, stripping `<script>`, `<style>`, `<nav>`, and `<footer>`.
4. It must submit the cleaned text to the LLM (using `UnifiedLLMClient` or local Ollama).
5. If the URL cannot be fetched or is invalid, it must fail gracefully without crashing.
6. Provide a working fallback mode when run without `--url` for offline testing.

### Reference Solution
Review `solutions/web_summarizer.py` when you have completed your implementation.
