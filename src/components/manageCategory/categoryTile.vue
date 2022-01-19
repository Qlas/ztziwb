<template>
  <div>
    <div class="box mb-1">
      <div class="columns is-vcentered">
        <div class="column">
          <div class="columns is-vcentered">
            <div class="column is-12 group-options"></div>
            <div class="column is-12">
              <h2>{{ name }}</h2>
            </div>
          </div>
        </div>
        <div class="column is-1">
          <b-button type="is-warning" @click="() => editClicked(name)"
            >Edytuj</b-button
          >
        </div>
        <div class="column is-1">
          <b-button type="is-danger" @click="() => removeClicked(id)"
            >Usuń</b-button
          >
        </div>
      </div>
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
import { mapActions, mapMutations, mapGetters } from "vuex";
import categoryForm from "@/components/manageCategory/categoryForm.vue";

export default {
  name: "CategoryTile",

  components: { categoryForm },

  props: [
    "id",
    "name",
    "info",
    "capacity",
    "cost",
    "user",
    "quantity",
    "price",
  ],
  data() {
    return { isCategoryModalActive: false, CategoryEdit: {} };
  },
  computed: {
    ...mapGetters("menu", ["categories"]),
  },
  methods: {
    ...mapActions("menu", ["removeCategory", "getCategories"]),
    padInt(value) {
      return value.toString().padStart(2, "0");
    },

    editClicked(name) {
      this.isCategoryModalActive = true;
      for (var category of this.categories) {
        if (category.name === name) {
          this.CategoryEdit = category;
        }
      }
    },
    removeClicked(id) {
      this.removeCategory(id).then(() => {
        this.getCategories({ show_main: false });
      });
    },
  },
};
</script>

<style lang="scss">
.preview-tile {
  margin: -1.3em 0 2.5em 0;
}

.preview-trigger {
  cursor: pointer;
}

.tl-count-tag {
  margin: 0 1.5em;
}

.tl-count-tag-total {
  margin-left: 9.5em;
}

.group-options {
  width: 3% !important;
}
</style>
