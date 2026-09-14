# Incident 004 - 504 Gateway Timeout

## Summary
Checkout requests intermittently returned 504 errors.

## Symptoms
- 504 Gateway Timeout
- Checkout requests exceeded 10 seconds
- Internal service CPU normal

## Investigation
Tracing showed a third-party payment API averaging 12 seconds.

## Root Cause
Slow downstream payment provider.

## Resolution
Added a strict downstream timeout and graceful failure response.

## Prevention
Monitor downstream latency and use circuit-breaker behavior.

## Related Documents
- API Timeout
- API Retry Strategy
- API High Latency
