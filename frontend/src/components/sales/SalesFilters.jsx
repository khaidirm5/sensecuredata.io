import { useState } from "react";

export default function SalesFilters({
  filters,
  onApply,
  onReset,
}) {
  const [search, setSearch] = useState(
    filters.search ?? "",
  );

  const [category, setCategory] = useState(
    filters.category ?? "",
  );

  const [region, setRegion] = useState(
    filters.region ?? "",
  );

  const [sortBy, setSortBy] = useState(
    filters.sort_by ?? "order_date",
  );

  const [order, setOrder] = useState(
    filters.order ?? "desc",
  );

  function handleSubmit(event) {
    event.preventDefault();

    onApply({
      search: search.trim() || undefined,
      category: category || undefined,
      region: region || undefined,
      sort_by: sortBy,
      order,
    });
  }

  function handleReset() {
    setSearch("");
    setCategory("");
    setRegion("");
    setSortBy("order_date");
    setOrder("desc");

    onReset();
  }

  return (
    <div className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
      <div>
        <h2 className="text-base font-semibold text-slate-900">
          Sales Filters
        </h2>

        <p className="mt-1 text-sm text-slate-500">
          Search, filter, and sort sales records.
        </p>
      </div>

      <form
        onSubmit={handleSubmit}
        className="mt-5 grid gap-4 md:grid-cols-2 xl:grid-cols-5"
      >
        <div className="xl:col-span-2">
          <label
            htmlFor="sales-search"
            className="mb-1.5 block text-sm font-medium text-slate-700"
          >
            Search
          </label>

          <input
            id="sales-search"
            type="search"
            value={search}
            onChange={(event) =>
              setSearch(event.target.value)
            }
            placeholder="Invoice, product, category, region..."
            className="w-full rounded-lg border border-slate-300 px-3 py-2 text-sm outline-none transition focus:border-slate-500 focus:ring-2 focus:ring-slate-200"
          />
        </div>

        <div>
          <label
            htmlFor="sales-category"
            className="mb-1.5 block text-sm font-medium text-slate-700"
          >
            Category
          </label>

          <input
            id="sales-category"
            type="text"
            value={category}
            onChange={(event) =>
              setCategory(event.target.value)
            }
            placeholder="All categories"
            className="w-full rounded-lg border border-slate-300 px-3 py-2 text-sm outline-none transition focus:border-slate-500 focus:ring-2 focus:ring-slate-200"
          />
        </div>

        <div>
          <label
            htmlFor="sales-region"
            className="mb-1.5 block text-sm font-medium text-slate-700"
          >
            Region
          </label>

          <input
            id="sales-region"
            type="text"
            value={region}
            onChange={(event) =>
              setRegion(event.target.value)
            }
            placeholder="All regions"
            className="w-full rounded-lg border border-slate-300 px-3 py-2 text-sm outline-none transition focus:border-slate-500 focus:ring-2 focus:ring-slate-200"
          />
        </div>

        <div>
          <label
            htmlFor="sales-sort"
            className="mb-1.5 block text-sm font-medium text-slate-700"
          >
            Sort By
          </label>

          <select
            id="sales-sort"
            value={sortBy}
            onChange={(event) =>
              setSortBy(event.target.value)
            }
            className="w-full rounded-lg border border-slate-300 bg-white px-3 py-2 text-sm outline-none transition focus:border-slate-500 focus:ring-2 focus:ring-slate-200"
          >
            <option value="order_date">
              Order Date
            </option>
            <option value="invoice_number">
              Invoice Number
            </option>
            <option value="product_name">
              Product
            </option>
            <option value="category">
              Category
            </option>
            <option value="quantity">
              Quantity
            </option>
            <option value="unit_price">
              Unit Price
            </option>
            <option value="total_price">
              Total Price
            </option>
            <option value="region">
              Region
            </option>
            <option value="created_at">
              Created At
            </option>
          </select>
        </div>

        <div>
          <label
            htmlFor="sales-order"
            className="mb-1.5 block text-sm font-medium text-slate-700"
          >
            Order
          </label>

          <select
            id="sales-order"
            value={order}
            onChange={(event) =>
              setOrder(event.target.value)
            }
            className="w-full rounded-lg border border-slate-300 bg-white px-3 py-2 text-sm outline-none transition focus:border-slate-500 focus:ring-2 focus:ring-slate-200"
          >
            <option value="desc">
              Descending
            </option>
            <option value="asc">
              Ascending
            </option>
          </select>
        </div>

        <div className="flex items-end gap-2 md:col-span-2 xl:col-span-5">
          <button
            type="submit"
            className="rounded-lg bg-slate-900 px-5 py-2 text-sm font-medium text-white transition hover:bg-slate-800"
          >
            Apply
          </button>

          <button
            type="button"
            onClick={handleReset}
            className="rounded-lg border border-slate-300 px-5 py-2 text-sm font-medium text-slate-700 transition hover:bg-slate-50"
          >
            Reset
          </button>
        </div>
      </form>
    </div>
  );
}