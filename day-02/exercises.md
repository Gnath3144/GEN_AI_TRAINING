# Day 02 Exercises: Structured Information Extraction

## Exercise 1: Token Counting & Financial Projection (Warm-up)
1. Write a script using `tiktoken` that takes a 1,000-word text document.
2. Calculate the exact token length under the `cl100k_base` and `o200k_base` encodings.
3. Calculate the projected cost to process 1,000,000 such documents through `gpt-4o-mini`, `gpt-4o`, and `llama3.2:1b` (local).

---

## Exercise 2: Production Customer Review Parser (Core Project)
### User Story
As an e-commerce data pipeline engineer, I need to parse messy, multi-sentence customer reviews into structured database records containing:
- Product name.
- Sentiment classification (`Positive`, `Negative`, `Neutral`, or `Mixed`).
- Extracted purchase price (numerical float or `null`).
- Numeric satisfaction rating (1 to 5).
- Clean list of pros and cons.

### Acceptance Criteria
1. Define a strict Pydantic model (`CustomerReviewExtraction`) matching the above requirements.
2. Ingest the dataset at `shared/sample_data/unstructured_reviews.json`.
3. Process each review using `UnifiedLLMClient` with structured JSON mode enabled.
4. Implement a sanitization step that strips any unintended markdown backticks (` ```json `) prior to Pydantic parsing.
5. If validation fails, attempt one automated retry with an error-correction prompt.
6. Print a formatted summary table of all extracted reviews and log token statistics.

### Reference Solution
Refer to `solutions/structured_extractor.py`.
