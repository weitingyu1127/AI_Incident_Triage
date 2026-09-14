# Incident 006 - Order Update Deadlocks

## Summary
Concurrent order updates intermittently failed.

## Symptoms
- Database deadlock errors
- Failures occurred only under concurrent traffic
- Retried requests often succeeded

## Investigation
Two transaction paths updated `orders` and `inventory` in opposite order.

## Root Cause
Inconsistent lock ordering across transactions.

## Resolution
Standardized transaction order to update inventory before orders.

## Prevention
Document resource lock ordering for shared transactions.

## Related Documents
- SQL Deadlock
- API Retry Strategy
