<template>
  <div class="tl-reservation-dashboard container">
    <div class="tile is-ancestor">
      <div class="tile is-vertical">
        <div class="box tile is-12">
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
                    <div class="is-pulled-right">{{ product.quantity }}</div>
                  </div>
                  <br />
                  <strong class="bold has-text-centered">Opis:</strong>

                  <div class="is-pulled-right">{{ product.description }}</div>
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
    };
  },
  computed: {},

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
  },

  created() {
    this.getProducts();
  },
};
</script>
