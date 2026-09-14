# SQL Deadlock Troubleshooting

## Overview
A deadlock occurs when two transactions each wait for a resource held by the other.

## Common Symptoms
- Transaction aborted by database
- Deadlock errors in logs
- Failures occur intermittently under concurrency
- Same operations succeed when retried

## Example
Transaction A:
1. Locks Order 1
2. Tries to lock Order 2

Transaction B:
1. Locks Order 2
2. Tries to lock Order 1

## Diagnosis
- Inspect database deadlock logs.
- Identify statements and resources involved.
- Compare lock ordering across transactions.

## Recommended Fixes
1. Access shared resources in consistent order.
2. Keep transactions short.
3. Add appropriate indexes.
4. Retry safe transactions.
5. Avoid unnecessary locking.

## Verification
- Deadlock count decreases.
- Retry rate decreases.
- Transaction latency remains stable.

## Related Documents
- SQL Query Optimization
- API Retry Strategy
