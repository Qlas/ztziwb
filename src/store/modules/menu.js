import menuService from "@/services/menuService";

const state = {
  categories: [],
  activeMenu: "",
};

const getters = {
  categories: (state) => {
    return state.categories;
  },
  activeMenu: (state) => {
    return state.activeMenu;
  },
};

const actions = {
  getCategories({ commit }, params) {
    return new Promise((resolve, reject) => {
      menuService
        .fetchCategories(params)
        .then((results) => {
          commit("setCategories", results);
          resolve();
        })
        .catch((err) => reject(err));
    });
  },

  addCategory({ commit }, result) {
    return new Promise((resolve, reject) => {
      menuService
        .postCategory(result)
        .then(() => {
          resolve(result);
        })
        .catch((err) => reject(err));
    });
  },

  updateCategory({ commit }, data) {
    return new Promise((resolve, reject) => {
      menuService
        .putCategory(data)
        .then(() => {
          resolve();
        })
        .catch((err) => reject(err));
    });
  },

  removeCategory({ commit }, data) {
    return new Promise((resolve, reject) => {
      menuService
        .deleteCategory(data)
        .then(() => {
          resolve();
        })
        .catch((err) => reject(err));
    });
  },
};

const mutations = {
  setCategories(state, results) {
    state.categories = results;
  },
  setActiveMenu(state, value) {
    state.activeMenu = value;
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
