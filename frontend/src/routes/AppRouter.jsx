import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

function Placeholder({ title }) {
  return (
    <div className="p-8 text-2xl font-semibold">
      {title}
    </div>
  );
}

export default function AppRouter() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/login" replace />} />

        <Route
          path="/login"
          element={<Placeholder title="Login Page" />}
        />

        <Route
          path="/dashboard"
          element={<Placeholder title="Dashboard Page" />}
        />

        <Route
          path="/sales"
          element={<Placeholder title="Sales Page" />}
        />

        <Route
          path="/upload"
          element={<Placeholder title="Upload Page" />}
        />

        <Route
          path="/security"
          element={<Placeholder title="Security Page" />}
        />

        <Route
          path="*"
          element={<Placeholder title="404 Not Found" />}
        />
      </Routes>
    </BrowserRouter>
  );
}