# ETL Transformation

## Overview

The transformation stage prepares validated input data for the application's sales data structure.

The stage sits between validation and loading. Its purpose is to convert the incoming dataset into a format that can be handled consistently by the backend and stored in PostgreSQL.

---

## Transformation Flow

```text
Uploaded Dataset
      │
      ▼
   Validation
      │
      ▼
 Transformation
      │
      ▼
   Prepared Data
      │
      ▼
     Loading
      │
      ▼
 PostgreSQL
```

---

## Source Data

The ETL process accepts sales data from uploaded files.

The uploaded dataset may contain fields that need to be mapped or prepared before they can be stored in the application's sales data structure.

The source file is not treated as the final database representation.

---

## Data Preparation

During transformation, validated input is prepared according to the structure expected by the sales data model.

The transformation stage is responsible for keeping this preparation separate from:

- File validation
- Security processing
- Database operations

This makes the processing flow easier to maintain as the sales dataset structure changes.

---

## Sales Data Structure

The resulting data is intended to match the application's sales data model:

```text
backend/app/models/sales_data.py
```

The transformed records can then be passed to the loading stage.

---

## Validation Before Transformation

Transformation is performed only after the input has passed the validation stage.

```text
Upload
  │
  ▼
Validation
  │
  ├── Invalid → Stop
  │
  └── Valid
       │
       ▼
   Transformation
       │
       ▼
      Loading
```

This prevents the transformation stage from having to handle input that should already have been rejected.

---

## Database Loading

Transformation does not directly represent the database itself.

After the data has been prepared, it continues to the loading stage where the records are stored in PostgreSQL.

Loading documentation:

```text
docs/etl/loading.md
```

---

## Current State

Transformation is part of the ETL workflow used for uploaded sales data.

The current flow is:

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

The transformation rules should be kept consistent with the current `sales_data` model and updated whenever the accepted sales data structure changes.