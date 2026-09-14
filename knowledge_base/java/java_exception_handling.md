# Java Exception Handling Guide

## Overview
Consistent exception handling improves reliability, observability, and API behavior.

## Principles
1. Catch exceptions only when you can handle or enrich them.
2. Do not silently ignore exceptions.
3. Avoid exposing sensitive stack traces to clients.
4. Log useful context and correlation IDs.
5. Return consistent error responses.

## Example
```java
try {
    orderService.create(order);
} catch (ValidationException e) {
    return ResponseEntity.badRequest().body(...);
} catch (Exception e) {
    log.error("Unexpected error creating order", e);
    return ResponseEntity.status(500).body(...);
}
```

## Recommended Error Response
```json
{
  "code": "ORDER_CREATE_FAILED",
  "message": "Unable to create order",
  "traceId": "abc-123"
}
```

## Anti-Patterns
- Empty catch blocks
- Catching `Exception` everywhere
- Returning raw exception messages
- Logging the same exception repeatedly at multiple layers

## Verification
- Error responses are consistent.
- Logs include trace IDs.
- Sensitive details are not returned to users.

## Related Documents
- API Error Handling
- Logging Best Practices
