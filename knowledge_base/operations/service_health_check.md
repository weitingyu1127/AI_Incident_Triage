# Service Health Check Guide

## Overview
Health checks help determine whether a service and its dependencies are functioning.

## Typical Endpoints
- `/health`
- `/ready`
- `/live`

## Liveness
Confirms the process is running.

## Readiness
Confirms the service can accept traffic.

## Dependency Checks
Readiness may include:
- database connectivity
- message queue connectivity
- critical downstream services

## Warning
Do not make liveness checks depend on every external service, because temporary dependency failures may cause restart loops.

## Related Documents
- API Timeout
- SQL Connection Pool
- Incident Triage Playbook
