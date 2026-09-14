# API High Latency Troubleshooting

## Overview
High latency means an API responds more slowly than expected even if it does not fail.

## Common Causes
1. Slow SQL query
2. Slow downstream API
3. Thread pool saturation
4. Connection pool saturation
5. Excessive serialization
6. Large payloads
7. CPU or memory pressure

## Diagnosis
Break request time into:
- application time
- database time
- downstream service time
- queue time
- network time

Use tracing when possible.

## Example
If total latency is 7 seconds and database time is 6.2 seconds, database investigation should be prioritized.

## Verification
Track p50, p95, and p99 latency after each fix.

## Related Documents
- SQL Slow Query
- API Timeout
- Java Thread Pool
- SQL Connection Pool
