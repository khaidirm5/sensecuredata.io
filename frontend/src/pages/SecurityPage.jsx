export default function SecurityPage() {
  return (
    <section>
      <div>
        <p className="text-sm font-medium text-slate-500">Security</p>
        <h1 className="mt-1 text-2xl font-bold text-slate-900">
          Security Center
        </h1>
        <p className="mt-1 text-sm text-slate-500">
          Monitor file validation and security scan activity.
        </p>
      </div>

      <div className="mt-6 rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
        <p className="text-sm text-slate-500">
          Security monitoring will be connected to the backend API.
        </p>
      </div>
    </section>
  );
}
