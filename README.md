# Sentinel Secure Data Intelligence Platform

Sentinel Secure Data Intelligence Platform is a full-stack application for secure sales data management, ETL processing, and analytics.

The project is built as a modular monolith using React and Vite on the frontend, FastAPI on the backend, and PostgreSQL as the primary database.

The project is currently under development and is intended to demonstrate practical backend engineering, frontend development, database design, API development, ETL processing, security, and software engineering practices.

---

## Features

### Authentication & Authorization

- JWT Authentication
- Access Token & Refresh Token
- Password Hashing
- Token Revocation
- Role-Based Access Control
- Protected API Endpoints
- Current User Endpoint

### Sales Management

- Sales Data Management
- Pagination
- Search
- Filtering
- Sorting

### ETL Pipeline

- CSV Upload
- File Validation
- Data Validation
- Data Transformation
- Data Loading
- Duplicate Detection
- Upload History

Excel upload support is part of the project scope, while the current implementation should be verified against the backend before being considered complete.

### Security Center

- File Validation
- Security Processing
- Security Scan
- Upload History
- Scan History
- Security Scan Database Records

### API

- REST API
- OpenAPI Specification
- Swagger UI
- ReDoc

### AI

AI-related modules are part of the project structure and documentation, but the AI features are still under development and should not be considered production-ready.

---

## Technology Stack

| Category | Technologies |
|---|---|
| Backend | FastAPI, SQLAlchemy, PostgreSQL, Alembic, Pydantic |
| Authentication | JWT, Password Hashing |
| Frontend | React, Vite, React Router, Axios |
| UI | Recharts, Lucide React, Sonner |
| Development | Git, GitHub, Ruff, Prettier |

---

## Architecture

The current application follows a modular monolith architecture.

```text
Web Browser
     ↓
React + Vite
     ↓
FastAPI
     ↓
Application Layers
     ↓
PostgreSQL
```

The backend is organized into separate modules and layers for API handling, services, repositories, models, schemas, security, database access, middleware, utilities, and AI-related functionality.

Microservices are a future direction and are not part of the current deployment architecture.

---

## Project Structure

```text
sensecuredata.io/
│
├── backend/
│   ├── alembic/
│   ├── app/
│   │   ├── ai/
│   │   ├── api/
│   │   ├── config/
│   │   ├── core/
│   │   ├── db/
│   │   ├── middleware/
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── schemas/
│   │   ├── security/
│   │   ├── services/
│   │   └── utils/
│   ├── scripts/
│   └── tests/
│
├── frontend/
│   ├── public/
│   └── src/
│       ├── assets/
│       ├── components/
│       ├── contexts/
│       ├── hooks/
│       ├── layouts/
│       ├── pages/
│       ├── routes/
│       ├── services/
│       ├── styles/
│       ├── types/
│       └── utils/
│
├── database/
│
├── docs/
│   ├── ai/
│   ├── api/
│   ├── architecture/
│   ├── database/
│   ├── deployment/
│   ├── development/
│   ├── etl/
│   ├── frontend/
│   ├── images/
│   └── security/
│
├── README.md
└── LICENSE
```

---

## Frontend

The frontend is built with React and Vite.

The current frontend structure separates pages, routes, layouts, reusable components, services, hooks, contexts, utilities, types, assets, and styling.

The current routing configuration defines the following paths:

```text
/
/login
/dashboard
/sales
/upload
/security
*
```

The current routes use placeholder components while the frontend is still being developed.

The currently implemented shared layout component is:

```text
frontend/src/components/layout/MainLayout.jsx
```

The frontend does not currently have a verified centralized state management implementation.

More details are available in:

```text
docs/frontend/
├── project-structure.md
├── routing.md
└── ui-components.md
```

---

## Backend

The backend is built with FastAPI and follows a modular layered structure.

```text
backend/app/
├── ai/
├── api/
├── config/
├── core/
├── db/
├── middleware/
├── models/
├── repositories/
├── schemas/
├── security/
├── services/
└── utils/
```

