import { api } from "@/services/api";

export default {
  fetchProducts(params) {
    return api.get(`product/`, { params }).then((response) => response.data);
  },
  postProduct(payload) {
    return api.post(`product/`, payload).then((response) => response.data);
  },
  putProduct(update) {
    return api
      .put(`product/${update.update.productId}/`, update.update.payload)
      .then((response) => response.data);
  },
  deleteProduct(productId) {
    return api
      .delete(`product/${productId}/`)
      .then((response) => response.data);
  },
};
