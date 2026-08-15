import {
  AlertTriangle,
  CheckCircle2,
  FileUp,
  ShieldCheck,
} from "lucide-react";

const activities = [
  {
    title: "Latest Upload",
    value: "sales_sample.csv",
    description: "124 records processed",
    icon: FileUp,
  },
  {
    title: "Upload Status",
    value: "Completed",
    description: "Last processed successfully",
    icon: CheckCircle2,
  },
  {
    title: "Security Scan",
    value: "Safe",
    description: "No critical threats detected",
    icon: ShieldCheck,
  },
  {
    title: "Risk Alerts",
    value: "2",
    description: "Requires review",
    icon: AlertTriangle,
  },
];

export default function ActivitySummary() {
  return (
    <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
      {activities.map((activity) => {
        const Icon = activity.icon;

        return (
          <div
            key={activity.title}
            className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm"
          >
            <div className="flex items-center gap-3">
              <div className="rounded-lg bg-slate-100 p-2 text-slate-600">
                <Icon size={18} />
              </div>

              <p className="text-sm font-medium text-slate-500">
                {activity.title}
              </p>
            </div>

            <p className="mt-4 font-semibold text-slate-900">
              {activity.value}
            </p>

            <p className="mt-1 text-xs text-slate-500">
              {activity.description}
            </p>
          </div>
        );
      })}
    </div>
  );
}
