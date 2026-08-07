# Frontend Routing

## Overview

Frontend routing is handled using React Router.

The routing configuration is located in:

```text
frontend/src/routes/AppRouter.jsx
```

The current router uses `BrowserRouter`, `Routes`, `Route`, and `Navigate` from `react-router-dom`.

At the current stage, the defined routes use placeholder components rather than the actual application pages.

## Router Structure

The current routing structure is:

```text
AppRouter
└── BrowserRouter
    └── Routes
        ├── /
        ├── /login
        ├── /dashboard
        ├── /sales
        ├── /upload
        ├── /security
        └── *
```

## Defined Routes

| Path | Current Component | Purpose |
|---|---|---|
| `/` | Placeholder | Root route |
| `/login` | Placeholder | Login page |
| `/dashboard` | Placeholder | Dashboard page |
| `/sales` | Placeholder | Sales page |
| `/upload` | Placeholder | Upload page |
| `/security` | Placeholder | Security page |
| `*` | Placeholder | 404 fallback |

## Root Route

The root path is:

```text
/
```

The router defines a root route for the application.

The current implementation is still under development, so the actual root-page behavior should not be considered finalized.

## Login Route

The login route is:

```text
/login
```

It currently renders a placeholder with the title:

```text
Login Page
```

The route is intended to represent the authentication entry point of the application.

Authentication and authorization behavior should not be inferred from the route definition alone.

## Dashboard Route

The dashboard route is:

```text
/dashboard
```

It currently renders a placeholder with the title:

```text
Dashboard Page
```

The actual dashboard page has not yet been connected to this route in the current router implementation.

## Sales Route

The sales route is:

```text
/sales
```

It currently renders a placeholder with the title:

```text
Sales Page
```

The route is intended for the sales-related frontend functionality.

## Upload Route

The upload route is:

```text
/upload
```

It currently renders a placeholder with the title:

```text
Upload Page
```

The route is intended for the dataset upload functionality.

## Security Route

The security route is:

```text
/security
```

It currently renders a placeholder with the title:

```text
Security Page
```

The route is intended for the Security Center interface.

## 404 Route

The router also defines a wildcard route:

```text
*
```

This route is used as the fallback for paths that do not match the defined routes.

The current implementation renders a placeholder with:

```text
404 Not Found
```

## Placeholder Component

The current router defines a local `Placeholder` component:

```jsx
function Placeholder({ title }) {
  return (
    <div>
      {title}
    </div>
  );
}
```

This component is currently used by the defined routes instead of the actual page components.

This indicates that frontend routing has been established, while the connection between routes and the final page implementations is still in development.

## Current Routing State

The current routing implementation can be summarized as:

```text
Browser
   ↓
BrowserRouter
   ↓
Routes
   ├── /
   ├── /login
   ├── /dashboard
   ├── /sales
   ├── /upload
   ├── /security
   └── *
        ↓
   Placeholder Component
```

The router currently provides the basic navigation structure, but the application pages are not yet connected to these routes.

## Authentication and Route Protection

The current `AppRouter.jsx` code does not show protected routes or authentication guards.

Therefore, this document does not claim that routes such as `/dashboard`, `/sales`, `/upload`, or `/security` are currently protected by authentication or role-based authorization.

Authentication and authorization are handled separately in the backend, while frontend route protection can be added as the frontend implementation progresses.

## Future Routing Work

As the frontend implementation progresses, the placeholder components can be replaced with the actual page components.

Potential work includes:

- Connecting routes to the corresponding page components.
- Adding authentication-aware route handling.
- Adding role-based frontend navigation where required.
- Adding a proper 404 page.
- Organizing route configuration as the number of application pages grows.

These items represent future frontend work and are not considered implemented features in the current router.