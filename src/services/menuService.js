import { api } from "@/services/api";

export default {
  fetchCategories(params) {
    return api.get(`category/`, { params }).then((response) => response.data);
  },
  postCategory(payload) {
    return api.post(`category/`, payload).then((response) => response.data);
  },
};
