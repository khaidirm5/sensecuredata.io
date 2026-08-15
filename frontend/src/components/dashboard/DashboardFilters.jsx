import { useState } from "react";

export default function DashboardFilters({
  categories = [],
  regions = [],
  filters = {},
  onApply,
  onReset,
}) {
  const [startDate, setStartDate] = useState(
    filters.start_date ?? "",
  );

  const [endDate, setEndDate] = useState(
    filters.end_date ?? "",
  );

  const [category, setCategory] = useState(
    filters.category ?? "",
  );

  const [region, setRegion] = useState(
    filters.region ?? "",
  );


  function handleSubmit(event) {
    event.preventDefault();

    onApply({
      start_date: startDate || undefined,
      end_date: endDate || undefined,
      category: category || undefined,
      region: region || undefined,
    });
  }


  function handleReset() {
    setStartDate("");
    setEndDate("");
    setCategory("");
    setRegion("");

    onReset();
  }


  return (
    <div className="rounded-xl border border-slate-200 bg-white p-5">
      <div>
        <h2 className="text-base font-semibold text-slate-900">
          Dashboard Filters
        </h2>

        <p className="mt-1 text-sm text-slate-500">
          Filter dashboard data by date, category, and region.
        </p>
      </div>


      <form
        onSubmit={handleSubmit}
        className="mt-5 grid gap-4 md:grid-cols-2 xl:grid-cols-5"
      >
        <div>
          <label
            htmlFor="dashboard-start-date"
            className="mb-1.5 block text-sm font-medium text-slate-700"
          >
            Start Date
          </label>

          <input
            id="dashboard-start-date"
            type="date"
            value={startDate}
            onChange={(event) =>
              setStartDate(event.target.value)
            }
            className="w-full rounded-lg border border-slate-300 px-3 py-2 text-sm outline-none transition focus:border-slate-500 focus:ring-2 focus:ring-slate-200"
          />
        </div>


        <div>
          <label
            htmlFor="dashboard-end-date"
            className="mb-1.5 block text-sm font-medium text-slate-700"
          >
            End Date
          </label>

          <input
            id="dashboard-end-date"
            type="date"
            value={endDate}
            onChange={(event) =>
              setEndDate(event.target.value)
            }
            className="w-full rounded-lg border border-slate-300 px-3 py-2 text-sm outline-none transition focus:border-slate-500 focus:ring-2 focus:ring-slate-200"
          />
        </div>


        <div>
          <label
            htmlFor="dashboard-category"
            className="mb-1.5 block text-sm font-medium text-slate-700"
          >
            Category
          </label>

          <select
            id="dashboard-category"
            value={category}
            onChange={(event) =>
              setCategory(event.target.value)
            }
            className="w-full rounded-lg border border-slate-300 bg-white px-3 py-2 text-sm outline-none transition focus:border-slate-500 focus:ring-2 focus:ring-slate-200"
          >
            <option value="">
              All Categories
            </option>

            {categories.map((item) => (
              <option key={item} value={item}>
                {item}
              </option>
            ))}
          </select>
        </div>


        <div>
          <label
            htmlFor="dashboard-region"
            className="mb-1.5 block text-sm font-medium text-slate-700"
          >
            Region
          </label>

          <select
            id="dashboard-region"
            value={region}
            onChange={(event) =>
              setRegion(event.target.value)
            }
            className="w-full rounded-lg border border-slate-300 bg-white px-3 py-2 text-sm outline-none transition focus:border-slate-500 focus:ring-2 focus:ring-slate-200"
          >
            <option value="">
              All Regions
            </option>

            {regions.map((item) => (
              <option key={item} value={item}>
                {item}
              </option>
            ))}
          </select>
        </div>


        <div className="flex items-end gap-2">
          <button
            type="submit"
            className="flex-1 rounded-lg bg-slate-900 px-4 py-2 text-sm font-medium text-white transition hover:bg-slate-800"
          >
            Apply
          </button>

          <button
            type="button"
            onClick={handleReset}
            className="rounded-lg border border-slate-300 px-4 py-2 text-sm font-medium text-slate-700 transition hover:bg-slate-50"
          >
            Reset
          </button>
        </div>
      </form>
    </div>
  );
}