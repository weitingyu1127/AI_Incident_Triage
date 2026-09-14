# API Retry Strategy

## Overview
Retries can improve resilience but can also amplify outages or create duplicate operations.

## Retry When
- Connection reset
- Temporary 503
- Temporary 429
- Some 502/504 failures

## Avoid Blind Retries For
- Validation errors
- Authentication errors
- Non-idempotent operations without safeguards

## Exponential Backoff
Example:
1s → 2s → 4s → 8s

Add random jitter to avoid synchronized retries.

## Idempotency
For create operations, use an idempotency key when retries may occur.

## Related Documents
- API Rate Limiting
- API Timeout
- SQL Deadlock
