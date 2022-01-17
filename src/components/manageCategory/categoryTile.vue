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
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapMutations } from "vuex";

export default {
  name: "CategoryTile",

  components: {},

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
    return {};
  },
  methods: {
    padInt(value) {
      return value.toString().padStart(2, "0");
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
