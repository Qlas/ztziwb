<template>
  <div class="contact container">
    <div class="tile is-ancestor">
      <div class="tile is-parent">
        <div class="tile is-child box is-3">
          <h2 class="title">Informacje</h2>
          <article class="media">
            <div class="media-left">
              <b-icon type="is-secondary" icon="email" />
            </div>
            <div class="media-content">
              <div class="content">
                Dzianiny24<br />
                ul Dzininowa 24<br />
                51-129 Wrocław<br />
                Polska
              </div>
            </div>
          </article>
          <article class="media">
            <div class="media-left">
              <b-icon type="is-secondary" icon="phone" />
            </div>
            <div class="media-content">
              <div class="content">
                Zadzwoń do nas<br />
                123 456 789<br />
              </div>
            </div>
          </article>
          <article class="media">
            <div class="media-left">
              <b-icon type="is-secondary" icon="email" />
            </div>
            <div class="media-content">
              <div class="content">
                Napisz do nas<br />
                sklep@dzianiny24.pl
              </div>
            </div>
          </article>
        </div>
        <ContactForm />
      </div>
    </div>
  </div>
</template>

<script>
import ContactForm from "@/components/ContactForm.vue";
export default {
  name: "Contact",
  components: {
    ContactForm,
  },
};
</script>
