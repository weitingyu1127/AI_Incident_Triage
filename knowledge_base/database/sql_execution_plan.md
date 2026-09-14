# SQL Execution Plan Guide

## Overview
Execution plans show how a database intends to execute a SQL query.

## Important Concepts
- Sequential Scan
- Index Scan
- Nested Loop
- Hash Join
- Merge Join
- Estimated rows
- Actual rows
- Execution time

## Example
```sql
EXPLAIN ANALYZE
SELECT *
FROM orders
WHERE customer_id = 123;
```

## Warning Signs
- Sequential scan on a very large table
- Large difference between estimated and actual rows
- Expensive nested loops
- Large sort operations
- High execution time on one plan node

## Recommended Actions
- Add or adjust indexes.
- Update table statistics.
- Rewrite inefficient joins.
- Reduce selected columns.
- Add selective filters.

## Related Documents
- SQL Slow Query
- SQL Indexing
- SQL Query Optimization
