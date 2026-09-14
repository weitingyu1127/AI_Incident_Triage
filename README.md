# AI Incident Copilot - Phase 1 Knowledge Base

This package contains a small synthetic technical knowledge base for building a first RAG prototype.

## Contents

- 5 Java troubleshooting documents
- 6 SQL/database documents
- 6 API documents
- 3 operations documents
- 10 historical incident reports

Total: 30 Markdown knowledge documents

## Suggested Phase 1 Architecture

```text
Markdown Documents
      ↓
Chunking
      ↓
Embeddings
      ↓
PostgreSQL + pgvector
      ↓
Semantic Retrieval
      ↓
LLM
      ↓
Answer + Source Citations
```

## Recommended First Test Questions

1. Why did the orders API become slow after the table grew to one million rows?
2. What should I check when I see SQLTimeoutException?
3. Why can a Java service return intermittent HTTP 500 errors only for some users?
4. How should I respond to HTTP 429 from a third-party API?
5. What can cause a database connection pool to become exhausted?
6. How can retries create duplicate orders?
7. Why would API latency be high even when CPU utilization is low?
8. How should I investigate a 504 Gateway Timeout?
9. What is the difference between a liveness and readiness check?
10. Which past incident is most similar to a missing database index problem?

## Suggested Metadata

When ingesting each document, consider storing:

- `source_file`
- `category`
- `document_type`
- `title`

Example:

```json
{
  "source_file": "sql_slow_query.md",
  "category": "database",
  "document_type": "technical_doc",
  "title": "SQL Slow Query Troubleshooting"
}
```

For incidents:

```json
{
  "source_file": "incident_001_orders_api_latency.md",
  "category": "incident",
  "document_type": "past_incident",
  "title": "Incident 001 - Orders API High Latency"
}
```

## Scope

The content is synthetic and intended for learning and portfolio development. It should not be treated as production operational guidance without review.
