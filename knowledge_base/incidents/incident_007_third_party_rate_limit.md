# Incident 007 - Third-Party API Rate Limit

## Summary
Address-validation requests failed during a traffic spike.

## Symptoms
- HTTP 429
- Third-party response included `Retry-After`
- Internal services remained healthy

## Investigation
The application immediately retried each failed request three times.

## Root Cause
Burst traffic exceeded the vendor quota, and aggressive retries amplified request volume.

## Resolution
Implemented exponential backoff with jitter and request caching.

## Prevention
Monitor quota usage and honor vendor retry headers.

## Related Documents
- API Rate Limiting
- API Retry Strategy
