import Vue from "vue";
import App from "@/App.vue";
import permissionUtils from "@/utils/permissionUtils";
import Buefy from "buefy";
import store from "@/store";
import router from "@/router";
import errorHandler from "@/error";
import "./validation/rules";
import { ValidationProvider, ValidationObserver } from "vee-validate";
import ValidatedInput from "@/components/customInputs/validatedInput";
import ValidatedSelect from "@/components/customInputs/ValidatedSelect";
Vue.config.productionTip = false;

// Vue.use(VueRouter)
Vue.use(Buefy);
Vue.component("ValidationProvider", ValidationProvider);
Vue.component("ValidationObserver", ValidationObserver);
Vue.component(ValidatedInput.name, ValidatedInput);
Vue.component(ValidatedSelect.name, ValidatedSelect);
Vue.prototype.$permissions = permissionUtils;
Vue.prototype.$errorHandler = errorHandler;

// handle auth when user open / refresh the app
if (store.getters["auth/isAuthenticated"]) {
  store.dispatch("auth/setAxiosHeaders");
  if (store.getters["auth/isAccessTokenExpired"]) {
    store.dispatch("auth/endAuthSession", true);
    router.push("/login");
  } else {
    store
      .dispatch("auth/refreshAccessToken")
      .then(() => {
        store.dispatch("auth/startTokenRefreshCounter");
      })
      .catch(() => {
        Notification.open({
          duration: 8000,
          message: `Refresh auth error. This should have never happened. Please sign in again. Please report this to administrator.`,
          position: "is-top-right",
          type: "is-danger",
          hasIcon: true,
        });
        store.dispatch("auth/endAuthSession");
        router.push("/login");
      });
  }
}

const vue = new Vue({
  router,
  store,
  render: (h) => h(App),
});

vue.$mount("#app");
