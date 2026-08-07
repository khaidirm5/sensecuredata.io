# Frontend Architecture

## Overview

The frontend of Sentinel Secure Data Intelligence Platform is built with React and Vite.

The frontend handles the application interface and communicates with the FastAPI backend through HTTP requests. The code is separated into pages, reusable components, routing, services, contexts, hooks, and utility functions.

The main frontend source code is located in:

```text
frontend/src/
├── assets/
├── components/
├── contexts/
├── hooks/
├── layouts/
├── pages/
├── routes/
├── services/
├── styles/
├── types/
├── utils/
├── App.css
├── App.jsx
├── index.css
└── main.jsx
```

---

## Application Entry Point

The frontend starts from:

```text
frontend/src/main.jsx
```

The main application component is:

```text
frontend/src/App.jsx
```

`main.jsx` mounts the React application, while `App.jsx` acts as the main application component.

---

## Pages

The `pages` directory contains the application's page-level components.

A page normally brings together the components, layout, routing state, and data required for a particular screen.

Examples of application areas include:

- Authentication
- Dashboard
- Sales
- Upload
- Analytics
- Security
- Audit Log
- Profile
- Settings

The exact pages will continue to change as development progresses.

---

## Components

The `components` directory contains reusable interface components.

Components are used when an element or piece of interface logic is needed in more than one part of the application.

Keeping reusable elements here helps avoid putting large amounts of UI code directly inside page files.

---

## Layouts

The `layouts` directory contains shared page layouts.

Layouts are used for common application structures such as navigation, sidebar areas, headers, and page containers.

This allows multiple pages to use the same overall structure without duplicating the layout code.

---

## Routing

Frontend routing is maintained in:

```text
frontend/src/routes/
```

React Router is used to handle navigation between application pages.

Routes determine which page component is displayed for a given URL.

Protected areas of the application can also use the routing layer together with authentication state to control access.

---

## Services

The `services` directory contains frontend modules used to communicate with the backend.

Axios is used as the HTTP client.

A simplified request flow is:

```text
React Page / Component
        ↓
Frontend Service
        ↓
FastAPI API
        ↓
Service / Repository
        ↓
PostgreSQL
```

Components should not connect directly to PostgreSQL. All database access is handled by the backend.

---

## Contexts

The `contexts` directory contains React Context implementations.

Context is used for data or state that needs to be available across different parts of the application.

Authentication-related state is one example of information that can be shared through this layer.

---

## Hooks

The `hooks` directory contains reusable React hooks.

Hooks are used to keep repeated frontend behavior separate from individual pages and components.

---

## Types

The `types` directory contains shared frontend type definitions.

These definitions provide a common structure for data used across different frontend modules.

---

## Utilities

The `utils` directory contains general-purpose helper functions.

Utilities should remain independent from individual pages whenever possible.

---

## Styling

Frontend styling is maintained through:

```text
frontend/src/index.css
frontend/src/App.css
frontend/src/styles/
```

Global styles are kept separate from page and component logic.

---

## Data Visualization

The frontend uses Recharts for data visualization.

Charts are primarily used for dashboard and analytical interfaces where data needs to be presented visually.

---

## Frontend and Backend

The frontend and backend are separate parts of the project.

```text
frontend/
    React + Vite
         │
         │ HTTP / REST API
         ▼
backend/
    FastAPI
         │
         ▼
    PostgreSQL
```

The frontend is responsible for the user interface, while authentication, business logic, validation, data processing, and database operations are handled by the backend.

---

## Current State

The frontend foundation is already in place with React, Vite, routing, reusable component directories, service modules, contexts, hooks, and styling structure.

Feature implementation is still progressing, so the frontend structure may change as new application functionality is added.

The architecture is intentionally kept modular so new pages and features can be added without putting the entire application into a small number of large components.