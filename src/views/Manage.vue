<template>
  <div class="container">
    <div class="buttons">
      <b-button
        class="is-primary ml-2"
        icon-left="plus-thick"
        @click="openCreateModal"
      >
        Dodaj Produkt
      </b-button>
    </div>
    <hr />

    <div v-for="(preview, index) of products" :key="index">
      <productTile
        :id="preview.id"
        :name="preview.name"
        :price="preview.price"
        :quantity="preview.quantity"
      />
    </div>

    <b-modal
      :active.sync="isProductModalActive"
      has-modal-card
      trap-focus
      aria-role="dialog"
      aria-modal
    >
      <productForm :currentData="ProductEdit" />
    </b-modal>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import productTile from "@/components/manage/productTile.vue";
import productForm from "@/components/manage/productForm.vue";
export default {
  name: "Sklep",
  components: {
    productTile,
    productForm,
  },

  computed: {
    ...mapGetters("product", ["products"]),
  },

  data() {
    return {
      isProductModalActive: false,
      ProductEdit: {},
    };
  },

  methods: {
    ...mapActions("product", ["getProducts"]),

    openCreateModal() {
      this.ProductEdit = null;
      this.isProductModalActive = true;
    },
  },

  created() {
    this.getProducts();
  },
};
</script>
