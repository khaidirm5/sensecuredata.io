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
    month: "long",
    year: "numeric",
  }).format(date);
}

function DetailItem({ label, value }) {
  return (
    <div>
      <p className="text-xs font-medium uppercase tracking-wide text-slate-400">
        {label}
      </p>

      <p className="mt-1 text-sm font-medium text-slate-900">
        {value ?? "-"}
      </p>
    </div>
  );
}

export default function SalesViewModal({
  sale,
  isLoading = false,
  onClose,
}) {
  if (!sale && !isLoading) {
    return null;
  }

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/50 p-4"
      onMouseDown={onClose}
    >
      <div
        className="w-full max-w-2xl overflow-hidden rounded-xl bg-white shadow-xl"
        onMouseDown={(event) => event.stopPropagation()}
      >
        <div className="flex items-start justify-between border-b border-slate-200 px-6 py-5">
          <div>
            <p className="text-xs font-medium uppercase tracking-wide text-slate-400">
              Sales Record
            </p>

            <h2 className="mt-1 text-xl font-bold text-slate-900">
              Sales Details
            </h2>

            {sale && (
              <p className="mt-1 text-sm text-slate-500">
                Invoice {sale.invoice_number}
              </p>
            )}
          </div>

          <button
            type="button"
            onClick={onClose}
            className="rounded-lg px-3 py-2 text-sm text-slate-500 hover:bg-slate-100"
          >
            Close
          </button>
        </div>

        {isLoading ? (
          <div className="space-y-4 p-6">
            <div className="h-5 w-40 animate-pulse rounded bg-slate-200" />
            <div className="h-5 w-56 animate-pulse rounded bg-slate-200" />
            <div className="h-5 w-48 animate-pulse rounded bg-slate-200" />
            <div className="h-5 w-64 animate-pulse rounded bg-slate-200" />
            <div className="h-5 w-52 animate-pulse rounded bg-slate-200" />
          </div>
        ) : (
          <div className="p-6">
            <div className="grid gap-5 sm:grid-cols-2">
              <DetailItem
                label="Invoice Number"
                value={sale.invoice_number}
              />

              <DetailItem
                label="Order Date"
                value={formatDate(sale.order_date)}
              />

              <DetailItem
                label="Product"
                value={sale.product_name}
              />

              <DetailItem
                label="Category"
                value={sale.category}
              />

              <DetailItem
                label="Region"
                value={sale.region || "Unknown"}
              />

              <DetailItem
                label="Quantity"
                value={formatNumber(sale.quantity)}
              />

              <DetailItem
                label="Unit Price"
                value={formatCurrency(sale.unit_price)}
              />

              <DetailItem
                label="Total Price"
                value={formatCurrency(sale.total_price)}
              />

              <DetailItem
                label="Record ID"
                value={sale.id}
              />

              <DetailItem
                label="Upload ID"
                value={sale.upload_id}
              />

              <DetailItem
                label="Created At"
                value={formatDate(sale.created_at)}
              />

              <DetailItem
                label="Updated At"
                value={formatDate(sale.updated_at)}
              />
            </div>

            <div className="mt-6 flex justify-end border-t border-slate-200 pt-4">
              <button
                type="button"
                onClick={onClose}
                className="rounded-lg bg-slate-900 px-4 py-2 text-sm font-medium text-white hover:bg-slate-800"
              >
                Close
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}