import Vue from "vue";
import Vuex from "vuex";
import auth from "./modules/auth";
import contactForm from "./modules/contactForm";
import menu from "./modules/menu";
import product from "./modules/product";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,
    contactForm,
    menu,
    product,
  },
});
