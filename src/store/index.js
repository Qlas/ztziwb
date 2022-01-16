import Vue from 'vue'
import Vuex from 'vuex'
import auth from './modules/auth'
import contactForm from './modules/contactForm'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    auth,
    contactForm
  }
})