export default function NotFoundPage() {
  return (
    <main className="flex min-h-screen items-center justify-center bg-slate-100 p-6">
      <div className="rounded-xl border border-slate-200 bg-white p-8 text-center shadow-sm">
        <p className="text-sm font-medium text-slate-500">Error</p>

        <h1 className="mt-1 text-3xl font-bold text-slate-900">
          404
        </h1>

        <p className="mt-2 text-sm text-slate-500">
          The requested page could not be found.
        </p>
      </div>
    </main>
  );
}
