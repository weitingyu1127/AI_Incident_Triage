# Incident 010 - Duplicate Orders Created

## Summary
Some customers created duplicate orders after network failures.

## Symptoms
- Multiple orders with same cart content
- Client retried after timeout
- Original server request had already succeeded

## Investigation
The create-order endpoint had no idempotency protection.

## Root Cause
A non-idempotent create operation was retried after an ambiguous network timeout.

## Resolution
Added an idempotency key to order creation requests.

## Prevention
Require idempotency keys for retryable create operations.

## Related Documents
- API Retry Strategy
- API Timeout
- API Error Handling
