# Logging Best Practices

## Overview
Useful logs accelerate diagnosis and support reliable AI incident triage.

## Recommended Fields
- timestamp
- service
- environment
- log level
- trace ID
- request ID
- user or tenant identifier when safe
- error code
- exception type
- duration

## Example Structured Log
```json
{
  "timestamp": "2026-09-12T14:20:00Z",
  "service": "order-service",
  "level": "ERROR",
  "traceId": "abc-123",
  "error": "SQLTimeoutException",
  "durationMs": 7200
}
```

## Avoid
- Passwords
- Access tokens
- Credit card numbers
- Sensitive personal information

## Related Documents
- API Error Handling
- Incident Triage Playbook
