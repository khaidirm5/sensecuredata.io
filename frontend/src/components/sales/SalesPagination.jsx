export default function SalesPagination({
  pagination,
  onPageChange,
}) {
  if (!pagination) {
    return null;
  }

  const {
    page,
    total,
    total_pages: totalPages,
    has_next: hasNext,
    has_previous: hasPrevious,
  } = pagination;

  if (total === 0) {
    return null;
  }

  return (
    <div className="flex flex-col gap-3 rounded-xl border border-slate-200 bg-white px-5 py-4 shadow-sm sm:flex-row sm:items-center sm:justify-between">
      <p className="text-sm text-slate-500">
        Page{" "}
        <span className="font-medium text-slate-700">
          {page}
        </span>{" "}
        of{" "}
        <span className="font-medium text-slate-700">
          {totalPages}
        </span>{" "}
        ·{" "}
        <span className="font-medium text-slate-700">
          {total}
        </span>{" "}
        records
      </p>

      <div className="flex gap-2">
        <button
          type="button"
          disabled={!hasPrevious}
          onClick={() => onPageChange(page - 1)}
          className="rounded-lg border border-slate-300 px-4 py-2 text-sm font-medium text-slate-700 transition hover:bg-slate-50 disabled:cursor-not-allowed disabled:opacity-40"
        >
          Previous
        </button>

        <button
          type="button"
          disabled={!hasNext}
          onClick={() => onPageChange(page + 1)}
          className="rounded-lg border border-slate-300 px-4 py-2 text-sm font-medium text-slate-700 transition hover:bg-slate-50 disabled:cursor-not-allowed disabled:opacity-40"
        >
          Next
        </button>
      </div>
    </div>
  );
}