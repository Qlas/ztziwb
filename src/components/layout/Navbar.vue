<template>
  <b-navbar
    class="is-spaced has-shadow mb-2"
    type="is-primary"
    wrapper-class="container"
  >
    <template slot="brand">
      <b-navbar-item :to="{ path: '/' }" tag="router-link">
        <b-icon :style="{ margin: '6px' }" icon="clover"></b-icon>
        <transition name="slide-left">
          <p
            v-if="$route.path !== '/'"
            class="subtitle is-5 is-unselectable has-spacing no-wrap"
            style="color: white"
          >
            Dzianiny24
          </p>
        </transition>
      </b-navbar-item>
    </template>
    <template slot="start">
      <b-navbar-item :to="{ path: '/o-nas' }" tag="router-link">
        <b-icon :style="{ margin: '6px' }" icon="information-outline" />
        <p class="is-unselectable">O nas</p>
      </b-navbar-item>
      <b-navbar-item :to="{ path: '/kontakt' }" tag="router-link">
        <b-icon :style="{ margin: '6px' }" icon="message-text-outline" />
        <p class="is-unselectable">Kontakt</p>
      </b-navbar-item>
      <b-navbar-item :to="{ path: '/sklep' }" tag="router-link">
        <b-icon :style="{ margin: '6px' }" icon="basket-outline" />
        <p class="is-unselectable">Sklep</p>
      </b-navbar-item>
      <b-navbar-dropdown
        label="Zarządzanie"
        v-if="
          isAuthenticated &&
          ($permissions.product.any(authUser) ||
            $permissions.category.any(authUser))
        "
      >
        <b-navbar-item :to="{ path: '/zarzadzanie/produkt' }" tag="router-link">
          <b-icon :style="{ margin: '6px' }" icon="basket-outline" />
          <p class="is-unselectable">Produkt</p>
        </b-navbar-item>
        <b-navbar-item
          :to="{ path: '/zarzadzanie/kategoria' }"
          tag="router-link"
        >
          <b-icon :style="{ margin: '6px' }" icon="basket-outline" />
          <p class="is-unselectable">Kategoria</p>
        </b-navbar-item>
      </b-navbar-dropdown>
    </template>

    <template slot="end">
      <b-navbar-dropdown arrowless style="color: black" v-if="isAuthenticated">
        <div class="modal-card">
          <header class="modal-card-head">
            <p class="modal-card-title has-text-centered">Twój koszyk</p>
          </header>
          <section class="modal-card-body">
            <div
              class="has-text-centered"
              v-if="
                cart === undefined ||
                (cart.cart_product !== undefined &&
                  cart.cart_product.length == 0)
              "
            >
              Twój koszyk jest pusty
            </div>
            <div v-else>
              <div
                v-for="cart_product in cart.cart_product"
                :key="cart_product.id"
                class="box"
              >
                <router-link :to="'/szczegoly/' + cart_product.product">
                  <div>
                    <div class="columns">
                      <div
                        class="column is-2"
                        style="display: flex; align-items: center"
                      >
                        <figure class="image">
                          <img
                            :src="cart_product.image"
                            alt="Placeholder image"
                          />
                        </figure>
                      </div>
                      <div
                        class="column"
                        style="display: flex; align-items: center"
                      >
                        <p class="title is-6">{{ cart_product.product }}</p>
                      </div>
                      <div
                        class="column is-2"
                        style="display: flex; align-items: center"
                      >
                        <p class="title is-6">{{ cart_product.quantity }}</p>
                      </div>
                      <div
                        class="column is-2"
                        style="display: flex; align-items: center"
                      >
                        <b-button
                          @click="
                            () => removeButtonClicked(cart_product.product)
                          "
                          >Usuń</b-button
                        >
                      </div>
                    </div>
                  </div>
                </router-link>
              </div>
            </div>
            <b-button class="is-secondary mt-4" tag="router-link" to="/koszyk"
              >Przejdź do koszyka</b-button
            >
          </section>
        </div>

        <template slot="label">Koszyk: {{ padInt(cartValue) }}</template>
      </b-navbar-dropdown>
      <b-dropdown :triggers="['hover']" v-if="isAuthenticated">
        <button class="button is-primary" slot="trigger">
          <b-icon icon="account"></b-icon>
          {{ authUser.username }}
          <b-icon icon="menu-down"></b-icon>
        </button>

        <b-dropdown-item aria-role="listitem" @click="logout">
          <div class="media">
            <b-icon class="media-left" icon="account-cancel"></b-icon>
            <div class="media-content">
              <p>Logout</p>
            </div>
          </div>
        </b-dropdown-item>
      </b-dropdown>
      <b-navbar-item v-else tag="div">
        <div class="buttons">
          <b-button tag="router-link" to="/logowanie" type="is-secondary">
            <strong>Zaloguj się</strong>
          </b-button>

          <b-button tag="router-link" to="/rejestracja" type="is-dark">
            <strong>Rejestracja</strong>
          </b-button>
        </div>
      </b-navbar-item>
    </template>
  </b-navbar>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import { NotificationProgrammatic as Notification } from "buefy";

export default {
  name: "Navbar",

  computed: {
    ...mapGetters("auth", ["isAuthenticated", "authUser"]),
    ...mapGetters("cart", ["cartValue", "cart"]),
  },

  methods: {
    ...mapActions("auth", ["endAuthSession"]),
    ...mapActions("cart", ["getCart", "removeCartProduct"]),

    logout() {
      this.endAuthSession();
      if (this.$route.path != "/") {
        this.$router.push("/");
      }
      Notification.open({
        message: "Logout complete",
        type: "is-success",
        hasIcon: true,
      });
    },

    removeButtonClicked(product) {
      this.removeCartProduct({
        id: this.cart.id,
        payload: { product: product },
      }).then(() => {
        this.getCart();
      });
    },

    padInt(value) {
      return value.toString() + " zł";
    },
  },

  created() {
    this.getCart();
  },
};
</script>

<style scoped lang="scss">
@keyframes slideLeftIn {
  0% {
    opacity: 0;
    transform: translateX(-1rem);
    max-width: 0px;
  }
  100% {
    opacity: 1;
    transform: translateX(0);
    max-width: 120px;
  }
}
@keyframes slideLeftOut {
  0% {
    opacity: 1;
    transform: translateX(0);
    max-width: 120px;
  }
  100% {
    opacity: 0;
    transform: translateX(-1rem);
    max-width: 0px;
  }
}
//Animation: Slide left
.slide-left-enter-active {
  animation: slideLeftIn 0.4s ease-out;
}
.slide-left-leave-active {
  animation: slideLeftOut 0.4s ease-in;
}
.slide-left-enter,
.slide-left-leave-to {
  opacity: 0;
  max-width: 0px;
  transform: translateX(-1rem);
}
.slide-left-leave,
.slide-left-enter-to {
  opacity: 1;
  max-width: 120px;
  transform: translateX(0);
}
.no-wrap {
  white-space: nowrap;
}
.navbar.has-shadow {
  box-shadow: 0px 1px 0px hsla(0, 0%, 100%, 0.2);
}
</style>
