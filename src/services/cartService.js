import { api } from "@/services/api";

export default {
  fetchCart(params) {
    return api.get(`cart/`, { params }).then((response) => response.data);
  },
  deleteCartProduct(data) {
    return api
      .patch(`cart/${data.id}/remove_item/`, data.payload)
      .then((response) => response.data);
  },
  changeProductQuantity(data) {
    return api
      .patch(`cart/${data.id}/change_product_quantity/`, data.payload)
      .then((response) => response.data);
  },
};
