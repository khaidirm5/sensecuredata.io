import { useState } from "react";

export default function SalesEditModal({
  sale,
  isLoading,
  onClose,
  onSave,
}) {
  const [form, setForm] = useState(() => ({
    invoice_number: sale?.invoice_number ?? "",
    order_date: sale?.order_date ?? "",
    product_name: sale?.product_name ?? "",
    category: sale?.category ?? "",
    quantity: sale?.quantity ?? "",
    unit_price: sale?.unit_price ?? "",
    total_price: sale?.total_price ?? "",
    region: sale?.region ?? "",
  }));

  if (!sale) {
    return null;
  }

  function handleChange(event) {
    const { name, value } = event.target;

    setForm((current) => ({
      ...current,
      [name]: value,
    }));
  }

  function handleSubmit(event) {
    event.preventDefault();

    onSave({
      invoice_number: form.invoice_number,
      order_date: form.order_date,
      product_name: form.product_name,
      category: form.category,
      quantity: Number(form.quantity),
      unit_price: Number(form.unit_price),
      total_price: Number(form.total_price),
      region: form.region || null,
    });
  }

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/50 p-4">
      <div className="w-full max-w-3xl overflow-hidden rounded-xl bg-white shadow-xl">
        <div className="flex items-center justify-between border-b border-slate-200 px-6 py-4">
          <div>
            <h2 className="text-lg font-semibold text-slate-900">
              Edit Sales
            </h2>

            <p className="mt-1 text-sm text-slate-500">
              Update sales record #{sale.id}
            </p>
          </div>

          <button
            type="button"
            onClick={onClose}
            disabled={isLoading}
            className="rounded-lg px-3 py-2 text-sm text-slate-500 hover:bg-slate-100 disabled:cursor-not-allowed disabled:opacity-50"
          >
            Close
          </button>
        </div>

        <form onSubmit={handleSubmit} className="p-6">
          <div className="grid gap-4 sm:grid-cols-2">
            <Field
              label="Invoice Number"
              name="invoice_number"
              value={form.invoice_number}
              onChange={handleChange}
              required
            />

            <Field
              label="Order Date"
              name="order_date"
              type="date"
              value={form.order_date}
              onChange={handleChange}
              required
            />

            <Field
              label="Product"
              name="product_name"
              value={form.product_name}
              onChange={handleChange}
              required
            />

            <Field
              label="Category"
              name="category"
              value={form.category}
              onChange={handleChange}
              required
            />

            <Field
              label="Quantity"
              name="quantity"
              type="number"
              min="0"
              value={form.quantity}
              onChange={handleChange}
              required
            />

            <Field
              label="Unit Price"
              name="unit_price"
              type="number"
              min="0"
              step="0.01"
              value={form.unit_price}
              onChange={handleChange}
              required
            />

            <Field
              label="Total Price"
              name="total_price"
              type="number"
              min="0"
              step="0.01"
              value={form.total_price}
              onChange={handleChange}
              required
            />

            <Field
              label="Region"
              name="region"
              value={form.region}
              onChange={handleChange}
            />
          </div>

          <div className="mt-6 flex justify-end gap-2 border-t border-slate-200 pt-4">
            <button
              type="button"
              onClick={onClose}
              disabled={isLoading}
              className="rounded-lg border border-slate-300 px-4 py-2 text-sm font-medium text-slate-700 hover:bg-slate-50 disabled:cursor-not-allowed disabled:opacity-50"
            >
              Cancel
            </button>

            <button
              type="submit"
              disabled={isLoading}
              className="rounded-lg bg-slate-900 px-4 py-2 text-sm font-medium text-white hover:bg-slate-800 disabled:cursor-not-allowed disabled:opacity-50"
            >
              {isLoading ? "Saving..." : "Save Changes"}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

function Field({
  label,
  name,
  type = "text",
  value,
  onChange,
  required = false,
  min,
  step,
}) {
  return (
    <div>
      <label
        htmlFor={`sales-edit-${name}`}
        className="mb-1.5 block text-sm font-medium text-slate-700"
      >
        {label}
      </label>

      <input
        id={`sales-edit-${name}`}
        name={name}
        type={type}
        value={value}
        onChange={onChange}
        required={required}
        min={min}
        step={step}
        className="w-full rounded-lg border border-slate-300 px-3 py-2 text-sm outline-none focus:border-slate-500 focus:ring-2 focus:ring-slate-200"
      />
    </div>
  );
}