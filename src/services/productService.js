import { api } from "@/services/api";

export default {
  fetchProducts(params) {
    return api.get(`product/`, { params }).then((response) => response.data);
  },
  postProduct(payload) {
    return api.post(`product/`, payload).then((response) => response.data);
  },
};
