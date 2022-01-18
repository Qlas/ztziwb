import cartProductService from "@/services/cartProductService";

const state = {};

const getters = {};

const actions = {
  addProductToCart({ commit }, result) {
    return new Promise((resolve, reject) => {
      cartProductService
        .postCartProduct(result)
        .then(() => {
          resolve(result);
        })
        .catch((err) => reject(err));
    });
  },
};

const mutations = {};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
