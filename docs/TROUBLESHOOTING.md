# Troubleshooting Guide & Common Pitfalls

## 1. Environment & Setup Issues

### Issue: "Ollama connection refused / Failed to connect to localhost:11434"
- **Cause**: Ollama background service is not running.
- **Fix**:
  - Windows: Check your taskbar system tray and click the Ollama icon, or run `ollama serve` in a new PowerShell window.
  - macOS: Open Applications -> Ollama.
  - Linux: Run `systemctl start ollama` or `ollama serve`.

### Issue: "AuthenticationError: Incorrect API key provided"
- **Cause**: `.env` file is missing or `python-dotenv` has not loaded it.
- **Fix**: Verify that `.env` exists in the repository root and contains `OPENAI_API_KEY=sk-...` without quotes. In Python scripts, verify `from dotenv import load_dotenv; load_dotenv()`.

---

## 2. Model & Generation Issues

### Issue: "JSONDecodeError: Expecting value"
- **Cause**: The model returned conversational preamble (e.g. *"Here is your JSON:"*) or markdown backticks (` ```json `).
- **Fix**:
  - In Day 02, use Pydantic `response_format` or strip markdown code blocks using `re.sub(r"^```json|```$", "", text.strip())`.

### Issue: "RateLimitError / 429 Too Many Requests"
- **Cause**: Exhausted free tier quotas or exceeded TPM (tokens per minute).
- **Fix**: Implement exponential backoff retry using `tenacity` (see Day 03) or temporarily fall back to local Ollama.

---

## 3. ChromaDB & Vector Store Issues

### Issue: "chromadb.errors.InvalidDimensionException"
- **Cause**: You queried a collection using an embedding model with dimension $D_1$ when it was initialized with dimension $D_2$.
- **Fix**: Ensure the same embedding model (e.g. `all-MiniLM-L6-v2` = 384 dimensions) is used for both ingestion and querying. Delete the persistence directory to rebuild if necessary.
