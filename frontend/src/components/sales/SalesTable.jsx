function formatCurrency(value) {
  return new Intl.NumberFormat("id-ID", {
    style: "currency",
    currency: "IDR",
    maximumFractionDigits: 0,
  }).format(Number(value ?? 0));
}

function formatNumber(value) {
  return new Intl.NumberFormat("id-ID").format(
    Number(value ?? 0),
  );
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

export default function SalesTable({
  data = [],
  isLoading = false,
  onView,
  onEdit,
  onDelete,
}) {
  if (isLoading) {
    return (
      <div className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
        <div className="space-y-3">
          {[1, 2, 3, 4, 5].map((item) => (
            <div
              key={item}
              className="h-12 animate-pulse rounded-lg bg-slate-100"
            />
          ))}
        </div>
      </div>
    );
  }

  return (
    <div className="overflow-hidden rounded-xl border border-slate-200 bg-white shadow-sm">
      <div className="border-b border-slate-200 px-5 py-4">
        <h2 className="text-base font-semibold text-slate-900">
          Sales Records
        </h2>

        <p className="mt-1 text-sm text-slate-500">
          Manage sales transactions stored in the platform.
        </p>
      </div>

      {data.length === 0 ? (
        <div className="flex min-h-48 items-center justify-center px-5 py-8 text-sm text-slate-400">
          No sales records found.
        </div>
      ) : (
        <div className="overflow-x-auto">
          <table className="w-full min-w-[1100px] text-left text-sm">
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
                  Unit Price
                </th>

                <th className="px-5 py-3 font-medium">
                  Total
                </th>

                <th className="px-5 py-3 text-right font-medium">
                  Actions
                </th>
              </tr>
            </thead>

            <tbody className="divide-y divide-slate-100">
              {data.map((sale) => (
                <tr
                  key={sale.id}
                  className="hover:bg-slate-50"
                >
                  <td className="whitespace-nowrap px-5 py-4 font-medium text-slate-900">
                    {sale.invoice_number}
                  </td>

                  <td className="whitespace-nowrap px-5 py-4 text-slate-600">
                    {formatDate(sale.order_date)}
                  </td>

                  <td className="max-w-[220px] truncate px-5 py-4 text-slate-600">
                    {sale.product_name}
                  </td>

                  <td className="whitespace-nowrap px-5 py-4 text-slate-600">
                    {sale.category}
                  </td>

                  <td className="whitespace-nowrap px-5 py-4 text-slate-600">
                    {sale.region || "Unknown"}
                  </td>

                  <td className="whitespace-nowrap px-5 py-4 text-slate-600">
                    {formatNumber(sale.quantity)}
                  </td>

                  <td className="whitespace-nowrap px-5 py-4 text-slate-600">
                    {formatCurrency(sale.unit_price)}
                  </td>

                  <td className="whitespace-nowrap px-5 py-4 font-medium text-slate-900">
                    {formatCurrency(sale.total_price)}
                  </td>

                  <td className="whitespace-nowrap px-5 py-4 text-right">
                    <div className="flex justify-end gap-2">
                      <button
                        type="button"
                        onClick={() => onView?.(sale)}
                        className="rounded-md border border-slate-300 px-3 py-1.5 text-xs font-medium text-slate-700 transition hover:bg-slate-50"
                      >
                        View
                      </button>

                      <button
                        type="button"
                        onClick={() => onEdit?.(sale)}
                        className="rounded-md border border-slate-300 px-3 py-1.5 text-xs font-medium text-slate-700 transition hover:bg-slate-50"
                      >
                        Edit
                      </button>

                      <button
                        type="button"
                        onClick={() => onDelete?.(sale)}
                        className="rounded-md border border-red-200 px-3 py-1.5 text-xs font-medium text-red-600 transition hover:bg-red-50"
                      >
                        Delete
                      </button>
                    </div>
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