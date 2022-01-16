import { api } from "@/services/api";

export default {
    postContactForm(payload) {
        return api.post(`contact_form/`, payload).then((response) => response.data);
    },
};
