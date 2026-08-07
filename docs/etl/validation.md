# ETL Validation

## Overview

Validation is the first data-processing stage after a dataset is uploaded.

The purpose is to make sure the incoming data can be processed safely and matches the structure expected by the application before it reaches the transformation and loading stages.

---

## Validation Flow

```text
Uploaded File
      │
      ▼
File Validation
      │
      ▼
Data Validation
      │
      ├── Invalid
      │     │
      │     ▼
      │   Reject
      │
      └── Valid
            │
            ▼
       Security Scan
            │
            ▼
       Transformation
```

---

## File Validation

The uploaded file is checked before its contents are processed.

Validation is intended to prevent unsupported or invalid input from entering the ETL pipeline.

File-related validation is also part of the application's security controls.

---

## Data Validation

After the file passes the initial checks, the dataset is validated before being transformed.

The validation stage helps ensure that the incoming records contain the information required by the sales data structure.

Invalid records should not be inserted directly into PostgreSQL.

---

## Validation and Security

Validation and security scanning have different responsibilities.

Validation checks whether the input is acceptable for processing.

Security scanning handles security-related checks for uploaded files.

The workflow therefore keeps both stages separate:

```text
Upload
  │
  ▼
Validation
  │
  ▼
Security Scan
  │
  ▼
ETL
```

Security Center documentation:

```text
docs/security/security-center.md
```

---

## Validation and Database

Validation takes place before data is loaded into PostgreSQL.

The final data is stored in the sales data table:

```text
sales_data
```

Database constraints provide an additional layer of data integrity after the application-level validation.

---

## Invalid Data

When uploaded data does not satisfy the required validation rules, processing should stop instead of continuing to the loading stage.

The application should return a controlled error to the client so the user can correct the source data and upload it again.

---

## Current State

The validation stage is part of the current upload and ETL workflow.

It works together with:

- File validation
- Security processing
- Data transformation
- Database loading
- Upload history

Detailed validation rules should be updated together with the implementation whenever the accepted upload format or sales data structure changes.