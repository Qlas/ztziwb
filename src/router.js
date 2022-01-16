import Vue from 'vue'
import Router from 'vue-router'
import VueMeta from 'vue-meta'
import Home from "@/views/Home";
import About from "@/views/About";
import Contact from "@/views/Contact";
import Login from "@/views/Login";

Vue.use(Router)
Vue.use(VueMeta)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      meta: { requiresAuth: false, requiresNoAuth: false, canBeOnFooter: false },
    },
    {
      path: '/o-nas',
      name: 'O nas',
      component: About,
      meta: { requiresAuth: false, requiresNoAuth: false, canBeOnFooter: true },
    },
    {
      path: '/kontakt',
      name: 'Kontakt',
      component: Contact,
      meta: { requiresAuth: false, requiresNoAuth: false, canBeOnFooter: true },
    },
    {
      path: "/logowanie",
      name: "Logowanie",
      component: Login,
      meta: { requiresAuth: false, requiresNoAuth: true, canBeOnFooter: true },
    },
  ]
})
