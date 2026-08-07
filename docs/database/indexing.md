# Database Indexing

## Overview

Indexes are used in the database to improve lookup and filtering performance.

The current project defines indexes mainly around sales queries, upload history, security scans, and authentication-related lookups.

Index definitions are maintained in the SQLAlchemy models and database migrations.

---

## Sales Data

The `sales_data` model contains the largest set of indexes because sales data is used for filtering, sorting, dashboard queries, and data analysis.

The current indexes are:

| Index | Column(s) |
|---|---|
| `idx_sales_invoice` | `invoice_number` |
| `idx_sales_category` | `category` |
| `idx_sales_order_date` | `order_date` |
| `idx_sales_region` | `region` |
| `idx_sales_upload` | `upload_id` |
| `idx_sales_date_category` | `order_date`, `category` |
| `idx_sales_date_region` | `order_date`, `region` |

The composite indexes are intended for queries that filter or group sales data using both date and category or date and region.

The model also defines a `UniqueConstraint` for the relevant sales fields.

---

## Upload History

The `upload_history` model defines indexes for fields used when accessing upload records.

These indexes support lookups related to uploaded datasets and their associated records.

The exact index definitions are maintained in:

```text
backend/app/models/upload_history.py
```

---

## Users

The `users` model defines unique constraints for:

- `email`
- `username`

These values must be unique across users.

The uniqueness is enforced at the database level through unique constraints.

---

## Revoked Tokens

The `revoked_tokens` model defines a unique indexed value for the token identifier (`jti`).

This allows revoked tokens to be checked efficiently while also preventing duplicate token identifiers.

The related migration creates a unique index for:

```text
jti
```

The migration history also contains a change that removes a redundant index from the table.

---

## Security Scans

The `security_scans` model contains an indexed field used for security scan lookups.

The index definition is maintained in:

```text
backend/app/models/security_scan.py
```

The initial database migration also creates the corresponding table index.

---

## Composite Indexes

The project uses composite indexes for sales queries:

```text
(order_date, category)
(order_date, region)
```

These indexes are useful when queries use the indexed columns together.

They are defined as:

```text
idx_sales_date_category
idx_sales_date_region
```

These indexes were added through the database migration:

```text
backend/alembic/versions/2435fafd8795_add_sales_dashboard_composite_indexes.py
```

---

## Migration Management

Index changes are tracked through Alembic migrations.

Relevant migrations include:

```text
backend/alembic/versions/
├── 2435fafd8795_add_sales_dashboard_composite_indexes.py
├── 3b59e9c6899d_create_revoked_tokens_table.py
├── 3e351e19fe8b_remove_redundant_revoked_tokens_id_index.py
├── 45734c91b4ef_remove_redundant_users_id_index.py
├── 7a100240f40d_create_users_table.py
└── f8cf7e126a1e_create_security_scans_table.py
```

This keeps index changes versioned together with the rest of the database schema.

---

## Indexing Approach

Indexes are added where they support actual application queries.

The project currently focuses indexing on:

- Sales filtering
- Sales sorting
- Sales dashboard queries
- Upload lookups
- Security scan lookups
- User uniqueness
- Revoked token lookups

Indexes should not be added indiscriminately because they also increase storage requirements and can add overhead to write operations.

Any new index should be based on an actual query or performance requirement.

---

## Current State

The current database already contains indexes for the main lookup patterns identified during development.

As the application grows, query performance should be monitored before introducing additional indexes.

Index changes should be made through the SQLAlchemy models and corresponding Alembic migrations rather than by manually modifying the database.