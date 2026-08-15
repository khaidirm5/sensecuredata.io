import api from "./api";

export const salesService = {
  async getSales(params = {}) {
    const response = await api.get("/sales/", {
      params,
    });

    return response.data;
  },

  async getSale(saleId) {
    const response = await api.get(`/sales/${saleId}`);

    return response.data;
  },

  async createSale(data) {
    const response = await api.post("/sales/", data);

    return response.data;
  },

  async updateSale(saleId, data) {
    const response = await api.put(
      `/sales/${saleId}`,
      data,
    );

    return response.data;
  },

  async deleteSale(saleId) {
    await api.delete(`/sales/${saleId}`);
  },

  async uploadSales(file) {
    const formData = new FormData();

    formData.append("file", file);

    const response = await api.post(
      "/sales/upload",
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      },
    );

    return response.data;
  },
};