import { useState } from "react";

import {
  Database,
  PhilippinePeso,
  ShoppingCart,
  TrendingUp,
} from "lucide-react";

import ActivitySummary from "../components/dashboard/ActivitySummary";
import CategoryChart from "../components/dashboard/CategoryChart";
import DashboardFilters from "../components/dashboard/DashboardFilters";
import RecentSales from "../components/dashboard/RecentSales";
import RegionChart from "../components/dashboard/RegionChart";
import SalesTrendChart from "../components/dashboard/SalesTrendChart";
import StatCard from "../components/dashboard/StatCard";
import TopProducts from "../components/dashboard/TopProducts";

import {
  useDashboardCategory,
  useDashboardMonthly,
  useDashboardRecentSales,
  useDashboardRegion,
  useDashboardSummary,
  useDashboardTopProducts,
} from "../hooks/useDashboard";


function formatCurrency(value) {
  const number = Number(value ?? 0);

  return new Intl.NumberFormat("id-ID", {
    style: "currency",
    currency: "IDR",
    maximumFractionDigits: 0,
  }).format(number);
}


function formatNumber(value) {
  return new Intl.NumberFormat("id-ID").format(
    Number(value ?? 0),
  );
}


function DashboardLoading() {
  return (
    <section>
      <div>
        <span className="text-sm font-medium text-slate-500">
          Overview
        </span>

        <h1 className="mt-1 text-2xl font-bold text-slate-900">
          Dashboard
        </h1>

        <p className="mt-1 text-sm text-slate-500">
          Monitor your sales data and platform activity.
        </p>
      </div>

      <div className="mt-6 grid gap-4 md:grid-cols-2 xl:grid-cols-4">
        {[1, 2, 3, 4].map((item) => (
          <div
            key={item}
            className="h-36 animate-pulse rounded-xl border border-slate-200 bg-white"
          />
        ))}
      </div>
    </section>
  );
}


function DashboardError({ message }) {
  return (
    <section>
      <div className="rounded-xl border border-red-200 bg-red-50 p-6">
        <span className="text-sm font-medium text-red-500">
          Dashboard
        </span>

        <h1 className="mt-1 text-2xl font-bold text-slate-900">
          Unable to load dashboard
        </h1>

        <p className="mt-2 text-sm text-red-600">
          {message}
        </p>
      </div>
    </section>
  );
}


export default function DashboardPage() {
  const [filters, setFilters] = useState({});

  /*
   * Unfiltered queries are used to populate the filter options.
   *
   * When filters are empty, React Query will reuse the same
   * request because the query key is identical.
   */
  const categoryOptionsQuery = useDashboardCategory();
  const regionOptionsQuery = useDashboardRegion();

  /*
   * Dashboard data uses the currently applied filters.
   */
  const summaryQuery = useDashboardSummary(filters);
  const categoryQuery = useDashboardCategory(filters);
  const regionQuery = useDashboardRegion(filters);
  const monthlyQuery = useDashboardMonthly(filters);

  const recentSalesQuery = useDashboardRecentSales({
    ...filters,
    limit: 5,
  });

  const topProductsQuery = useDashboardTopProducts({
    ...filters,
    limit: 10,
  });


  const isLoading =
    summaryQuery.isLoading ||
    categoryQuery.isLoading ||
    regionQuery.isLoading ||
    monthlyQuery.isLoading ||
    recentSalesQuery.isLoading ||
    topProductsQuery.isLoading ||
    categoryOptionsQuery.isLoading ||
    regionOptionsQuery.isLoading;


  const isError =
    summaryQuery.isError ||
    categoryQuery.isError ||
    regionQuery.isError ||
    monthlyQuery.isError ||
    recentSalesQuery.isError ||
    topProductsQuery.isError ||
    categoryOptionsQuery.isError ||
    regionOptionsQuery.isError;


  if (isLoading) {
    return <DashboardLoading />;
  }


  if (isError) {
    const error =
      summaryQuery.error ||
      categoryQuery.error ||
      regionQuery.error ||
      monthlyQuery.error ||
      recentSalesQuery.error ||
      topProductsQuery.error ||
      categoryOptionsQuery.error ||
      regionOptionsQuery.error;

    return (
      <DashboardError
        message={
          error?.response?.data?.detail ||
          error?.message ||
          "An unexpected error occurred while loading dashboard data."
        }
      />
    );
  }


  const summary = summaryQuery.data ?? {};

  /*
   * Backend returns objects such as:
   *
   * {
   *   category: "Electronics",
   *   total_revenue: ...,
   *   total_quantity: ...
   * }
   *
   * We only need the category/region names for the filter options.
   */
  const categories = categoryOptionsQuery.data
    ?.map((item) => item.category)
    .filter(Boolean) ?? [];

  const regions = regionOptionsQuery.data
    ?.map((item) => item.region)
    .filter(Boolean) ?? [];


  return (
    <section>
      <div>
        <span className="text-sm font-medium text-slate-500">
          Overview
        </span>

        <h1 className="mt-1 text-2xl font-bold text-slate-900">
          Dashboard
        </h1>

        <p className="mt-1 text-sm text-slate-500">
          Monitor your sales data and platform activity.
        </p>
      </div>


      <div className="mt-6">
        <DashboardFilters
          categories={categories}
          regions={regions}
          filters={filters}
          onApply={setFilters}
          onReset={() => setFilters({})}
        />
      </div>


      <div className="mt-6 grid gap-4 md:grid-cols-2 xl:grid-cols-4">
        <StatCard
          title="Total Revenue"
          value={formatCurrency(summary.total_revenue)}
          description="Total sales revenue"
          trend={0}
          trendLabel="Current period"
          icon={PhilippinePeso}
        />

        <StatCard
          title="Total Orders"
          value={formatNumber(summary.total_orders)}
          description="Sales orders"
          trend={0}
          trendLabel="Current period"
          icon={ShoppingCart}
        />

        <StatCard
          title="Total Quantity"
          value={formatNumber(summary.total_quantity)}
          description="Units sold"
          trend={0}
          trendLabel="Current period"
          icon={Database}
        />

        <StatCard
          title="Average Order Value"
          value={formatCurrency(summary.average_order_value)}
          description="Average revenue per order"
          trend={0}
          trendLabel="Current period"
          icon={TrendingUp}
        />
      </div>


      <div className="mt-6 grid gap-6 xl:grid-cols-3">
        <div className="xl:col-span-2">
          <SalesTrendChart
            data={monthlyQuery.data ?? []}
          />
        </div>

        <CategoryChart
          data={categoryQuery.data ?? []}
        />
      </div>


      <div className="mt-6">
        <RegionChart
          data={regionQuery.data ?? []}
        />
      </div>


      <div className="mt-6">
        <RecentSales
          data={recentSalesQuery.data ?? []}
          isLoading={recentSalesQuery.isLoading}
        />
      </div>


      <div className="mt-6">
        <TopProducts
          data={topProductsQuery.data ?? []}
        />
      </div>


      <div className="mt-6">
        <ActivitySummary />
      </div>
    </section>
  );
}