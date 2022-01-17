import { api } from "@/services/api";

export default {
  fetchProducts(params) {
    return api.get(`product/`, { params }).then((response) => response.data);
  },
};
