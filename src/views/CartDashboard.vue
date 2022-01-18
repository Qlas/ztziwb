<template>
  <div class="tl-reservation-dashboard container">
    <div
      class="card columns mt-1"
      v-for="cart_product in cart.cart_product"
      :key="cart_product.id"
    >
      <div class="column is-7">
        <div class="card-content">
          <div class="media">
            <div class="media-left">
              <img
                :src="
                  cart_product.image
                    ? cart_product.image
                    : 'https://e-pasmanteria.pl/environment/cache/images/0_0_productGfx_21861.jpg'
                "
                alt="Placeholder image"
                style="height: 100px"
              />
            </div>
            <div class="media-content">
              <p class="title is-4">{{ cart_product.product }}</p>
              <p class="subtitle is-6">{{ padInt(cart_product.price) }}</p>
            </div>
          </div>
        </div>
      </div>

      <div class="column" style="display: flex; align-items: center">
        <b-numberinput
          @input="
            (quantity) =>
              valueChanged(cart_product.product, quantity, cart_product)
          "
          controls-position="compact"
          min="1"
          :max="cart_product.max_quantity"
          v-model="cart_product.quantity"
          style="width: 150px"
        />
      </div>
      <div
        class="column"
        style="display: flex; align-items: center; padding-bottom: 35px"
      >
        <p class="title is-4">
          {{ padInt(cart_product.quantity * cart_product.price) }}
        </p>
      </div>
      <div
        class="column is-1"
        style="display: flex; align-items: center; padding-bottom: 25px"
      >
        <b-button @click="() => removeButtonClicked(cart_product.product)"
          >Usuń</b-button
        >
      </div>
    </div>
    <div class="columns card mt-1">
      <div class="box column">
        <div class="title has-text-centered">Szczegóły zamówienia</div>
        <div class="panel-block is-justify-content-space-between">
          <div class="is-pulled-left title mb-0">Produkty</div>
          <div class="is-pulled-right title">{{ cartValue }} zł</div>
        </div>
        <div class="panel-block is-justify-content-space-between">
          <div class="is-pulled-left title mb-0">Przesyłka</div>
          <div class="is-pulled-right title">{{ padInt(delivery) }}</div>
        </div>
        <div class="panel-block is-justify-content-space-between">
          <div class="is-pulled-left title mb-0">Suma</div>
          <div class="is-pulled-right title">
            {{ padInt(deliverycartValue) }}
          </div>
        </div>
        <b-button
          type="is-success"
          expanded
          class="mt-5"
          @click="subButtonClicked"
          :disabled="
            cart === undefined ||
            cart.cart_product === undefined ||
            cart.cart_product.length == 0
          "
          >Zamów</b-button
        >
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "CartDashboard",
  components: {},

  data() {
    return {
      product: {},
      quantity: 1,
    };
  },

  watch: {
    $route: {
      handler: "fetchTestlineData",
      immediate: true,
    },
  },

  computed: {
    ...mapGetters("product", ["products"]),

    ...mapGetters("auth", ["isAuthenticated", "authUser"]),
    ...mapGetters("cart", [
      "cartValue",
      "cart",
      "delivery",
      "deliverycartValue",
    ]),
  },

  methods: {
    ...mapActions("product", ["getProducts"]),
    ...mapActions("cartProduct", ["addProductToCart"]),
    ...mapActions("cart", ["getCart", "changeProduct"]),
    ...mapActions("cart", ["getCart", "removeCartProduct", "CloseCart"]),
    fetchTestlineData() {
      this.getProducts().then(() => {
        for (var product of this.products) {
          if (product.name === this.$route.params.name) {
            this.product = product;
            break;
          }
        }
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

    valueChanged(name, quantity, cart_product) {
      if (quantity >= cart_product.max_quantity) {
        cart_product.quantity = cart_product.max_quantity;
        return;
      }
      this.changeProduct({
        id: this.cart.id,
        payload: { product: name, quantity: quantity },
      }).then(() => {
        this.getCart();
      });
    },

    subButtonClicked() {
      this.CloseCart({ id: this.cart.id });
    },

    padInt(value) {
      return value.toFixed(2).replace(".", ",") + " zł";
    },

    addToButton() {
      this.addProductToCart({
        product: this.product.name,
        quantity: this.quantity,
      })
        .then(() => {
          this.$buefy.toast.open({
            message: "Dodano produkt do koszyka",
            type: "is-success",
          });
          this.quantity = 0;
          this.getCart();
        })
        .catch(() => {
          this.$buefy.toast.open({
            message: "Przekroczono maksymalną liczbę dostepnych produktów",
            type: "is-danger",
          });
          this.quantity = 0;
        });
    },
  },
};
</script>
