<template>
  <div class="tl-reservation-dashboard container">
    <div class="tile is-ancestor">
      <div class="tile is-vertical">
        <div class="box tile is-12" v-if="!loading">
          <div class="tile is-vertical">
            <div class="title has-text-centered">{{ product.name }}</div>
            <div class="tile is-ancestor">
              <div class="tile is-6">
                <figure class="image">
                  <img
                    :src="
                      product.image
                        ? product.image
                        : 'https://e-pasmanteria.pl/environment/cache/images/0_0_productGfx_21861.jpg'
                    "
                    alt="Placeholder image"
                  />
                </figure>
              </div>
              <div class="tile is-6">
                <div class="tile is-vertical is-12">
                  <div class="panel-block is-justify-content-space-between">
                    <div class="is-pulled-left">
                      <strong class="bold">Cena:</strong>
                    </div>
                    <div class="is-pulled-right">{{ product.price }}</div>
                  </div>

                  <div class="panel-block is-justify-content-space-between">
                    <div class="is-pulled-left">
                      <strong class="bold">Dostępność:</strong>
                    </div>
                    <div class="is-pulled-right">
                      {{
                        product.quantity > 50
                          ? "duża"
                          : product.quantity > 25
                          ? "średnia"
                          : product.quantity > 1
                          ? "na wyczerpaniu"
                          : "brak w magazynie"
                      }}
                    </div>
                  </div>
                  <br />

                  <div style="width: 40%; margin-left: 210px">
                    <b-field>
                      <b-numberinput
                        expanded
                        controls-position="compact"
                        controls-alignment="left"
                        min="1"
                        :max="product.quantity"
                        :disabled="product.quantity === 0"
                        v-model="quantity"
                      />
                      <p class="control ml-1">
                        <b-button
                          label="Do koszyka"
                          :disabled="product.quantity === 0 || quantity === 0"
                          @click="addToButton"
                        />
                      </p>
                    </b-field>
                  </div>
                  <strong class="bold has-text-centered">Opis:</strong>

                  <div
                    class="is-pulled-right"
                    v-html="product.description"
                  ></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "TLDetailsDashboard",
  components: {},

  data() {
    return {
      product: {},
      quantity: 1,
      loading: true,
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
  },

  methods: {
    ...mapActions("product", ["getProducts"]),
    ...mapActions("cartProduct", ["addProductToCart"]),
    ...mapActions("cart", ["getCart"]),
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

  created() {
    this.getProducts().then(() => {
      this.loading = false;
    });
  },
};
</script>
