# Java Thread Pool Troubleshooting

## Overview
Thread pools limit how many tasks execute concurrently. If the pool is undersized, blocked, or exhausted, application latency can increase sharply.

## Common Symptoms
- API requests wait several seconds before processing
- CPU utilization is low but latency is high
- Thread queue length keeps increasing
- Timeouts occur during peak traffic
- Thread dump shows many blocked or waiting threads

## Common Causes
1. Pool size is too small for request volume.
2. Threads block on database or network calls.
3. Tasks never complete because of deadlocks.
4. Queue is unbounded.
5. Slow downstream dependencies consume worker threads.

## Diagnosis
1. Check active thread count and queue length.
2. Capture a thread dump.
3. Identify blocked threads.
4. Measure downstream call latency.
5. Compare peak traffic to configured pool size.

## Recommended Fixes
- Use reasonable maximum pool size.
- Add timeouts to downstream calls.
- Use asynchronous I/O where appropriate.
- Configure bounded queues.
- Separate CPU-heavy and I/O-heavy workloads.

## Verification
- Queue length returns to normal.
- API latency decreases.
- Timeout count drops.
- Thread utilization is stable.

## Related Documents
- API High Latency
- API Timeout
- Service Health Check
