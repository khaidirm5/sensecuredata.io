import { useQuery } from "@tanstack/react-query";

import { dashboardService } from "../services/dashboardService";

export function useDashboardSummary(params = {}) {
  return useQuery({
    queryKey: ["dashboard", "summary", params],
    queryFn: () => dashboardService.getSummary(params),
  });
}

export function useDashboardCategory(params = {}) {
  return useQuery({
    queryKey: ["dashboard", "category", params],
    queryFn: () => dashboardService.getCategory(params),
  });
}

export function useDashboardRegion(params = {}) {
  return useQuery({
    queryKey: ["dashboard", "region", params],
    queryFn: () => dashboardService.getRegion(params),
  });
}

export function useDashboardMonthly(params = {}) {
  return useQuery({
    queryKey: ["dashboard", "monthly", params],
    queryFn: () => dashboardService.getMonthly(params),
  });
}

export function useDashboardTopProducts(params = {}) {
  return useQuery({
    queryKey: ["dashboard", "top-products", params],
    queryFn: () => dashboardService.getTopProducts(params),
  });
}

export function useDashboardRecentSales(params = {}) {
  return useQuery({
    queryKey: ["dashboard", "recent-sales", params],
    queryFn: () => dashboardService.getRecentSales(params),
  });
}