# Authorization & RBAC

## Overview

Authentication identifies the user making a request, while authorization determines whether that user is allowed to access a particular resource or perform an action.

Sentinel Secure Data Intelligence Platform uses role-based access control (RBAC) for authorization.

The current roles are:

- `admin`
- `analyst`
- `user`

---

## Role-Based Access

Access to protected functionality is determined by the authenticated user's role.

The general flow is:

```text
Request
   │
   ▼
JWT Validation
   │
   ▼
Authenticated User
   │
   ▼
Role Check
   │
   ├── Allowed
   │     │
   │     ▼
   │   Endpoint
   │
   └── Not Allowed
         │
         ▼
       Reject
```

Authentication must succeed before the authorization check can be performed.

---

## Roles

### Admin

The `admin` role is intended for users who require elevated access to application functionality.

Administrative permissions should only be assigned where they are actually required.

### Analyst

The `analyst` role is intended for users who work with application data and analytical functionality.

The exact permissions depend on the endpoint being accessed.

### User

The `user` role represents a standard application user.

Access is limited to functionality available to normal users.

---

## Authorization Checks

Role checks are performed by the backend rather than relying on the frontend.

The frontend can hide or disable interface elements based on the user's role, but this is not considered an authorization boundary.

The backend must perform the actual permission check before allowing a protected operation.

---

## Protected Endpoints

A protected endpoint generally follows this sequence:

```text
HTTP Request
      │
      ▼
Authentication
      │
      ▼
Current User
      │
      ▼
Role / Permission Check
      │
      ▼
Business Logic
```

If the user does not have the required role, the request should be rejected before the protected operation is executed.

---

## Authentication vs Authorization

These two checks have different purposes.

| Security Layer | Purpose |
|---|---|
| Authentication | Verifies who the user is |
| Authorization | Determines what the user can access |

For example, a valid JWT confirms that the request belongs to an authenticated user. It does not automatically mean that the user can access every endpoint.

---

## Frontend Considerations

The React frontend may use the authenticated user's role to control the interface.

For example, navigation items or actions that are not available to a role can be hidden from the user interface.

However, frontend checks are only for the user experience.

The backend remains responsible for enforcing authorization.

---

## Unauthorized Access

When an authenticated user does not have permission to access a resource, the backend should return an appropriate authorization error.

The response should not expose internal authorization rules or sensitive implementation details.

---

## Current State

The application currently has role-based authorization with the following roles:

```text
admin
analyst
user
```

Authorization is part of the backend security layer and works together with JWT authentication.

As more application features are added, individual endpoint permissions can be refined according to their actual access requirements.