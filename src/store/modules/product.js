import productService from "@/services/productService";

const state = {
  products: [],
};

const getters = {
  products: (state) => {
    return state.products;
  },
};

const actions = {
  getProducts({ commit }, params) {
    return new Promise((resolve, reject) => {
      productService
        .fetchProducts(params)
        .then((results) => {
          commit("setProducts", results);
          resolve();
        })
        .catch((err) => reject(err));
    });
  },

  addProduct({ commit }, result) {
    return new Promise((resolve, reject) => {
      productService
        .postProduct(result)
        .then(() => {
          resolve(result);
        })
        .catch((err) => reject(err));
    });
  },

  updateProduct({ commit }, data) {
    return new Promise((resolve, reject) => {
      productService
        .putProduct(data)
        .then(() => {
          resolve();
        })
        .catch((err) => reject(err));
    });
  },

  removeProduct({ commit }, data) {
    return new Promise((resolve, reject) => {
      productService
        .deleteProduct(data)
        .then(() => {
          resolve();
        })
        .catch((err) => reject(err));
    });
  },
};

const mutations = {
  setProducts(state, results) {
    state.products = results;
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
