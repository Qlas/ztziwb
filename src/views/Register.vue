<template>
  <form class="login" @submit.prevent="registerMethod">
    <div class="columns is-center">
      <div class="column is-two-fifths box">
        <b-field
          label="Nazwa użytkownika"
          :type="wrongCredentialsProvided ? 'is-danger' : ''"
          :message="
            wrongCredentialsProvided
              ? 'nazwa użytkownika lub hasło jest nieprawidłowe.'
              : ''
          "
        >
          <b-input
            required
            validation-message="wypełnij to pole"
            v-model="username"
            placeholder="jkowalski"
            icon="account"
            data-cy="username"
          ></b-input>
        </b-field>

        <b-field label="Imię">
          <b-input
            required
            validation-message="wypełnij to pole"
            v-model="firstName"
            placeholder="Kamil"
            icon="account"
            data-cy="username"
          ></b-input>
        </b-field>

        <b-field label="Nazwisko">
          <b-input
            required
            validation-message="wypełnij to pole"
            v-model="lastName"
            placeholder="Kowalski"
            icon="account"
            data-cy="username"
          ></b-input>
        </b-field>

        <b-field label="Email">
          <b-input
            required
            validation-message="wypełnij to pole"
            v-model="email"
            type="email"
            placeholder="jkowalski@przyklad.pl"
            icon="email"
          ></b-input>
        </b-field>

        <b-field
          label="Hasło"
          :type="wrongPassword ? 'is-danger' : ''"
          :message="wrongPassword ? 'Hasła muszą być takie same.' : ''"
        >
          <b-input
            required
            validation-message="wypełnij to pole"
            v-model="password"
            type="password"
            password-reveal
            icon="lock"
            data-cy="password"
            @input="test"
          ></b-input>
        </b-field>

        <b-field
          label="Powtórz hasło"
          :type="wrongPassword ? 'is-danger' : ''"
          :message="wrongPassword ? 'Hasła muszą być takie same.' : ''"
        >
          <b-input
            required
            validation-message="wypełnij to pole"
            v-model="password2"
            type="password"
            password-reveal
            icon="lock"
            data-cy="password"
            @input="test"
          ></b-input>
        </b-field>

        <div class="buttons is-right">
          <b-button type="is-primary" native-type="submit" data-cy="button"
            >Rejestracja</b-button
          >
        </div>
      </div>
    </div>
  </form>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "Login",
  data() {
    return {
      wrongCredentialsProvided: false,
      username: "",
      firstName: "",
      lastName: "",
      password: "",
      password2: "",
      email: "",
      wrongPassword: false,
    };
  },
  methods: {
    ...mapActions("auth", ["register"]),

    test() {
      if (this.password2 !== this.password) {
        this.wrongPassword = true;
      } else this.wrongPassword = false;
    },
    registerMethod() {
      this.register({
        username: this.username,
        password: this.password,
        first_name: this.firstName,
        last_name: this.lastName,
        email: this.email,
      })
        .then(() => {
          this.$buefy.toast.open({
            message: "Konto zostało założone",
            position: "is-top",
            type: "is-primary",
            container: "div.toast-space",
          });
          this.$router.push("/logowanie");
        })
        .catch((err) => {
          this.$errorHandler.handleResponseError(err);
        });
    },
  },
};
</script>

<style scoped>
.is-center {
  height: 75vh;
  display: flex;
  flex-wrap: nowrap;
  justify-content: center;
  align-items: center;
}
</style>