The backend uses PostgreSQL as its primary database and Alembic for database migrations.

---

## Database

PostgreSQL is used as the main application database.

Current database models include:

- `users`
- `upload_history`
- `sales_data`
- `security_scans`
- `revoked_tokens`

Database migrations are managed using Alembic.

Database documentation is available under:

```text
docs/database/
├── erd.md
├── indexing.md
├── migrations.md
└── schema.md
```

---

## ETL Pipeline

The current ETL flow is organized as:

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

Upload history is used to track uploaded datasets, while sales data and security scans can be associated with an upload.

Detailed ETL documentation is available under:

```text
docs/etl/
├── overview.md
├── validation.md
├── transformation.md
└── loading.md
```

---

## Getting Started

### Clone Repository

```bash
git clone git@github.com:khaidirm5/sensecuredata.io.git

cd sensecuredata.io
```

---

## Backend Setup

Create a virtual environment:

```bash
cd backend

python3 -m venv venv
```

Activate the environment.

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create an environment file with the required application settings.

Example:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/sensecuredata

SECRET_KEY=your-secret-key

ACCESS_TOKEN_EXPIRE_MINUTES=30

REFRESH_TOKEN_EXPIRE_DAYS=7
```

Run database migrations:

```bash
alembic upgrade head
```

Start the backend server:

```bash
uvicorn app.main:app --reload
```

Backend URL:

```text
http://localhost:8000
```

---

## Frontend Setup

From the project root:

```bash
cd frontend

npm install

npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

## API Documentation

When the backend is running, API documentation is available through:

Swagger UI:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

---

## Documentation

Project documentation is organized inside the `docs/` directory.

```text
docs/
├── ai/
├── api/
├── architecture/
├── database/
├── deployment/
├── development/
├── etl/
├── frontend/
├── images/
└── security/
```

Documentation covers:

- System Architecture
- Backend Architecture
- Frontend Architecture
- API
- Database Design
- ETL Pipeline
- Security
- Deployment
- Development Workflow
- AI-related Features
- Frontend Structure and Routing

Documentation is maintained alongside the project and is updated as implementation progresses.

---

## Development Status

Current phase:

**Phase 11 — Frontend Development**

### Completed

- Project Foundation
- Authentication & Authorization Backend
- Dashboard Backend
- Sales Management Backend
- ETL Documentation
- Security Center Backend
- Upload History
- Database Documentation
- Architecture Documentation
- API Documentation
- Backend Documentation
- Frontend Project Structure Documentation
- Frontend Routing Documentation
- Frontend UI Components Documentation

### In Progress

- Frontend Development
- Frontend Page Implementation
- Frontend and Backend Integration

### Planned

- Business Intelligence Dashboard
- Reporting
- Audit Log
- Performance Optimization
- Additional API Security
- Testing & Quality Assurance
- Docker & CI/CD
- AI Analytics
- Production Deployment
- Microservices Architecture

The planned items are not considered implemented features.

---

## Security

The current security implementation includes:

- JWT authentication
- Refresh tokens
- Password hashing
- Token validation
- Token revocation
- Role-based access control
- Backend input validation
- Upload validation
- Security scanning

The following features are currently not implemented and should not be considered active security mechanisms:

- Rate limiting
- Response caching
- Redis
- Secure HTTP headers

These may be introduced as part of future development.

---

## Design Principles

The project follows several software engineering principles:

- RESTful API Design
- Repository Pattern
- Service Layer Pattern
- Dependency Injection
- Modular Architecture
- Separation of Concerns
- Database Migration with Alembic
- Layered Backend Structure

The architecture is kept modular while remaining a single FastAPI application.

---

## Code Quality

Development standards include:

- Ruff
- Type Hints
- Modular Project Structure
- Layered Architecture
- Consistent Code Style
- Prettier for frontend formatting

---

## License

This project is licensed under the **Apache License 2.0**.

You may use, modify, and distribute this software in accordance with the Apache License 2.0.

See the `LICENSE` file for the complete license text.