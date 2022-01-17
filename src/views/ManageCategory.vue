<template>
  <div class="container">
    <div class="buttons">
      <b-button
        class="is-primary ml-2"
        icon-left="plus-thick"
        @click="openCreateModal"
      >
        Dodaj Kategorie
      </b-button>
    </div>
    <hr />

    <div v-for="(preview, index) of categories" :key="index">
      <categoryTile :id="preview.id" :name="preview.name" />
    </div>

    <b-modal
      :active.sync="isCategoryModalActive"
      has-modal-card
      trap-focus
      aria-role="dialog"
      aria-modal
    >
      <categoryForm :currentData="CategoryEdit" />
    </b-modal>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import categoryTile from "@/components/manageCategory/categoryTile.vue";
import categoryForm from "@/components/manageCategory/categoryForm.vue";
export default {
  name: "ManageCategory",
  components: {
    categoryTile,
    categoryForm,
  },

  computed: {
    ...mapGetters("menu", ["categories"]),
  },

  data() {
    return {
      isCategoryModalActive: false,
      CategoryEdit: {},
    };
  },

  methods: {
    ...mapActions("menu", ["getCategories"]),

    openCreateModal() {
      this.CategoryEdit = null;
      this.isCategoryModalActive = true;
    },
  },

  created() {
    this.getCategories({ show_main: false });
  },
};
</script>
