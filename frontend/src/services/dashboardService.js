import api from "./api";

export const dashboardService = {
  async getSummary(params = {}) {
    const response = await api.get("/dashboard/summary", {
      params,
    });

    return response.data;
  },

  async getCategory(params = {}) {
    const response = await api.get("/dashboard/category", {
      params,
    });

    return response.data;
  },

  async getRegion(params = {}) {
    const response = await api.get("/dashboard/region", {
      params,
    });

    return response.data;
  },

  async getMonthly(params = {}) {
    const response = await api.get("/dashboard/monthly", {
      params,
    });

    return response.data;
  },

  async getTopProducts(params = {}) {
    const response = await api.get("/dashboard/top-products", {
      params,
    });

    return response.data;
  },

  async getRecentSales(params = {}) {
    const response = await api.get("/dashboard/recent-sales", {
      params,
    });

    return response.data;
  },
};