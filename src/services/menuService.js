import { api } from "@/services/api";

export default {
  fetchCategories(params) {
    return api.get(`category/`, { params }).then((response) => response.data);
  },
  postCategory(payload) {
    return api.post(`category/`, payload).then((response) => response.data);
  },
  putCategory(update) {
    return api
      .put(`category/${update.update.categoryId}/`, update.update.payload)
      .then((response) => response.data);
  },
  deleteCategory(categoryId) {
    return api
      .delete(`category/${categoryId}/`)
      .then((response) => response.data);
  },
};
