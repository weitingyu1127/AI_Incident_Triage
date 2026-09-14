# Incident Triage Playbook

## Overview
This playbook provides a standard sequence for responding to production incidents.

## Step 1: Confirm Impact
Determine:
- affected users
- affected service
- start time
- severity
- error rate
- latency

## Step 2: Check Recent Changes
Review:
- deployments
- configuration changes
- schema changes
- dependency changes

## Step 3: Review Observability
Check:
- logs
- metrics
- traces
- health checks

## Step 4: Identify the Slow or Failing Component
Break the request into:
- application
- database
- downstream API
- network

## Step 5: Compare Similar Incidents
Search previous incidents for matching symptoms or error types.

## Step 6: Mitigate
Possible mitigations:
- rollback
- restart
- disable feature
- reduce traffic
- scale service
- fail over

## Step 7: Verify Recovery
Confirm:
- error rate returns to normal
- latency recovers
- health checks pass

## Step 8: Document Root Cause
Record cause, resolution, and prevention actions.

## Related Documents
- Logging Best Practices
- Service Health Check
- API High Latency
