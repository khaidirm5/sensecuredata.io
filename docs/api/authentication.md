# Authentication API

## Overview

The authentication API handles user login and token management for the application.

Authentication is implemented in the FastAPI backend using JSON Web Tokens (JWT).

The related backend code is located under:

```text
backend/app/api/
backend/app/security/
backend/app/services/
```

---

## Authentication Flow

The general authentication flow is:

```text
User
  │
  ▼
Login Request
  │
  ▼
FastAPI Authentication Endpoint
  │
  ├── Verify Credentials
  │
  └── Generate Tokens
          │
          ├── Access Token
          └── Refresh Token
```

The client uses the access token when accessing protected API endpoints.

---

## Login

The login endpoint receives the user's credentials and verifies them against the stored user information.

A successful login returns authentication tokens that can be used for subsequent requests.

The authentication implementation is handled by the backend rather than by the React frontend.

---

## Access Token

The access token is used to access protected API endpoints.

The client sends the token with authenticated requests.

Conceptually:

```http
Authorization: Bearer <access_token>
```

The backend validates the token before allowing access to protected resources.

---

## Refresh Token

A refresh token is issued as part of the authentication flow.

It can be used to obtain a new access token when the current access token is no longer valid.

Refresh token handling is implemented on the backend.

---

## Token Revocation

The application maintains a revoked token list.

Revoked token records are stored in:

```text
revoked_tokens
```

The corresponding model is:

```text
backend/app/models/revoked_token.py
```

The token identifier (`jti`) is stored as a unique indexed value.

This allows the backend to check whether a token has been revoked.

---

## Protected Endpoints

Protected endpoints require a valid authenticated user.

Authentication information is resolved through FastAPI dependencies before the endpoint continues with its normal processing.

The general flow is:

```text
HTTP Request
     │
     ▼
Authentication Dependency
     │
     ├── Invalid Token → Reject Request
     │
     └── Valid Token
            │
            ▼
        API Endpoint
```

---

## User Roles

The application supports role-based authorization.

Current roles include:

- `admin`
- `analyst`
- `user`

Authentication determines the identity of the user.

Authorization determines whether that user has permission to perform a particular operation.

Role and permission handling is documented separately in:

```text
docs/security/authorization-rbac.md
```

---

## Password Handling

User passwords are not stored as plain text.

The authentication system uses password hashing before credentials are stored.

During login, the submitted password is checked against the stored password hash.

---

## Authentication Errors

Authentication failures should return an appropriate HTTP error response rather than exposing sensitive authentication details.

Examples include:

- Invalid credentials
- Missing authentication token
- Invalid token
- Expired token
- Revoked token

The backend is responsible for handling these cases.

---

## Frontend Integration

The React frontend communicates with the authentication API through the frontend service layer.

The frontend is responsible for maintaining the authentication state required by the user interface.

The backend remains responsible for validating tokens and enforcing access to protected resources.

---

## Current State

The authentication system currently includes:

- JWT authentication
- Access tokens
- Refresh tokens
- Password hashing
- Token validation
- Token revocation
- Role-based authorization

The implementation may evolve as additional authentication and security requirements are added to the project.