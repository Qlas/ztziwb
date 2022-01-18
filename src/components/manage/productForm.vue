<template>
  <ValidationObserver v-slot="{ handleSubmit }">
    <form @submit.prevent="handleSubmit(processForm)">
      <div class="modal-card" style="width: 40em">
        <header class="modal-card-head">
          <p class="modal-card-title">
            {{
              currentData ? `Edit ${currentData.name}` : "Dodaj nowy produkt"
            }}
          </p>
        </header>
        <section class="modal-card-body">
          <ValidatedInput
            v-model="name"
            placeholder="Wpisz nazwe produktu"
            maxlength="255"
            :validation="{
              name: 'Nazwa',
              rules: 'required',
            }"
            :field="{ label: 'Nazwa', expanded: true }"
          />

          <ValidatedInput
            v-model="description"
            placeholder="Wpisz opis produktu"
            type="textarea"
            maxlength="512"
            :validation="{ name: 'Opis', rules: 'required' }"
            :field="{ label: 'Opis', expanded: true }"
          />

          <b-field label="Kategoria">
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

          <ValidatedInput
            inputType="b-numberinput"
            v-model="price"
            min="0"
            step="0.01"
            :validation="{
              rules: 'required',
            }"
            :field="{ label: 'Cena' }"
          />

          <ValidatedInput
            inputType="b-numberinput"
            v-model="quantity"
            min="0"
            step="1"
            :validation="{
              rules: 'required',
            }"
            :field="{ label: 'Liczba sztuk' }"
          />

          <ValidatedInput
            inputType="url"
            v-model="image"
            min="0"
            step="1"
            :validation="{
              rules: 'required|url',
            }"
            :field="{ label: 'Zdjęcie' }"
          />
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
  name: "ProductForm",

  props: ["currentData"],

  data() {
    return {
      name: this.currentData ? this.currentData.name : "",
      description: this.currentData ? this.currentData.description : "",
      cost: this.currentData ? this.currentData.cost : {},
      price: this.currentData ? parseFloat(this.currentData.price) : 0,
      quantity: this.currentData ? this.currentData.quantity : 0,
      image: this.currentData ? this.currentData.image : "",
      category: this.currentData ? this.currentData.category : "",
    };
  },

  methods: {
    ...mapActions("product", ["addProduct", "updateProduct"]),
    ...mapActions("product", ["getProducts"]),
    ...mapActions("menu", ["getCategories"]),

    deleteDropFile(index) {
      this.dropFiles.splice(index, 1);
    },

    processForm() {
      const processFormAction = this.currentData
        ? this.updateProduct
        : this.addProduct;

      let requestData = {
        name: this.name,
        description: this.description,
        cost: this.cost,
        time: this.time,
        price: this.price,
        quantity: this.quantity,
        image: this.image,
        category: this.category,
      };

      if (this.currentData) {
        requestData = {
          update: {
            payload: {
              name: this.name,
              description: this.description,
              cost: this.cost,
              time: this.time,
              price: this.price,
              quantity: this.quantity,
              image: this.image,
              category: this.category,
            },
            productId: this.currentData.id,
          },
        };
      }

      const toastMessage = this.currentData
        ? `Zaktualizowano ${this.name}`
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
