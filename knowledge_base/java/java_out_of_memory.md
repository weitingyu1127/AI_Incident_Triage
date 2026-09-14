# Java OutOfMemoryError Troubleshooting

## Overview
`OutOfMemoryError` occurs when the JVM cannot allocate enough memory for an operation. It may be caused by a true memory leak, oversized data processing, excessive caching, or insufficient heap configuration.

## Common Symptoms
- Service crashes or restarts
- `java.lang.OutOfMemoryError: Java heap space`
- Very high garbage collection activity
- Increasing heap usage over time
- Requests slow down before failure

## Common Causes
1. Objects remain referenced and cannot be garbage collected.
2. Large files or query results are loaded entirely into memory.
3. Cache grows without limits.
4. JVM heap is configured too small.
5. Too many concurrent requests allocate large objects.

## Diagnosis

### Step 1: Check JVM Memory Metrics
Review heap usage, GC frequency, and memory growth.

### Step 2: Capture a Heap Dump
Enable heap dump generation on OOM and inspect it with a profiler.

### Step 3: Identify Large Object Groups
Look for collections or caches holding unexpectedly large numbers of objects.

### Step 4: Review Recent Code Changes
Focus on newly introduced caching, file processing, or batch operations.

## Recommended Fixes
- Stream large files instead of loading them fully.
- Add bounded cache policies.
- Release references when no longer needed.
- Reduce batch size.
- Increase heap only after confirming memory usage is legitimate.

## Verification
1. Run a load test.
2. Confirm heap stabilizes.
3. Confirm GC time remains within acceptable limits.
4. Verify service no longer crashes.

## Related Documents
- Java Thread Pool
- Logging Best Practices
- Incident Triage Playbook
