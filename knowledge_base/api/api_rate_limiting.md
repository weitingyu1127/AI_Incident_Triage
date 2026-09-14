# API Rate Limiting Troubleshooting

## Overview
Rate limits protect services from excessive traffic.

## Common Symptoms
- HTTP 429 responses
- Third-party API requests fail during bursts
- Errors disappear after waiting

## Recommended Client Behavior
1. Respect `Retry-After` if provided.
2. Use exponential backoff.
3. Add jitter.
4. Avoid retrying too aggressively.
5. Cache responses when appropriate.

## Example Backoff
1 second, 2 seconds, 4 seconds, 8 seconds.

## Prevention
- Batch requests where possible.
- Monitor quota usage.
- Use request queues for bursty workloads.

## Related Documents
- API Retry Strategy
- API Error Handling
