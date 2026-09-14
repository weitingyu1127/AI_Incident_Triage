# Incident 005 - Database Connection Pool Exhaustion

## Summary
The order service stopped processing requests during peak traffic.

## Symptoms
- `Connection is not available`
- Many threads waiting for DB connection
- Database remained reachable

## Investigation
Pool metrics showed all 20 connections active with long transactions.

## Root Cause
A new batch endpoint kept transactions open while performing external API calls.

## Resolution
Moved external calls outside the database transaction and shortened transaction scope.

## Prevention
Track connection checkout time and transaction duration.

## Related Documents
- SQL Connection Pool
- Java Database Connection
- API Timeout
