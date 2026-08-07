# Dashboard API

## Overview

The Dashboard API provides aggregated data used by the dashboard interface.

The dashboard is intended to present an overview of the data stored and processed by the application without requiring the frontend to perform database queries directly.

The frontend communicates with the FastAPI backend through HTTP requests.

---

## Request Flow

```text
Dashboard Page
      │
      ▼
Frontend Service
      │
      ▼
Dashboard API
      │
      ▼
Service Layer
      │
      ▼
Repository / Database Query
      │
      ▼
PostgreSQL
```

The backend handles the data aggregation before returning the result to the frontend.

---

## Dashboard Data

Dashboard responses can be used to display application statistics and sales-related information.

The data source is the PostgreSQL database populated through the application's normal data and upload workflows.

The exact metrics returned by the API should follow the implementation in the backend rather than being duplicated in the frontend.

---

## Sales Aggregation

Sales data can be aggregated for dashboard purposes.

Possible query dimensions used by the current data model include:

- Order date
- Category
- Region
- Sales records

The database already contains indexes supporting common sales dashboard queries, including:

```text
(order_date, category)
(order_date, region)
```

These indexes are documented in:

```text
docs/database/indexing.md
```

---

## API Responsibility

The Dashboard API is responsible for:

- Receiving dashboard requests
- Validating request parameters
- Retrieving the required data
- Performing or coordinating aggregation
- Returning structured API responses

The frontend is responsible for presenting the returned data.

---

## Frontend Integration

The dashboard frontend uses the backend API rather than accessing PostgreSQL directly.

A simplified flow is:

```text
React Dashboard
      │
      ▼
Axios / Frontend Service
      │
      ▼
FastAPI Dashboard Endpoint
      │
      ▼
Database
```

The resulting data can then be displayed through tables, summary information, or charts.

---

## Authentication

Dashboard endpoints that expose protected application data should require an authenticated user.

The authentication mechanism is based on JWT.

Authentication details are documented in:

```text
docs/api/authentication.md
```

Authorization rules are documented in:

```text
docs/security/authorization-rbac.md
```

---

## Response Handling

The API should return structured JSON responses that can be consumed by the React frontend.

The response format should remain consistent with the backend schemas and frontend service expectations.

Frontend components should not depend on database-specific structures.

---

## Performance

Dashboard queries can involve aggregation across sales records.

Database indexes are used to support common filtering and grouping operations.

If dashboard queries become more complex or expensive, performance should be evaluated using actual query behavior before introducing additional caching or infrastructure.

---

## Current State

The dashboard API is part of the current backend architecture.

The frontend has a dedicated dashboard area for displaying application and sales information.

Dashboard functionality will continue to evolve as additional analytics and data processing features are implemented.