# Incident 008 - Service Unavailable After Deployment

## Summary
A newly deployed service could not start in production.

## Symptoms
- Deployment completed but health check failed
- Database authentication error
- Previous version worked

## Investigation
The new deployment referenced a staging database secret name.

## Root Cause
Incorrect production environment configuration.

## Resolution
Updated the secret reference and redeployed.

## Prevention
Add environment configuration validation to deployment pipeline.

## Related Documents
- Service Health Check
- Incident Triage Playbook
- Java Database Connection
