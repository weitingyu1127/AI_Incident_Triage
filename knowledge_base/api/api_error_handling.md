# API Error Handling Guide

## Overview
API error handling should provide useful client feedback while preserving internal security.

## Recommended Error Format
```json
{
  "code": "ORDER_NOT_FOUND",
  "message": "The requested order does not exist.",
  "traceId": "abc-123"
}
```

## Principles
- Use correct HTTP status codes.
- Never expose stack traces to clients.
- Include a trace ID.
- Log internal technical details.
- Keep client messages stable and understandable.

## Server Errors
For unexpected failures:
1. Log the exception.
2. Attach request/trace context.
3. Return a generic 500 response.
4. Alert if error rate exceeds threshold.

## Related Documents
- HTTP Status Codes
- Logging Best Practices
- Java Exception Handling
