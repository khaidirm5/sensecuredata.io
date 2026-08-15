import { X } from "lucide-react";

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

export default function SaleDetailModal({
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
      onMouseDown={(event) => {
        if (event.target === event.currentTarget) {
          onClose();
        }
      }}
    >
      <div className="w-full max-w-2xl rounded-xl border border-slate-200 bg-white shadow-xl">
        <div className="flex items-center justify-between border-b border-slate-200 px-6 py-4">
          <div>
            <h2 className="text-lg font-semibold text-slate-900">
              Sale Details
            </h2>

            <p className="mt-1 text-sm text-slate-500">
              Detailed information about this sales record.
            </p>
          </div>

          <button
            type="button"
            onClick={onClose}
            className="rounded-lg p-2 text-slate-500 transition hover:bg-slate-100 hover:text-slate-700"
            aria-label="Close"
          >
            <X size={20} />
          </button>
        </div>

        {isLoading ? (
          <div className="space-y-4 p-6">
            {[1, 2, 3, 4, 5, 6].map((item) => (
              <div
                key={item}
                className="h-10 animate-pulse rounded-lg bg-slate-100"
              />
            ))}
          </div>
        ) : (
          <div className="grid gap-4 p-6 sm:grid-cols-2">
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
              label="Upload ID"
              value={sale.upload_id}
            />

            <DetailItem
              label="Record ID"
              value={sale.id}
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
        )}

        <div className="flex justify-end border-t border-slate-200 px-6 py-4">
          <button
            type="button"
            onClick={onClose}
            className="rounded-lg bg-slate-900 px-5 py-2 text-sm font-medium text-white transition hover:bg-slate-800"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );
}

function DetailItem({ label, value }) {
  return (
    <div className="rounded-lg border border-slate-200 bg-slate-50 p-4">
      <p className="text-xs font-medium uppercase tracking-wide text-slate-500">
        {label}
      </p>

      <p className="mt-1 break-words text-sm font-medium text-slate-900">
        {value ?? "-"}
      </p>
    </div>
  );
}