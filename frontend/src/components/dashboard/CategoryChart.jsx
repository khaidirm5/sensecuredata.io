import {
  Cell,
  Pie,
  PieChart,
  ResponsiveContainer,
  Tooltip,
} from "recharts";

const COLORS = [
  "#1e293b",
  "#475569",
  "#64748b",
  "#94a3b8",
  "#cbd5e1",
];

function formatCurrency(value) {
  return new Intl.NumberFormat("id-ID", {
    style: "currency",
    currency: "IDR",
    maximumFractionDigits: 0,
  }).format(Number(value ?? 0));
}

export default function CategoryChart({ data = [] }) {
  const totalRevenue = data.reduce(
    (sum, item) => sum + Number(item.total_revenue ?? 0),
    0,
  );

  const chartData = data.map((item) => {
    const revenue = Number(item.total_revenue ?? 0);

    return {
      name: item.category,
      value: revenue,
      percentage:
        totalRevenue > 0 ? (revenue / totalRevenue) * 100 : 0,
    };
  });

  return (
    <div className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
      <div>
        <h2 className="text-base font-semibold text-slate-900">
          Sales by Category
        </h2>

        <p className="mt-1 text-sm text-slate-500">
          Revenue distribution by category
        </p>
      </div>

      <div className="mt-5 h-72">
        {chartData.length === 0 ? (
          <div className="flex h-full items-center justify-center text-sm text-slate-400">
            No category data available.
          </div>
        ) : (
          <ResponsiveContainer width="100%" height="100%">
            <PieChart>
              <Pie
                data={chartData}
                dataKey="value"
                nameKey="name"
                cx="50%"
                cy="50%"
                innerRadius={60}
                outerRadius={95}
                paddingAngle={3}
              >
                {chartData.map((entry, index) => (
                  <Cell
                    key={entry.name}
                    fill={COLORS[index % COLORS.length]}
                  />
                ))}
              </Pie>

              <Tooltip
                formatter={(value) => [
                  formatCurrency(value),
                  "Revenue",
                ]}
              />
            </PieChart>
          </ResponsiveContainer>
        )}
      </div>

      <div className="grid grid-cols-2 gap-3">
        {chartData.map((item, index) => (
          <div
            key={item.name}
            className="flex items-center gap-2 text-xs text-slate-600"
          >
            <span
              className="h-2.5 w-2.5 rounded-full"
              style={{
                backgroundColor:
                  COLORS[index % COLORS.length],
              }}
            />

            <span className="truncate">{item.name}</span>

            <span className="ml-auto font-medium text-slate-900">
              {item.percentage.toFixed(1)}%
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}
