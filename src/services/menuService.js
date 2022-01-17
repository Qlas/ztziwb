import { api } from "@/services/api";

export default {
  fetchCategories(payload) {
    return api.get(`category/`, payload).then((response) => response.data);
  },
};
