# Input Validation

## Overview

Input validation is used to make sure data received by the backend matches the format and rules expected by the application.

Validation is performed before data is processed or stored in PostgreSQL.

The backend uses Pydantic schemas together with application-level validation.

---

## Request Flow

```text
Client Request
      │
      ▼
FastAPI Endpoint
      │
      ▼
Pydantic Validation
      │
      ├── Invalid
      │     │
      │     ▼
      │   Reject Request
      │
      └── Valid
            │
            ▼
        Service Layer
            │
            ▼
        Repository
            │
            ▼
        PostgreSQL
```

---

## Request Schemas

Request and response schemas are maintained under:

```text
backend/app/schemas/
```

Pydantic is used to validate incoming API data before it reaches the application logic.

This keeps validation rules separate from the database models.

---

## API Input

API endpoints should validate incoming values before passing them to the service layer.

Validation can cover things such as:

- Required fields
- Data types
- Expected formats
- Allowed values
- Field lengths
- Request structure

Invalid input should be rejected before it reaches database operations.

---

## File Input

File uploads require additional validation because uploaded files are processed by the application.

The upload workflow includes validation before the file continues to the processing stage.

A simplified flow is:

```text
Uploaded File
      │
      ▼
File Validation
      │
      ├── Invalid → Reject
      │
      └── Valid
            │
            ▼
       Security Processing
            │
            ▼
          ETL
```

File-related validation is part of the application's security and ETL workflow.

---

## Data Validation

Data imported from CSV or Excel files should also be validated before being inserted into the sales tables.

The purpose is to prevent malformed data from entering the database and causing problems later during queries or analysis.

The ETL validation process is documented under:

```text
docs/etl/validation.md
```

---

## Database Constraints

Application-level validation is not the only validation layer.

PostgreSQL also enforces database constraints where they are defined.

Examples in the current schema include:

- Unique email
- Unique username
- Unique revoked token identifier
- Foreign key relationships
- Sales-related uniqueness constraints

This provides an additional layer of data integrity.

---

## Error Handling

Invalid input should result in a controlled API response.

The backend should return validation errors without exposing internal implementation details.

Sensitive information such as:

- Database credentials
- Internal filesystem paths
- SQL statements
- Authentication secrets

should not be included in validation responses.

---

## Validation and Security

Input validation is one part of the application's security controls.

It works together with:

- Authentication
- Authorization
- File validation
- Security scanning
- Database constraints
- API security controls

Validation does not replace authentication or authorization.

---

## Current State

The backend already uses Pydantic schemas for request and response validation.

File and dataset validation are also part of the upload and ETL workflow.

As new API endpoints and data-processing features are added, their input validation rules should be implemented alongside the corresponding schemas and business logic.