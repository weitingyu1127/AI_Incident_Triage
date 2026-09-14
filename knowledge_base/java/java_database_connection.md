# Java Database Connection Troubleshooting

## Overview
Java applications commonly access databases through JDBC and a connection pool. Connection failures can cause timeouts, 500 errors, or complete service outages.

## Common Symptoms
- `SQLException`
- `Connection is not available`
- Requests fail when traffic increases
- Database appears healthy but application cannot connect
- Connections remain open for a long time

## Common Causes
1. Connection pool exhaustion
2. Connection leak
3. Incorrect database credentials
4. Network interruption
5. Database unavailable
6. Long-running transactions

## Diagnosis
1. Check pool active, idle, and waiting connection counts.
2. Verify database connectivity.
3. Review transaction duration.
4. Check whether connections are always closed.
5. Inspect recent credential or environment changes.

## Recommended Fixes
Use try-with-resources:

```java
try (Connection conn = dataSource.getConnection()) {
    // database work
}
```

Set:
- connection timeout
- idle timeout
- max lifetime
- maximum pool size

## Verification
- Waiting connection count approaches zero.
- API errors stop.
- Connections are returned to the pool.
- Database load remains stable.

## Related Documents
- SQL Connection Pool
- API Timeout
- Incident Triage Playbook
