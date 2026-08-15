import { ArrowDownRight, ArrowUpRight } from "lucide-react";

export default function StatCard({
  title,
  value,
  description,
  trend,
  trendLabel,
  icon: Icon,
}) {
  const isPositive = trend >= 0;

  return (
    <div className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
      <div className="flex items-start justify-between">
        <div>
          <p className="text-sm font-medium text-slate-500">
            {title}
          </p>

          <p className="mt-2 text-2xl font-bold text-slate-900">
            {value}
          </p>

          {description && (
            <p className="mt-1 text-xs text-slate-400">
              {description}
            </p>
          )}
        </div>

        {Icon && (
          <div className="rounded-lg bg-slate-100 p-2.5 text-slate-600">
            <Icon size={20} />
          </div>
        )}
      </div>

      <div className="mt-4 flex items-center gap-2 text-xs">
        <span
          className={`flex items-center gap-1 font-medium ${
            isPositive ? "text-emerald-600" : "text-red-600"
          }`}
        >
          {isPositive ? (
            <ArrowUpRight size={14} />
          ) : (
            <ArrowDownRight size={14} />
          )}

          {Math.abs(trend)}%
        </span>

        <span className="text-slate-400">{trendLabel}</span>
      </div>
    </div>
  );
}
