# Microservices Roadmap

## Overview

Sentinel Secure Data Intelligence Platform currently uses a modular monolith architecture.

The backend modules are separated by responsibility inside a single FastAPI application. They share the same application runtime and PostgreSQL database.

Microservices are not currently deployed.

---

## Current Architecture

The current backend structure is organized into separate modules:

```text
FastAPI Application
├── API
├── Services
├── Repositories
├── Security
├── Database
├── Middleware
├── AI
└── Utilities
```

This approach keeps the system easier to develop and maintain while the main features are still being built.

---

## Why Microservices Are Not Used Yet

The current project does not require independent services.

Introducing microservices too early would add additional infrastructure and operational requirements, including:

- Service-to-service communication
- Independent deployments
- Service discovery
- Centralized logging
- Monitoring
- Network security
- Distributed failure handling

For the current stage, keeping the modules inside one FastAPI application is more practical.

---

## Potential Service Boundaries

If the application grows significantly, some backend modules could be separated into independent services.

Potential candidates include:

### Authentication Service

Responsible for:

- User authentication
- Token management
- Role and permission handling

### Data Service

Responsible for:

- Sales data
- Dataset management
- Data processing

### Security Service

Responsible for:

- File security checks
- Validation
- Security-related processing

### Analytics Service

Responsible for:

- Dashboard aggregation
- Analytics processing
- Reporting

### AI Service

Responsible for:

- AI-related processing
- Forecasting
- Anomaly detection
- Recommendation features

These are potential future boundaries and are not currently deployed as independent services.

---

## Possible Future Structure

A future architecture could look like:

```text
Client
   |
   v
API Gateway
   |
   +--------------------+
   |         |          |
   v         v          v
 Auth      Data      Security
Service   Service     Service
   |         |          |
   +---------+----------+
             |
             v
       Shared Platform
```

The final architecture would depend on the application's requirements and operational needs at that time.

---

## Migration Strategy

If the project eventually moves toward microservices, the transition should be incremental.

A possible migration sequence is:

1. Stabilize the current modular monolith.
2. Define clear boundaries between modules.
3. Add automated tests around each module.
4. Define stable API contracts.
5. Identify modules that require independent scaling.
6. Extract one module at a time.
7. Introduce service-to-service authentication.
8. Add centralized logging and monitoring.
9. Review database ownership and data access.
10. Deploy services independently.

The application should not be converted into microservices simply for architectural complexity. The change should be driven by an actual technical requirement.

---

## Database Considerations

The current application uses PostgreSQL as the primary database.

A future microservices architecture may require clearer ownership of database tables or separate databases for individual services.

This should only be introduced after the service boundaries are stable.

---

## Deployment Considerations

A microservices deployment would require additional infrastructure compared with the current application.

Potential components could include:

- Containerized services
- API gateway
- Service networking
- Centralized logging
- Monitoring
- Health checks
- Independent deployment pipelines

These components are part of the future architecture and are not currently required by the application.

---

## Current Status

The project currently remains a modular monolith.

No independent backend microservices are deployed.

The existing module structure provides a foundation for future separation if the application's scale or operational requirements make it necessary.