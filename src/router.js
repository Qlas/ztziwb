import Vue from "vue";
import Router from "vue-router";
import VueMeta from "vue-meta";
import Home from "@/views/Home";
import About from "@/views/About";
import Contact from "@/views/Contact";
import Login from "@/views/Login";
import Register from "@/views/Register";
import Shop from "@/views/Shop";
import Manage from "@/views/Manage";
import ManageCategory from "@/views/ManageCategory";
import productDetails from "@/views/productDetails";

Vue.use(Router);
Vue.use(VueMeta);

export default new Router({
  routes: [
    {
      path: "/",
      name: "home",
      component: Home,
      meta: {
        requiresAuth: false,
        requiresNoAuth: false,
        canBeOnFooter: false,
      },
    },
    {
      path: "/o-nas",
      name: "O nas",
      component: About,
      meta: { requiresAuth: false, requiresNoAuth: false, canBeOnFooter: true },
    },
    {
      path: "/kontakt",
      name: "Kontakt",
      component: Contact,
      meta: { requiresAuth: false, requiresNoAuth: false, canBeOnFooter: true },
    },
    {
      path: "/sklep",
      name: "Sklep",
      component: Shop,
      meta: { requiresAuth: false, requiresNoAuth: false, canBeOnFooter: true },
    },
    {
      path: "/zarzadzanie/produkt",
      name: "Zarzadzanie Produktem",
      component: Manage,
      meta: { requiresAuth: true, requiresNoAuth: false, canBeOnFooter: false },
    },
    {
      path: "/zarzadzanie/kategoria",
      name: "Zarzadzanie Kategorią",
      component: ManageCategory,
      meta: { requiresAuth: true, requiresNoAuth: false, canBeOnFooter: false },
    },
    {
      path: "/logowanie",
      name: "Logowanie",
      component: Login,
      meta: { requiresAuth: false, requiresNoAuth: true, canBeOnFooter: true },
    },
    {
      path: "/rejestracja",
      name: "rejestracja",
      component: Register,
      meta: { requiresAuth: false, requiresNoAuth: true, canBeOnFooter: true },
    },
    {
      path: "/szczegoly/:name",
      name: "szczegoly",
      component: productDetails,
      meta: { requiresAuth: true, requiresNoAuth: false, canBeOnFooter: false },
    },
  ],
});
