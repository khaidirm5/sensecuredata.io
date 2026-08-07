# ETL Overview

## Overview

The ETL process is used to handle sales data imported from uploaded files.

The current workflow takes an uploaded dataset through validation and security processing before transforming the data and loading the resulting records into PostgreSQL.

The ETL process is part of the backend and is connected to the upload history and sales data models.

---

## ETL Flow

The current data flow can be represented as:

```text
CSV / Excel File
       │
       ▼
    Upload
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

The processing stages are kept separate so that validation, transformation, and database operations do not have to be handled in one place.

---

## Extract

The extract stage starts when a user uploads a supported dataset.

The uploaded file contains the source data that will be processed by the backend.

The upload is recorded in the upload history so the application can keep track of the dataset being processed.

---

## Validation

Before the data is loaded into the database, the input is checked against the requirements of the application.

Validation is intended to prevent invalid input from continuing through the processing pipeline.

Validation documentation:

```text
docs/etl/validation.md
```

---

## Security Processing

Uploaded files pass through the application's security processing before continuing to the ETL stage.

Security scan results are stored separately and associated with the upload.

The security-related implementation is documented in:

```text
docs/security/security-center.md
```

---

## Transformation

The transformation stage prepares the validated input so it can be stored in the application's sales data structure.

This stage is responsible for converting the source dataset into the format expected by the backend.

Transformation documentation:

```text
docs/etl/transformation.md
```

---

## Loading

After the data has passed validation and transformation, the resulting records can be inserted into PostgreSQL.

Sales records are stored in:

```text
sales_data
```

The loading stage is documented in:

```text
docs/etl/loading.md
```

---

## Upload History

Upload history is used to keep information about uploaded datasets and their processing.

The related model is:

```text
backend/app/models/upload_history.py
```

Sales records can reference the upload that produced them.

This provides a connection between the source dataset and the resulting records in the database.

---

## Current Implementation

The current ETL-related structure includes:

- File upload processing
- Input validation
- Security scan processing
- Data transformation
- Loading sales data into PostgreSQL
- Upload history

The ETL process is currently part of the main FastAPI application and uses the application's PostgreSQL database.

---

## Related Documentation

```text
docs/etl/validation.md
docs/etl/transformation.md
docs/etl/loading.md
docs/security/security-center.md
docs/database/schema.md
```