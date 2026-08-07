# Security Center API

## Overview

The Security Center API handles security-related information associated with uploaded files.

The backend performs validation and security processing before uploaded data continues through the application workflow.

Security-related backend code is separated from the frontend and is handled by FastAPI.

---

## Request Flow

```text
File Upload
     │
     ▼
Validation
     │
     ▼
Security Processing
     │
     ▼
Security Scan Result
     │
     ▼
Upload Processing
```

The frontend only sends the request and displays the result returned by the backend.

---

## Security Scan

Security scan records are stored in PostgreSQL.

The corresponding SQLAlchemy model is:

```text
backend/app/models/security_scan.py
```

A scan record is associated with the related upload through the upload reference.

This makes it possible to connect a security result with the file that was processed.

---

## Upload and Security Processing

Security checks are part of the file processing workflow.

The general flow is:

```text
Uploaded File
      │
      ▼
Input Validation
      │
      ▼
Security Scan
      │
      ├── Rejected
      │
      └── Accepted
             │
             ▼
         ETL Processing
```

A file that does not pass the required checks should not continue to the data processing stage.

---

## Validation

The application performs validation before processing uploaded files.

Validation can include checks related to the uploaded file and the data it contains.

The detailed validation rules are documented in:

```text
docs/security/input-validation.md
```

---

## Upload History

Security processing is connected to the upload history system.

The relationship can be represented as:

```text
Upload History
      │
      └── Security Scan
```

This provides a record of security processing associated with an uploaded dataset.

---

## Authentication

Security Center endpoints that expose protected application information should require an authenticated user.

Authentication uses JWT.

Authentication details are documented in:

```text
docs/api/authentication.md
```

Role-based access control is documented in:

```text
docs/security/authorization-rbac.md
```

---

## Error Handling

Security-related requests should return controlled API responses when processing fails.

The API should avoid exposing internal implementation details, filesystem information, database errors, or other sensitive information in error responses.

---

## Security Response

The frontend can use the API response to show the result of the security processing.

The response should provide enough information for the application interface to indicate whether processing can continue without exposing unnecessary internal security details.

---

## Current State

The Security Center is part of the current backend structure.

The application already contains:

- Security scan model
- Upload-related security processing
- Input validation
- Security-related API functionality

Additional security checks can be added as the file processing workflow develops.

Detailed security documentation is maintained under:

```text
docs/security/
```