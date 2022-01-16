import contactFormService from "@/services/contactFormService";

const state = {
};

const getters = {
};

const actions = {

    sendForm({ commit }, result) {
        return new Promise((resolve, reject) => {
            contactFormService
                .postContactForm(result)
                .then(() => {
                    commit("sendForm", result);
                    resolve(result);
                })
                .catch((err) => reject(err));
        });
    },

};

const mutations = {
    sendForm(state, results) {
        return
    },
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
};
