# Day 07 Exercises: Security Guardrails & Caching Middleware

## Exercise 1: PII Redaction Pipeline (Warm-up)
1. Write a Python function `redact_pii(text: str) -> str` using regular expressions.
2. Automatically replace:
   - Email addresses with `[EMAIL_REDACTED]`.
   - US Social Security Numbers (`\d{3}-\d{2}-\d{4}`) with `[SSN_REDACTED]`.
   - Credit card numbers with `[CARD_REDACTED]`.
3. Verify that sanitized text can be passed to the LLM without leaking private customer data.

---

## Exercise 2: Production Guardrail & Caching Middleware (Core Project)
### User Story
As an AI security architect, I need an end-to-end middleware proxy that intercepts all incoming LLM requests to:
1. Check the in-memory exact-match cache (returning cached responses with zero token usage).
2. Scan for prompt injection, jailbreaks, and system override attempts.
3. Automatically sanitize/quarantine detected attacks and log an audit security event.
4. If clean, forward the query to the model and cache the output for subsequent queries.

### Acceptance Criteria
1. Implement a class `SecurityGuardrailMiddleware`.
2. Test against a suite of 5 benign queries and 5 adversarial injection attacks.
3. Achieve 100% interception of direct override attacks.
4. Demonstrate that a repeated query returns in under 5 milliseconds from cache.

### Reference Solution
See `solutions/security_guardrails.py`.
