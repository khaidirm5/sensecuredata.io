# Sales API

## Overview

The Sales API handles sales data used by the application.

Sales records can be created, retrieved, updated, and deleted through the backend API. Sales data can also originate from uploaded datasets processed by the application's data pipeline.

The API is implemented in FastAPI.

---

## Request Flow

```text
React Frontend
      │
      ▼
Sales Service
      │
      ▼
FastAPI Sales API
      │
      ▼
Service Layer
      │
      ▼
Repository Layer
      │
      ▼
PostgreSQL
```

The frontend does not access the database directly.

---

## Sales Data

Sales records are represented by the SQLAlchemy model:

```text
backend/app/models/sales_data.py
```

The model contains sales-related fields and references the upload that produced the record.

Sales data can therefore be associated with an upload history record.

---

## CRUD Operations

The Sales API supports the normal operations required to manage sales records.

### Create

Creates a new sales record.

### Read

Retrieves sales records from the database.

The API can support filtering and other query parameters used by the application.

### Update

Updates an existing sales record.

### Delete

Deletes a sales record when permitted by the application.

The exact request and response schemas are defined by the backend implementation.

---

## Sales Uploads

Sales data can also be created through file uploads.

The general flow is:

```text
CSV / Excel File
       │
       ▼
File Validation
       │
       ▼
Security Processing
       │
       ▼
ETL Processing
       │
       ▼
Sales Records
       │
       ▼
PostgreSQL
```

Upload-related processing is documented under:

```text
docs/etl/
```

---

## Upload History

Sales records created through an upload can be associated with the corresponding upload history record.

The relationship is represented through the upload reference in the sales model.

This allows the application to trace sales records back to the dataset from which they originated.

---

## Filtering and Queries

Sales data is commonly queried using fields such as:

- Invoice number
- Category
- Order date
- Region
- Upload

The database contains indexes for these fields.

Composite indexes are also available for:

```text
order_date + category
order_date + region
```

The indexing details are documented in:

```text
docs/database/indexing.md
```

---

## Authentication

Sales endpoints that modify or expose protected application data should require an authenticated user.

Authentication uses JWT.

The authentication flow is documented in:

```text
docs/api/authentication.md
```

Access control based on user roles is documented in:

```text
docs/security/authorization-rbac.md
```

---

## Validation

Incoming sales data is validated by the backend before being written to the database.

Validation is handled through the application's request schemas and business logic.

For uploaded datasets, validation also takes place as part of the ETL and file processing workflow.

---

## Error Handling

The API should return appropriate HTTP responses when an operation cannot be completed.

Common cases include:

- Invalid request data
- Record not found
- Unauthorized request
- Forbidden operation
- Database or processing error

Error responses should not expose internal database details or sensitive application information.

---

## Current State

The Sales API is part of the current FastAPI backend.

Sales records are stored in PostgreSQL and can be managed through the API or generated through the upload and ETL workflow.

The API will continue to evolve as additional sales analytics and data management features are added.