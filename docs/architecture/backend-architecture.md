# Backend Architecture

## Overview

The backend of Sentinel Secure Data Intelligence Platform is built with FastAPI.

The backend currently follows a layered structure. API routes, business logic, database access, security components, and shared utilities are separated into different modules.

The application runs as a single FastAPI application.

---

## Backend Structure

The main backend source code is located in:

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

---

## API Layer

The `api` directory contains the HTTP endpoints exposed by the FastAPI application.

This layer is responsible for:

- Receiving HTTP requests
- Validating request data
- Resolving dependencies
- Calling the appropriate application logic
- Returning HTTP responses

API routes should not contain database queries or complex business logic directly.

---

## Service Layer

The `services` directory contains application-level business logic.

Services are responsible for processing operations requested by the API layer and coordinating the required repositories or other application components.

Keeping business logic inside services prevents route handlers from becoming too large and keeps responsibilities separated.

---

## Repository Layer

The `repositories` directory contains database access logic.

Repositories are responsible for operations such as:

- Retrieving records
- Creating records
- Updating records
- Deleting records
- Executing database queries

The repository layer uses SQLAlchemy to communicate with PostgreSQL.

This keeps database access separate from API routes and business logic.

---

## Models

The `models` directory contains SQLAlchemy ORM models.

Models represent the database entities used by the application.

The models define the structure of database records and their relationships.

---

## Schemas

The `schemas` directory contains Pydantic schemas used by the API.

Schemas define the structure of incoming requests and outgoing responses.

They are also used to validate data before it reaches the application logic.

---

## Database

The `db` directory contains database-related configuration and session management.

The backend uses PostgreSQL as its primary database and SQLAlchemy as the ORM.

Database migrations are managed separately through Alembic.

The migration configuration is located at:

```text
backend/alembic/
backend/alembic.ini