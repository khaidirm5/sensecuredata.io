# ETL Loading

## Overview

The loading stage is the final part of the current ETL flow.

After the uploaded sales data has passed validation, security processing, and transformation, the resulting records are prepared for storage in PostgreSQL.

---

## Loading Flow

```text
Uploaded File
      │
      ▼
   Validation
      │
      ▼
 Security Scan
      │
      ▼
 Transformation
      │
      ▼
    Loading
      │
      ▼
 PostgreSQL
      │
      ▼
  sales_data
```

---

## Target Database

The transformed sales records are stored in PostgreSQL.

The corresponding SQLAlchemy model is:

```text
backend/app/models/sales_data.py
```

The database is accessed through the backend rather than directly from the frontend.

---

## Upload Reference

Sales records produced from an uploaded dataset can be associated with the corresponding upload history record.

This provides a link between:

```text
Upload History
      │
      └── Sales Data
```

The relationship allows the application to trace processed sales records back to their source upload.

---

## Database Access

Database operations are handled by the backend's database layer.

The general application structure is:

```text
ETL
 │
 ▼
Service Layer
 │
 ▼
Repository Layer
 │
 ▼
SQLAlchemy
 │
 ▼
PostgreSQL
```

Keeping database operations inside the backend prevents the ETL process from requiring direct database access from the frontend.

---

## Data Integrity

Before records reach the loading stage, the data has already passed the earlier processing steps.

The database also provides its own constraints and indexes to help maintain data integrity and support queries.

Relevant database documentation:

```text
docs/database/schema.md
docs/database/indexing.md
docs/database/migrations.md
```

---

## Upload History

The upload history model is located at:

```text
backend/app/models/upload_history.py
```

Upload history provides information about the dataset being processed and its processing lifecycle.

This makes it possible to relate the loaded sales data to the original upload.

---

## Error Handling

If the loading operation fails, the application should return a controlled error rather than treating the upload as successfully processed.

Database errors should not expose internal database details to the client.

The processing result should remain associated with the corresponding upload history where applicable.

---

## Current State

The loading stage is part of the current ETL structure for uploaded sales data.

The overall process is:

```text
Upload
  ↓
Validation
  ↓
Security Processing
  ↓
Transformation
  ↓
Loading
  ↓
PostgreSQL
```

The loading implementation should remain consistent with the current `sales_data` and `upload_history` models as the database schema evolves.   