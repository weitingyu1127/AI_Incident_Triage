# Incident 001 - Orders API High Latency

## Summary
The `/orders` endpoint response time increased from approximately 800 ms to 7.2 seconds.

## Symptoms
- High API latency
- `SQLTimeoutException`
- Database CPU increased

## Investigation
The slow query was:

```sql
SELECT *
FROM orders
WHERE customer_id = ?;
```

`EXPLAIN ANALYZE` showed a sequential scan over approximately 1.2 million rows.

## Root Cause
The `customer_id` column did not have an index.

## Resolution
```sql
CREATE INDEX idx_orders_customer_id
ON orders(customer_id);
```

## Result
Latency decreased from 7.2 seconds to approximately 620 ms.

## Prevention
Review query plans for high-volume tables before production release.

## Related Documents
- SQL Slow Query
- SQL Indexing
- API High Latency
