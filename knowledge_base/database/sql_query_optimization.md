# SQL Query Optimization Guide

## Overview
Query optimization reduces database work and improves response time.

## Common Improvements
1. Avoid `SELECT *` when unnecessary.
2. Add selective filters.
3. Use appropriate indexes.
4. Avoid functions on indexed columns when possible.
5. Reduce unnecessary joins.
6. Use pagination for large result sets.
7. Batch operations carefully.

## Example
Instead of:
```sql
SELECT *
FROM orders
WHERE DATE(created_at) = '2026-09-01';
```

Prefer a range:
```sql
SELECT id, customer_id, status
FROM orders
WHERE created_at >= '2026-09-01'
  AND created_at < '2026-09-02';
```

## Verification
- Compare execution plans.
- Measure query latency before and after.
- Monitor database CPU and I/O.

## Related Documents
- SQL Indexing
- SQL Execution Plan
- SQL Slow Query
