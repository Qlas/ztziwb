<template>
  <div class="box">
    <div>
      <figure class="image" style="height: 210px">
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
    <div class="has-text-centered">
      <b>{{ product.name }}</b>
    </div>
    <div class="has-text-centered">{{ product.price }} zł</div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  components: {},

  name: "ProductBox",
  props: ["product"],
  data() {
    return {
      email: "",
      purpose: "",
      topic: "",
    };
  },

  computed: {},

  methods: {},
};
</script>
