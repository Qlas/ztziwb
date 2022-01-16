import Vue from 'vue'
import Router from 'vue-router'
import VueMeta from 'vue-meta'
import Home from "@/views/Home";
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
      path: "/login",
      name: "Login",
      component: Login,
      meta: { requiresAuth: false, requiresNoAuth: true, canBeOnFooter: false },
    },
  ]
})
