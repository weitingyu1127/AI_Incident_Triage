# Incident 003 - Service Crash Due to OutOfMemoryError

## Summary
A reporting service restarted repeatedly while generating a large export.

## Symptoms
- JVM restart
- `OutOfMemoryError: Java heap space`
- Heap usage reached 100%

## Investigation
The export loaded 2.5 million records into an in-memory list before writing the file.

## Root Cause
Unbounded in-memory processing of a very large dataset.

## Resolution
Changed the export process to stream database results in batches.

## Prevention
Use bounded batch processing and load-test large exports.

## Related Documents
- Java OutOfMemoryError
- SQL Query Optimization
