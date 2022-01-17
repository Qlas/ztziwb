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
              rules: 'required|alpha_dash',
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

          <b-field>
            <b-upload v-model="dropFiles" multiple drag-drop>
              <section class="section">
                <div class="content has-text-centered">
                  <p>
                    <b-icon icon="upload" size="is-large"> </b-icon>
                  </p>
                  <p>Drop your files here or click to upload</p>
                </div>
              </section>
            </b-upload>
          </b-field>

          <div class="tags">
            <span
              v-for="(file, index) in dropFiles"
              :key="index"
              class="tag is-primary"
            >
              {{ file.name }}
              <button
                class="delete is-small"
                type="button"
                @click="deleteDropFile(index)"
              ></button>
            </span>
          </div>
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
      time: this.currentData ? this.currentData.time : {},
      price: this.currentData ? this.currentData.name : 0,
      quantity: this.currentData ? this.currentData.quantity : 0,
      dropFiles: [],
    };
  },

  methods: {
    ...mapActions("clients", ["getClients", "addClient", "updateClient"]),

    deleteDropFile(index) {
      this.dropFiles.splice(index, 1);
    },

    processForm() {
      console.log(this.dropFiles);
      return;
      const processFormAction = this.currentData
        ? this.updateClient
        : this.addClient;

      let requestData = {
        name: this.name,
        description: this.description,
        cost: this.cost,
        time: this.time,
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
        : "Added a new Client";

      processFormAction(requestData)
        .then(() => {
          this.$parent.close();
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
    ...mapGetters("product", ["products"]),
  },
};
</script>
