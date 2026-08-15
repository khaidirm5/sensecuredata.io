import {
  Bar,
  BarChart,
  CartesianGrid,
  LabelList,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

function formatCurrency(value) {
  return new Intl.NumberFormat("id-ID", {
    style: "currency",
    currency: "IDR",
    maximumFractionDigits: 0,
  }).format(Number(value ?? 0));
}

function formatCompactCurrency(value) {
  return new Intl.NumberFormat("id-ID", {
    style: "currency",
    currency: "IDR",
    notation: "compact",
    maximumFractionDigits: 1,
  }).format(Number(value ?? 0));
}

export default function RegionChart({ data = [] }) {
  const chartData = data
    .map((item) => ({
      region: item.region || "Unknown",
      sales: Number(item.total_revenue ?? 0),
    }))
    .sort((a, b) => b.sales - a.sales);

  return (
    <div className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
      <div>
        <h2 className="text-base font-semibold text-slate-900">
          Sales by Region
        </h2>

        <p className="mt-1 text-sm text-slate-500">
          Regional sales performance
        </p>
      </div>

      <div className="mt-5 h-80">
        {chartData.length === 0 ? (
          <div className="flex h-full items-center justify-center text-sm text-slate-400">
            No regional data available.
          </div>
        ) : (
          <ResponsiveContainer width="100%" height="100%">
            <BarChart
              data={chartData}
              margin={{
                top: 20,
                right: 20,
                left: 20,
                bottom: 5,
              }}
            >
              <CartesianGrid strokeDasharray="3 3" />

              <XAxis
                dataKey="region"
                tickLine={false}
                axisLine={false}
                interval={0}
                angle={-30}
                textAnchor="end"
                height={70}
              />

              <YAxis
                tickLine={false}
                axisLine={false}
                tickFormatter={formatCompactCurrency}
              />

              <Tooltip
                formatter={(value) => [
                  formatCurrency(value),
                  "Revenue",
                ]}
                labelFormatter={(label) => `Region: ${label}`}
              />

              <Bar
                dataKey="sales"
                radius={[6, 6, 0, 0]}
                minPointSize={4}
              >
                <LabelList
                  dataKey="sales"
                  position="top"
                  formatter={formatCompactCurrency}
                  fontSize={10}
                />
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        )}
      </div>
    </div>
  );
}