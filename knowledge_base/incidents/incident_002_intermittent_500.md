# Incident 002 - Intermittent HTTP 500 Errors

## Summary
The customer profile API returned HTTP 500 for users without a secondary address.

## Symptoms
- Intermittent 500 responses
- `NullPointerException`
- Only some users affected

## Investigation
The failing code was:

```java
String city = customer.getSecondaryAddress().getCity();
```

Some customer records had no secondary address.

## Root Cause
The application assumed `secondaryAddress` was always present.

## Resolution
Added null-safe handling and unit tests.

## Prevention
Add validation for optional fields and test incomplete customer profiles.

## Related Documents
- Java NullPointerException
- Java Exception Handling
- API Error Handling
