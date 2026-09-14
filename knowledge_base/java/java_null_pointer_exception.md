# Java NullPointerException Troubleshooting

## Overview
`NullPointerException` occurs when Java code attempts to use an object reference whose value is `null`. Common examples include calling a method, accessing a field, or reading an array element through a null reference.

## Common Symptoms
- HTTP 500 errors in a Java service
- Stack trace contains `java.lang.NullPointerException`
- Failure occurs only for some requests
- A field expected from a database or API is missing
- New code path fails after deployment

## Common Causes
1. Method returns `null` unexpectedly.
2. Database query returns no matching row.
3. External API response omits a field.
4. Object dependency was not initialized.
5. Optional values are treated as mandatory.
6. Incorrect assumptions about collection contents.

## Diagnosis

### Step 1: Read the Stack Trace
Locate the first application-owned class and line number in the stack trace.

### Step 2: Identify the Null Reference
Inspect every object dereferenced on that line.

Example:

```java
String city = customer.getAddress().getCity();
```

Possible null values:
- `customer`
- `customer.getAddress()`

### Step 3: Check Input Data
Validate the request payload, database record, and external API response involved in the failed request.

### Step 4: Reproduce the Failure
Create a test using the same missing or null data.

## Recommended Fixes

### Validate Required Data
```java
Objects.requireNonNull(customer, "customer must not be null");
```

### Use Defensive Checks
```java
if (customer.getAddress() != null) {
    return customer.getAddress().getCity();
}
```

### Use Optional Carefully
```java
Optional.ofNullable(customer.getAddress())
        .map(Address::getCity)
        .orElse("UNKNOWN");
```

## Verification
1. Add a unit test for the failing scenario.
2. Re-run the request.
3. Confirm HTTP 500 no longer occurs.
4. Check logs for repeated exceptions.

## Related Documents
- Java Exception Handling
- API Error Handling
- Logging Best Practices
