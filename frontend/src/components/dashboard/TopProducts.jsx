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

export default function TopProducts({ data = [] }) {
  return (
    <div className="rounded-xl border border-slate-200 bg-white">
      <div className="border-b border-slate-200 px-5 py-4">
        <h2 className="text-base font-semibold text-slate-900">
          Top Products
        </h2>

        <p className="mt-1 text-sm text-slate-500">
          Best-selling products by quantity
        </p>
      </div>

      <div className="overflow-x-auto">
        {data.length === 0 ? (
          <div className="flex min-h-40 items-center justify-center px-5 py-8 text-sm text-slate-400">
            No product data available.
          </div>
        ) : (
          <table className="w-full text-left text-sm">
            <thead className="bg-slate-50 text-xs uppercase text-slate-500">
              <tr>
                <th className="px-5 py-3 font-medium">
                  #
                </th>

                <th className="px-5 py-3 font-medium">
                  Product
                </th>

                <th className="px-5 py-3 font-medium">
                  Quantity Sold
                </th>

                <th className="px-5 py-3 font-medium">
                  Revenue
                </th>
              </tr>
            </thead>

            <tbody className="divide-y divide-slate-100">
              {data.map((product, index) => (
                <tr
                  key={`${product.product_name}-${index}`}
                  className="hover:bg-slate-50"
                >
                  <td className="whitespace-nowrap px-5 py-4 font-medium text-slate-500">
                    {index + 1}
                  </td>

                  <td className="px-5 py-4 font-medium text-slate-900">
                    {product.product_name}
                  </td>

                  <td className="whitespace-nowrap px-5 py-4 text-slate-600">
                    {formatNumber(product.total_quantity)}
                  </td>

                  <td className="whitespace-nowrap px-5 py-4 font-medium text-slate-900">
                    {formatCurrency(product.total_revenue)}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
}