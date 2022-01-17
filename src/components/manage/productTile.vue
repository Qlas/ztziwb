<template>
  <div>
    <div class="box mb-1">
      <div class="columns is-vcentered">
        <div class="column">
          <div class="columns is-vcentered">
            <div class="column is-1 group-options"></div>
            <div class="column is-3">
              <h2>{{ name }}</h2>
            </div>
            <div class="column is-offset-4">
              <b-field grouped>
                <div class="control tl-count-tag">
                  <b-taglist attached>
                    <b-tag type="is-success">Cena</b-tag>
                    <b-tag class="is-dark">{{ padInt(price) }}</b-tag>
                  </b-taglist>
                </div>

                <div class="control tl-count-tag">
                  <b-taglist attached>
                    <b-tag type="is-warning">Sztuk</b-tag>
                    <b-tag type="is-dark">{{ padInt(quantity) }}</b-tag>
                  </b-taglist>
                </div>
              </b-field>
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
  name: "ProductTile",

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
