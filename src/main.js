import Vue from 'vue'
import App from '@/App.vue'
import permissionUtils from "@/utils/permissionUtils";
import Buefy from "buefy";
import store from '@/store'
import router from '@/router'
import "./validation/rules";
import { ValidationProvider, ValidationObserver } from "vee-validate";
import ValidatedInput from "@/components/customInputs/validatedInput";
import ValidatedSelect from "@/components/customInputs/ValidatedSelect";
Vue.config.productionTip = false

// Vue.use(VueRouter)
Vue.use(Buefy);
Vue.component("ValidationProvider", ValidationProvider);
Vue.component("ValidationObserver", ValidationObserver);
Vue.component(ValidatedInput.name, ValidatedInput);
Vue.component(ValidatedSelect.name, ValidatedSelect);
Vue.prototype.$permissions = permissionUtils;


const vue = new Vue({
  router,
  store,
  render: h => h(App)
})

vue.$mount('#app')
