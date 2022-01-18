import { api } from "@/services/api";

export default {
  postCartProduct(payload) {
    return api.post(`cart-product/`, payload).then((response) => response.data);
  },
};
