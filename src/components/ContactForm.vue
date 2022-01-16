<template>
  <article class="tile is-child box">
    <ValidationObserver v-slot="{ handleSubmit }">
      <form ref="form" @submit.prevent="handleSubmit(sendFormMethod)">
        <p>
          <span class="title">Formularz kontaktowy</span>
        </p>
        <section>
          <ValidatedInput
            placeholder="przyklad@przyklad.pl"
            type="email"
            v-model="email"
            :validation="{
              rules: 'required|email',
            }"
            :field="{
              label: 'Email',
            }"
          />
          <ValidatedInput
            placeholder="Temat"
            maxlength="50"
            v-model="topic"
            :validation="{
              rules: 'required',
            }"
            :field="{
              label: 'Temat',
            }"
          />
          <ValidatedInput
            placeholder="Treść wiadomości"
            type="textarea"
            maxlength="512"
            v-model="purpose"
            :validation="{
              rules: 'required',
            }"
            :field="{
              expanded: 'true',
              label: 'Wiadomość',
            }"
          />

          <button class="button is-primary">Wyślij</button>
        </section>
      </form>
    </ValidationObserver>
  </article>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import validatedInput from "@/components/customInputs/validatedInput.vue";

export default {
  components: { validatedInput },

  name: "ContactForm",

  data() {
    return {
      email: "",
      purpose: "",
      topic: "",
    };
  },

  computed: {
    ...mapGetters("group", ["groupNames"]),
    ...mapGetters("auth", ["isAuthenticated", "authUser"]),
  },

  methods: {
    ...mapActions("contactForm", ["sendForm"]),

    sendFormMethod() {
      this.sendForm({
        email: this.email,
        purpose: this.purpose,
        topic: this.topic,
      }).then(() => {
        this.$buefy.toast.open({
          message: "Twoja wiadomość została wysłana",
          position: "is-top",
          type: "is-primary",
          container: "div.toast-space",
        });
        this.email = "";
        this.purpose = "";
        this.topic = "";
      });
    },
  },
};
</script>