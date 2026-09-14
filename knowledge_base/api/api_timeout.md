# API Timeout Troubleshooting

## Overview
An API timeout occurs when a request does not complete within the allowed time.

## Common Symptoms
- 504 Gateway Timeout
- Client-side timeout
- `SQLTimeoutException`
- Requests succeed for small payloads but fail for large ones

## Common Causes
1. Slow database query
2. Slow downstream service
3. Thread pool exhaustion
4. Network issue
5. Excessively large payload
6. Timeout configured too aggressively

## Diagnosis
1. Trace request duration by component.
2. Check database query time.
3. Check downstream API latency.
4. Check thread and connection pools.
5. Review timeout values.

## Recommended Fixes
- Optimize the slow dependency.
- Add bounded retries only for safe operations.
- Set realistic timeouts.
- Use asynchronous processing for long jobs.
- Add circuit breakers where appropriate.

## Related Documents
- API High Latency
- SQL Slow Query
- Java Thread Pool
- API Retry Strategy
