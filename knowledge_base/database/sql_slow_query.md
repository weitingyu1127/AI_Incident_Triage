# SQL Slow Query Troubleshooting

## Overview
Slow SQL queries can cause API latency, timeouts, and high database resource usage.

## Common Symptoms
- API response time increases
- `SQLTimeoutException`
- Database CPU usage is high
- Query execution exceeds several seconds
- Peak traffic causes severe degradation

## Common Causes
1. Missing index
2. Full table scan
3. Inefficient JOIN
4. Large result set
5. Lock contention
6. Poor query plan

## Diagnosis

### Step 1: Identify the Query
Use application logs, APM traces, or database slow-query logs.

### Step 2: Run EXPLAIN or EXPLAIN ANALYZE
Inspect whether the database uses an index or performs a sequential scan.

### Step 3: Check Indexes
Columns in `WHERE`, `JOIN`, and sometimes `ORDER BY` clauses may require indexes.

### Step 4: Check Row Counts
A query that was fast at 10,000 rows may become slow at 1,000,000 rows.

## Example
```sql
SELECT *
FROM orders
WHERE customer_id = 123;
```

If `customer_id` is not indexed, the database may scan the entire table.

## Recommended Fix
```sql
CREATE INDEX idx_orders_customer_id
ON orders(customer_id);
```

## Verification
1. Run `EXPLAIN ANALYZE` again.
2. Compare execution time.
3. Monitor API latency.
4. Check database CPU usage.

## Related Documents
- SQL Indexing
- SQL Execution Plan
- API High Latency
