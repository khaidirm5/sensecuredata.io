# Database Schema

## Overview

Sentinel Secure Data Intelligence Platform uses PostgreSQL as its primary relational database.

The database schema is represented in the SQLAlchemy models located under:

```text
backend/app/models/
```

The current models cover users, sales data, upload history, security scans, and revoked authentication tokens.

Database schema changes are managed through Alembic.

---

## Current Models

The current database models are:

```text
backend/app/models/
├── user.py
├── sales_data.py
├── upload_history.py
├── security_scan.py
└── revoked_token.py
```

Each model represents a database table used by the backend application.

---

## Users

The user model is defined in:

```text
backend/app/models/user.py
```

The table stores application user information.

The model defines unique constraints for:

```text
email
username
```

This prevents multiple users from being created with the same email address or username.

---

## Sales Data

The sales model is defined in:

```text
backend/app/models/sales_data.py
```

The table stores sales records used by the application.

The model contains indexes for fields used by sales-related queries, including:

```text
invoice_number
category
order_date
region
upload_id
```

It also contains composite indexes involving:

```text
order_date + category
order_date + region
```

The sales table is associated with upload history through its upload reference.

---

## Upload History

The upload history model is defined in:

```text
backend/app/models/upload_history.py
```

The table stores information about uploaded datasets and their processing history.

Each upload is associated with a user.

Upload history is also used as a reference for related sales records and security scan results.

---

## Security Scans

The security scan model is defined in:

```text
backend/app/models/security_scan.py
```

The table stores the results of security checks performed against uploaded files.

Security scan records are associated with an upload through the upload reference.

The model also contains an indexed field used for scan-related lookups.

---

## Revoked Tokens

The revoked token model is defined in:

```text
backend/app/models/revoked_token.py
```

The table stores revoked authentication token identifiers.

The token identifier (`jti`) is unique and indexed so that the application can efficiently check whether a token has been revoked.

The current model does not define a foreign key relationship between revoked tokens and the users table.

---

## Relationships

The current model relationships can be summarized as:

```text
users
  │
  └── upload_history
          │
          ├── sales_data
          │
          └── security_scans

revoked_tokens
```

The relationships currently defined by the models are:

| Parent | Child | Relationship |
|---|---|---|
| `users` | `upload_history` | One-to-many |
| `upload_history` | `sales_data` | One-to-many |
| `upload_history` | `security_scans` | One-to-many |

`revoked_tokens` currently has no direct foreign key relationship to another table.

---

## Constraints

The database uses constraints to maintain data integrity.

Current model-level constraints include:

- Unique `users.email`
- Unique `users.username`
- Unique `revoked_tokens.jti`
- Sales-related `UniqueConstraint`
- Foreign key relationships between related records

The exact constraint definitions are maintained in the SQLAlchemy models and Alembic migrations.

---

## Indexes

Indexes are defined for fields that are used frequently by application queries.

Sales-related indexes include:

```text
idx_sales_invoice
idx_sales_category
idx_sales_order_date
idx_sales_region
idx_sales_upload
idx_sales_date_category
idx_sales_date_region
```

Additional indexes are defined for authentication, upload history, and security scan lookups.

Detailed indexing information is documented in:

```text
docs/database/indexing.md
```

---

## Schema Changes

Database schema changes are managed through Alembic.

Migration files are stored in:

```text
backend/alembic/versions/
```

The migration history includes changes for:

- Initial table creation
- Authentication-related tables
- Sales data
- Upload history
- Security scans
- Revoked tokens
- Index creation
- Index cleanup
- Composite sales indexes

More information about the migration workflow is available in:

```text
docs/database/migrations.md
```

---

## Current State

The current schema supports the application's main data and authentication requirements.

The database structure is expected to evolve as additional application features are implemented.

Changes to the SQLAlchemy models should be accompanied by the appropriate Alembic migration so the application model and database schema remain consistent.