import { useMemo, useState } from "react";

import SalesEditModal from "../components/sales/SalesEditModal";
import SalesFilters from "../components/sales/SalesFilters";
import SalesPagination from "../components/sales/SalesPagination";
import SalesTable from "../components/sales/SalesTable";
import SalesViewModal from "../components/sales/SalesViewModal";

import {
  useDeleteSale,
  useSales,
  useSale,
  useUpdateSale,
} from "../hooks/useSales";

const DEFAULT_FILTERS = {
  search: "",
  category: "",
  region: "",
  sort_by: "order_date",
  order: "desc",
};

const DEFAULT_PAGE = 1;
const DEFAULT_LIMIT = 20;

function SalesLoading() {
  return (
    <section>
      <div>
        <p className="text-sm font-medium text-slate-400">
          Management
        </p>

        <h1 className="mt-1 text-2xl font-bold text-slate-900">
          Sales
        </h1>

        <p className="mt-1 text-sm text-slate-500">
          Manage and analyze sales records.
        </p>
      </div>

      <div className="mt-6 space-y-6">
        <div className="h-48 animate-pulse rounded-xl border border-slate-200 bg-white" />

        <div className="h-96 animate-pulse rounded-xl border border-slate-200 bg-white" />
      </div>
    </section>
  );
}

function SalesError({ message }) {
  return (
    <section>
      <div>
        <p className="text-sm font-medium text-slate-400">
          Management
        </p>

        <h1 className="mt-1 text-2xl font-bold text-slate-900">
          Sales
        </h1>

        <p className="mt-1 text-sm text-slate-500">
          Manage and analyze sales records.
        </p>
      </div>

      <div className="mt-6 rounded-xl border border-red-200 bg-red-50 p-5">
        <h2 className="font-semibold text-red-800">
          Unable to load sales data
        </h2>

        <p className="mt-1 text-sm text-red-600">
          {message}
        </p>
      </div>
    </section>
  );
}

export default function SalesPage() {
  const [filters, setFilters] = useState(DEFAULT_FILTERS);
  const [page, setPage] = useState(DEFAULT_PAGE);
  const [selectedSaleId, setSelectedSaleId] = useState(null);
  const [editSale, setEditSale] = useState(null);

  const queryParams = useMemo(
    () => ({
      page,
      limit: DEFAULT_LIMIT,
      search: filters.search || undefined,
      category: filters.category || undefined,
      region: filters.region || undefined,
      sort_by: filters.sort_by,
      order: filters.order,
    }),
    [page, filters],
  );

  const salesQuery = useSales(queryParams);

  const saleDetailQuery = useSale(selectedSaleId);

  const updateMutation = useUpdateSale();
  const deleteMutation = useDeleteSale();

  function handleApply(nextFilters) {
    setFilters({
      ...DEFAULT_FILTERS,
      ...nextFilters,
    });

    setPage(DEFAULT_PAGE);
  }

  function handleReset() {
    setFilters(DEFAULT_FILTERS);
    setPage(DEFAULT_PAGE);
  }

  function handlePageChange(nextPage) {
    setPage(nextPage);
  }

  function handleView(sale) {
    setSelectedSaleId(sale.id);
  }

  function handleEdit(sale) {
    setEditSale(sale);
  }

  async function handleDelete(sale) {
    const confirmed = window.confirm(
      `Are you sure you want to delete "${sale.invoice_number}"?`,
    );

    if (!confirmed) {
      return;
    }

    try {
      await deleteMutation.mutateAsync(sale.id);
    } catch (error) {
      window.alert(
        error?.response?.data?.detail ||
          "Failed to delete sales record.",
      );
    }
  }

  function handleCloseView() {
    setSelectedSaleId(null);
  }

  function handleCloseEdit() {
    if (updateMutation.isPending) {
      return;
    }

    setEditSale(null);
  }

  async function handleUpdate(data) {
    if (!editSale) {
      return;
    }

    try {
      await updateMutation.mutateAsync({
        saleId: editSale.id,
        data,
      });

      setEditSale(null);
    } catch (error) {
      window.alert(
        error?.response?.data?.detail ||
          "Failed to update sales record.",
      );
    }
  }

  if (salesQuery.isLoading) {
    return <SalesLoading />;
  }

  if (salesQuery.isError) {
    return (
      <SalesError
        message={
          salesQuery.error?.response?.data?.detail ||
          salesQuery.error?.message ||
          "An unexpected error occurred while loading sales data."
        }
      />
    );
  }

  const response = salesQuery.data ?? {};
  const sales = response.items ?? [];
  const pagination = response.pagination ?? null;
  const detailSale = saleDetailQuery.data;

  return (
    <section>
      <div>
        <p className="text-sm font-medium text-slate-400">
          Management
        </p>

        <h1 className="mt-1 text-2xl font-bold text-slate-900">
          Sales
        </h1>

        <p className="mt-1 text-sm text-slate-500">
          Manage and analyze sales records.
        </p>
      </div>

      <div className="mt-6 space-y-6">
        <SalesFilters
          filters={filters}
          onApply={handleApply}
          onReset={handleReset}
        />

        <SalesTable
          data={sales}
          isLoading={salesQuery.isFetching}
          onView={handleView}
          onEdit={handleEdit}
          onDelete={handleDelete}
        />

        <SalesPagination
          pagination={pagination}
          onPageChange={handlePageChange}
        />
      </div>

      {selectedSaleId && (
        <SalesViewModal
          sale={detailSale}
          isLoading={saleDetailQuery.isLoading}
          onClose={handleCloseView}
        />
      )}

      {editSale && (
        <SalesEditModal
          sale={editSale}
          onClose={handleCloseEdit}
          onSave={handleUpdate}
          isLoading={updateMutation.isPending}
        />
      )}
    </section>
  );
}