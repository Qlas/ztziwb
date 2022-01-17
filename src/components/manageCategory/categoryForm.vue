<template>
  <ValidationObserver v-slot="{ handleSubmit }">
    <form @submit.prevent="handleSubmit(processForm)">
      <div class="modal-card" style="width: 40em">
        <header class="modal-card-head">
          <p class="modal-card-title">
            {{
              currentData ? `Edit ${currentData.name}` : "Dodaj nową kategorie"
            }}
          </p>
        </header>
        <section class="modal-card-body">
          <ValidatedInput
            v-model="name"
            placeholder="Wpisz nazwe kategorii"
            maxlength="255"
            :validation="{
              name: 'Nazwa',
              rules: 'required',
            }"
            :field="{ label: 'Nazwa', expanded: true }"
          />

          <b-field label="Kategoria główna">
            <b-select placeholder="Wybierz kategorie" v-model="category">
              <option
                v-for="option in categories"
                :value="option.name"
                :key="option.id"
              >
                {{ option.name }}
              </option>
            </b-select>
          </b-field>
        </section>
        <footer class="modal-card-foot">
          <button class="button" type="button" @click="$parent.close()">
            Zamknij
          </button>
          <button class="button is-primary">
            <p v-if="!currentData">Dodaj</p>
            <p v-else>Update</p>
          </button>
        </footer>
      </div>
    </form>
  </ValidationObserver>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "CategoryForm",

  props: ["currentData"],

  data() {
    return {
      name: this.currentData ? this.currentData.name : "",
      description: this.currentData ? this.currentData.description : "",
      cost: this.currentData ? this.currentData.cost : {},
      price: this.currentData ? this.currentData.name : 0,
      quantity: this.currentData ? this.currentData.quantity : 0,
      image: this.currentData ? this.currentData.image : "",
      category: this.currentData ? this.currentData.category : "",
    };
  },

  methods: {
    ...mapActions("product", ["addProduct"]),
    ...mapActions("product", ["getProducts"]),
    ...mapActions("menu", ["getCategories", "addCategory"]),

    deleteDropFile(index) {
      this.dropFiles.splice(index, 1);
    },

    processForm() {
      const processFormAction = this.currentData
        ? this.updateClient
        : this.addCategory;

      let requestData = {
        name: this.name,
        is_main: this.category === "",
        parent_category: this.category ? this.category : null,
        sub_category: null,
      };

      if (this.currentData) {
        requestData = {
          update: {
            payload: {
              name: this.name,
              description: this.description,
              cost: this.cost,
              time: this.time,
            },
            clientId: this.currentData.id,
          },
        };
      }

      const toastMessage = this.currentData
        ? `Updated ${this.name} Client`
        : "Dodano nowy produkt";

      processFormAction(requestData)
        .then(() => {
          this.$parent.close();
          this.getProducts();
          this.$buefy.toast.open({
            message: toastMessage,
            position: "is-top",
            type: "is-primary",
            container: "div.toast-space",
          });
        })
        .catch((err) => {
          this.$errorHandler.handleResponseError(err);
        });
    },
  },

  computed: {
    ...mapGetters("menu", ["categories"]),
  },

  created() {
    this.getCategories({ show_main: false });
  },
};
</script>
