import Vue from 'vue'
import Router from 'vue-router'
import VueMeta from 'vue-meta'
import Home from "@/views/Home";

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
  ]
})
