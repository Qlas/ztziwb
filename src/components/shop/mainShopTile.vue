<template>
  <article class="tile is-vertical box">
    <div class="tile is-parent" v-for="row in chunkedArr">
      <div
        class="tile is-parent is-4 pr-1 pl-1 pb-1 pt-1"
        v-for="(item, index) in row"
        :key="index"
      >
        <productBox :product="item" />
      </div>
    </div>
  </article>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import validatedInput from "@/components/customInputs/validatedInput.vue";
import productBox from "@/components/shop/productBox.vue";

export default {
  components: { validatedInput, productBox },

  name: "MainShopTile",

  data() {
    return {
      email: "",
      purpose: "",
      topic: "",
    };
  },

  watch: {
    $route: {
      handler: "RouterChanged",
    },
  },

  computed: {
    ...mapGetters("product", ["products"]),
    chunkedArr() {
      const result = [];
      for (let i = 0; i < this.products.length; i += 3)
        result.push(this.products.slice(i, i + 3));
      return result;
    },
  },

  methods: {
    ...mapActions("product", ["getProducts"]),

    RouterChanged(route) {
      this.getProducts(route.query);
    },
  },

  created() {
    this.getProducts();
  },
};
</script>
