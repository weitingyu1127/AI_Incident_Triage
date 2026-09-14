# HTTP Status Codes for APIs

## Overview
Consistent status codes help clients understand failures and retry behavior.

## Common Codes
- 200 OK: Request succeeded
- 201 Created: Resource created
- 400 Bad Request: Invalid input
- 401 Unauthorized: Authentication missing or invalid
- 403 Forbidden: Authenticated but not allowed
- 404 Not Found: Resource does not exist
- 409 Conflict: Resource state conflict
- 429 Too Many Requests: Rate limit exceeded
- 500 Internal Server Error: Unexpected application failure
- 502 Bad Gateway: Invalid response from upstream
- 503 Service Unavailable: Service temporarily unavailable
- 504 Gateway Timeout: Upstream service timed out

## Troubleshooting Guidance
A 5xx response usually indicates server-side or dependency issues.
A 4xx response usually indicates client request, auth, or authorization issues.

## Related Documents
- API Error Handling
- API Timeout
- API Rate Limiting
