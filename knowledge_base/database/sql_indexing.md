# SQL Indexing Guide

## Overview
Indexes allow databases to locate rows without scanning an entire table. Correct indexes can dramatically reduce query latency.

## Good Candidates for Indexing
- Frequently filtered columns
- Join keys
- Foreign keys
- High-selectivity columns
- Frequently sorted columns

## Example
```sql
CREATE INDEX idx_orders_customer_id
ON orders(customer_id);
```

## Composite Index
```sql
CREATE INDEX idx_orders_customer_status
ON orders(customer_id, status);
```

Column order matters.

## Common Problems
1. Too many indexes slow writes.
2. Index exists but query cannot use it.
3. Low-selectivity index provides little benefit.
4. Composite index columns are in the wrong order.

## Diagnosis
Use `EXPLAIN ANALYZE` and verify the plan uses the expected index.

## Verification
- Query execution time decreases.
- Sequential scan is removed where appropriate.
- Write performance remains acceptable.

## Related Documents
- SQL Slow Query
- SQL Execution Plan
- SQL Query Optimization
