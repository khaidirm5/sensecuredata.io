import api from "./api";

export const authService = {
  async login(email, password) {
    const formData = new URLSearchParams();

    formData.append("username", email);
    formData.append("password", password);

    const response = await api.post("/auth/login", formData, {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    });

    const { access_token, refresh_token } = response.data;

    localStorage.setItem("access_token", access_token);
    localStorage.setItem("refresh_token", refresh_token);

    return response.data;
  },

  async getMe() {
    const response = await api.get("/auth/me");

    return response.data;
  },

  async refresh(refreshToken) {
    const response = await api.post("/auth/refresh", {
      refresh_token: refreshToken,
    });

    localStorage.setItem(
      "access_token",
      response.data.access_token,
    );

    return response.data;
  },

  async logout() {
    try {
      await api.post("/auth/logout");
    } finally {
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");
    }
  },

  clearTokens() {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
  },
};