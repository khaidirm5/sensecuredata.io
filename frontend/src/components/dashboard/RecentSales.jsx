function formatCurrency(value) {
  return new Intl.NumberFormat("id-ID", {
    style: "currency",
    currency: "IDR",
    maximumFractionDigits: 0,
  }).format(Number(value ?? 0));
}

function formatDate(value) {
  if (!value) {
    return "-";
  }

  const date = new Date(value);

  if (Number.isNaN(date.getTime())) {
    return value;
  }

  return new Intl.DateTimeFormat("id-ID", {
    day: "2-digit",
    month: "short",
    year: "numeric",
  }).format(date);
}

export default function RecentSales({ data = [], isLoading = false }) {
  return (
    <div className="overflow-hidden rounded-xl border border-slate-200 bg-white">
      <div className="border-b border-slate-200 px-5 py-4">
        <h2 className="text-base font-semibold text-slate-900">
          Recent Sales
        </h2>

        <p className="mt-1 text-sm text-slate-500">
          Latest sales transactions
        </p>
      </div>

      {isLoading ? (
        <div className="space-y-3 p-5">
          {[1, 2, 3, 4, 5].map((item) => (
            <div
              key={item}
              className="h-12 animate-pulse rounded-lg bg-slate-100"
            />
          ))}
        </div>
      ) : data.length === 0 ? (
        <div className="flex h-40 items-center justify-center px-5 text-sm text-slate-400">
          No recent sales available.
        </div>
      ) : (
        <div className="overflow-x-auto">
          <table className="w-full text-left text-sm">
            <thead className="bg-slate-50 text-xs uppercase text-slate-500">
              <tr>
                <th className="px-5 py-3 font-medium">
                  Invoice
                </th>

                <th className="px-5 py-3 font-medium">
                  Date
                </th>

                <th className="px-5 py-3 font-medium">
                  Product
                </th>

                <th className="px-5 py-3 font-medium">
                  Category
                </th>

                <th className="px-5 py-3 font-medium">
                  Region
                </th>

                <th className="px-5 py-3 font-medium">
                  Quantity
                </th>

                <th className="px-5 py-3 font-medium">
                  Amount
                </th>
              </tr>
            </thead>

            <tbody className="divide-y divide-slate-100">
              {data.map((sale) => (
                <tr
                  key={`${sale.invoice_number}-${sale.product_name}-${sale.order_date}`}
                  className="hover:bg-slate-50"
                >
                  <td className="whitespace-nowrap px-5 py-4 font-medium text-slate-900">
                    {sale.invoice_number}
                  </td>

                  <td className="whitespace-nowrap px-5 py-4 text-slate-600">
                    {formatDate(sale.order_date)}
                  </td>

                  <td className="px-5 py-4 text-slate-600">
                    {sale.product_name}
                  </td>

                  <td className="whitespace-nowrap px-5 py-4 text-slate-600">
                    {sale.category}
                  </td>

                  <td className="whitespace-nowrap px-5 py-4 text-slate-600">
                    {sale.region || "Unknown"}
                  </td>

                  <td className="whitespace-nowrap px-5 py-4 text-slate-600">
                    {new Intl.NumberFormat("id-ID").format(
                      Number(sale.quantity ?? 0)
                    )}
                  </td>

                  <td className="whitespace-nowrap px-5 py-4 font-medium text-slate-900">
                    {formatCurrency(sale.total_price)}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}