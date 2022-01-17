import { api } from "@/services/api";

export default {
  fetchCategories(params) {
    return api.get(`category/`, { params }).then((response) => response.data);
  },
};
