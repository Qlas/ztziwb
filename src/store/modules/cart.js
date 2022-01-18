import cartService from "@/services/cartService";

const state = {
  cart: {},
  cartValue: 0,
  delivery: 20,
  deliverycartValue: 0,
};

const getters = {
  cart: (state) => {
    return state.cart;
  },
  cartValue: (state) => {
    return state.cartValue;
  },
  delivery: (state) => {
    return state.delivery;
  },
  deliverycartValue: (state) => {
    return state.deliverycartValue;
  },
};

const actions = {
  getCart({ commit }, params) {
    return new Promise((resolve, reject) => {
      cartService
        .fetchCart(params)
        .then((results) => {
          commit("setCart", results);
          resolve();
        })
        .catch((err) => reject(err));
    });
  },
  removeCartProduct({ commit }, data) {
    return new Promise((resolve, reject) => {
      cartService
        .deleteCartProduct(data)
        .then(() => {
          resolve();
        })
        .catch((err) => reject(err));
    });
  },

  changeProduct({ commit }, data) {
    return new Promise((resolve, reject) => {
      cartService
        .changeProductQuantity(data)
        .then(() => {
          resolve();
        })
        .catch((err) => reject(err));
    });
  },
};

const mutations = {
  setCart(state, results) {
    state.cart = results[0];
    var cartValue = 0;
    for (let result of results[0].cart_product) {
      cartValue += result.price * result.quantity;
    }
    if (cartValue > 300) {
      state.delivery = 0;
    } else {
      state.delivery = 20;
    }
    state.cartValue = cartValue.toFixed(2).replace(".", ",");
    state.deliverycartValue = state.delivery + cartValue;
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
