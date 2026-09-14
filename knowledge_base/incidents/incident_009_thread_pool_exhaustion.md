# Incident 009 - Peak Traffic Thread Pool Exhaustion

## Summary
Search API latency increased sharply during peak traffic.

## Symptoms
- p95 latency above 8 seconds
- CPU below 50%
- Request queue increased continuously

## Investigation
Thread dumps showed most worker threads waiting on a slow downstream search service.

## Root Cause
Worker thread pool exhausted by blocking downstream calls.

## Resolution
Added downstream timeout, increased pool capacity moderately, and moved requests to asynchronous I/O.

## Prevention
Monitor thread utilization and request queue length.

## Related Documents
- Java Thread Pool
- API High Latency
- API Timeout
