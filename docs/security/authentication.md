# Authentication Security

## Overview

Authentication is handled by the FastAPI backend.

The application uses JWT-based authentication to identify users and protect endpoints that require authentication.

Authentication-related code is maintained under the backend security and authentication modules.

---

## Authentication Flow

The current authentication flow is:

```text
User
  │
  ▼
Login
  │
  ▼
Credential Verification
  │
  ├── Invalid → Authentication Failed
  │
  └── Valid
       │
       ▼
   Token Generation
       │
       ├── Access Token
       └── Refresh Token
```

The access token is then used when accessing protected API endpoints.

---

## Password Handling

User passwords are not stored as plain text.

Before a password is stored, it is processed using the application's password hashing mechanism.

During authentication, the submitted password is checked against the stored password hash.

This keeps the original password out of the database.

---

## JWT Access Token

The access token is used to authenticate requests to protected endpoints.

The client sends the token using the standard authorization header:

```http
Authorization: Bearer <access_token>
```

The backend validates the token before allowing the request to continue.

---

## Refresh Token

The authentication system also supports refresh tokens.

A refresh token can be used to obtain a new access token when the current access token is no longer usable.

Refresh token handling remains on the backend.

---

## Token Revocation

The application maintains a revoked token list.

Revoked tokens are stored in the:

```text
revoked_tokens
```

table.

The corresponding model is:

```text
backend/app/models/revoked_token.py
```

The token identifier (`jti`) is stored as a unique indexed value.

This allows the backend to check whether a token has been revoked.

---

## Protected Requests

Protected endpoints use FastAPI authentication dependencies to obtain the authenticated user.

The general request flow is:

```text
HTTP Request
     │
     ▼
JWT Validation
     │
     ├── Invalid / Revoked
     │        │
     │        ▼
     │      Reject
     │
     └── Valid
          │
          ▼
      Authenticated User
          │
          ▼
       API Endpoint
```

Authentication is checked before protected application logic is executed.

---

## Authorization

Authentication and authorization are handled separately.

Authentication answers:

> Who is making the request?

Authorization answers:

> Is this user allowed to perform the requested action?

Role-based authorization is documented separately in:

```text
docs/security/authorization-rbac.md
```

---

## Authentication Errors

Authentication failures should be returned as controlled API errors.

Typical cases include:

- Invalid credentials
- Missing token
- Invalid token
- Expired token
- Revoked token

Error responses should not expose passwords, token contents, database credentials, or internal implementation details.

---

## Database

User authentication data is stored in PostgreSQL.

The user model is located at:

```text
backend/app/models/user.py
```

Revoked token records are stored separately:

```text
backend/app/models/revoked_token.py
```

The current `revoked_tokens` model does not have a direct foreign key relationship with the `users` table.

---

## Current State

The current authentication implementation includes:

- Password hashing
- JWT access tokens
- Refresh tokens
- Token validation
- Token revocation
- Protected API endpoints
- Role-based authorization

Authentication security should continue to evolve together with the application's authorization and API security requirements.