# SQL Connection Pool Troubleshooting

## Overview
A database connection pool reuses connections instead of opening a new connection for every request.

## Common Symptoms
- `Connection timeout`
- Application threads wait for database connections
- Database itself appears healthy
- Errors increase during traffic spikes

## Common Causes
1. Connections are not returned.
2. Transactions remain open too long.
3. Pool size is too small.
4. Queries are too slow.
5. Too many application instances share a limited database.

## Diagnosis
Monitor:
- active connections
- idle connections
- waiting requests
- average checkout time
- query duration

## Recommended Fixes
- Fix connection leaks.
- Optimize slow queries.
- Configure pool size based on database capacity.
- Set connection acquisition timeout.
- Shorten transactions.

## Related Documents
- Java Database Connection
- SQL Slow Query
- API Timeout
