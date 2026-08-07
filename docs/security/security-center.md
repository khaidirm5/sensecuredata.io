# Security Center

## Overview

Security Center handles security checks for files uploaded to the application.

The feature is connected to the upload workflow and stores security scan results in PostgreSQL.

The related model is located at:

```text
backend/app/models/security_scan.py
```

## Upload Security Flow

The current upload flow includes validation and security processing before the data continues to the ETL stage.

```text
File Upload
     │
     ▼
Input Validation
     │
     ▼
Security Scan
     │
     ├── Rejected
     │
     └── Passed
            │
            ▼
        ETL Processing
            │
            ▼
        Sales Data
```

## Security Scan Records

Security scan results are stored in the database using the `SecurityScan` model.

The model is located at:

```text
backend/app/models/security_scan.py
```

Scan records are associated with uploaded files through the upload reference.

This allows the application to keep the security result connected to the corresponding upload.

## Upload History

Security scanning is part of the upload processing workflow.

The relationship between the main records is:

```text
User
 │
 ▼
Upload History
 │
 └── Security Scan
```

Upload history provides a record of uploaded datasets, while security scan records contain the result of the security processing associated with those uploads.

## Input Validation

Uploaded input is validated before the application continues with further processing.

Validation is handled by the backend and is part of the application's file-processing workflow.

More information about validation is available in:

```text
docs/security/input-validation.md
```

## Database

Security scan information is stored in PostgreSQL.

The corresponding SQLAlchemy model is:

```text
backend/app/models/security_scan.py
```

The security scan table and its database changes are managed through Alembic migrations.

Migration files are located at:

```text
backend/alembic/versions/
```

The current migration history includes the creation of the security scan table.

## API Integration

Security-related functionality is handled by the FastAPI backend.

The backend API is located under:

```text
backend/app/api/
```

The React frontend communicates with the backend through HTTP requests. The frontend does not access PostgreSQL directly.

## Authentication and Authorization

Security-related API operations use the application's existing authentication and authorization mechanisms where required.

Authentication is based on JWT.

Authentication documentation:

```text
docs/security/authentication.md
```

Role-based authorization documentation:

```text
docs/security/authorization-rbac.md
```

## Current Implementation

The current Security Center functionality includes:

- Input validation for uploaded data
- Security scan processing
- Security scan records
- Upload and security scan association
- PostgreSQL storage
- FastAPI integration

Features that have not been implemented, such as rate limiting, response caching, and secure HTTP headers, are not considered part of the current Security Center implementation.