<template>
  <b-menu-item
    :label="item.name + ' (' + item.products_count + ')'"
    @click="clickMethod"
    :active="item.name === activeMenu"
  >
    <MenuItem
      :item="item"
      v-for="(item, index) in item.sub_category"
      :key="index"
      v-if="item.sub_category && item.products_count > 0"
    />
  </b-menu-item>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from "vuex";
import validatedInput from "@/components/customInputs/validatedInput.vue";

export default {
  components: { validatedInput },
  props: ["item"],
  name: "MenuItem",

  computed: {
    ...mapGetters("menu", ["categories", "activeMenu"]),
  },

  methods: {
    ...mapActions("menu", ["getCategories"]),
    ...mapMutations("menu", ["setActiveMenu"]),

    clickMethod() {
      let routerConfig = {
        name: "Sklep",
        query: { search: this.item.name },
      };
      if (
        this.$router.currentRoute.fullPath !==
        this.$router.resolve(routerConfig).route.fullPath
      )
        this.$router.replace(routerConfig);
      this.setActiveMenu(this.item.name);
    },
  },
};
</script>
