<template>
  <article class="tile is-child box">
    <b-menu class="is-custom-mobile">
      <b-menu-list label="Menu">
        <MenuItem
          :item="item"
          v-for="(item, index) in categories"
          :key="index"
        /> </b-menu-list
    ></b-menu>
  </article>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import validatedInput from "@/components/customInputs/validatedInput.vue";
import MenuItem from "@/components/shop/MenuItem.vue";

export default {
  components: { validatedInput, MenuItem },

  name: "Menu",

  data() {
    return {
      email: "",
      purpose: "",
      topic: "",
    };
  },

  computed: {
    ...mapGetters("menu", ["categories"]),
  },

  methods: {
    ...mapActions("menu", ["getCategories"]),
  },

  created() {
    this.getCategories();
  },
};
</script>
