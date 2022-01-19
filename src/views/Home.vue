<template>
  <div class="home">
    <section
      class="hero is-primary is-bold is-relative home-top"
      :style="{
        'background-image':
          'url(' + require('../assets/pasmanteria.jpg') + ') ',
      }"
    >
      <div class="hero-body">
        <div class="container has-text-centered">
          <transition name="slide-down">
            <h1 v-if="showElements" class="title is-size-1 is-spaced">
              Dzianiny24
            </h1>
          </transition>
          <transition name="slide-up-200ms">
            <h3 v-if="showElements" class="subtitle"></h3>
          </transition>
        </div>
      </div>
      <div class="hero-foot">
        <div class="section has-smaller-padding">
          <div class="container">
            <div class="column is-12 has-text-centered">
              <transition name="slow-in-300ms">
                <div v-if="showElements"></div>
              </transition>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="hero is-lighter is-unselectable">
      <div class="hero-body">
        <div class="container has-text-centered">
          <div class="columns is-centered is-multiline is-mobile">
            <div class="column is-half-mobile has-text-centered">
              <p class="title is-4 has-text-weight-semibold">
                100% Satysfakcji
              </p>

              <b-icon
                size="is-medium"
                type="is-gold"
                icon="star-circle-outline"
              ></b-icon>
            </div>

            <div class="column is-half-mobile has-text-centered">
              <p class="title is-4 has-text-weight-semibold">14 dni na zwrot</p>

              <b-icon
                size="is-medium"
                type="is-success"
                icon="calendar"
              ></b-icon>
            </div>
          </div>
        </div>
      </div>
    </section>
    <div class="title has-text-centered">Nowości</div>
    <div class="container">
      <b-carousel-list
        :data="products"
        :arrow="true"
        :arrow-hover="false"
        :items-to-show="3"
      >
        <template #item="list">
          <productBox :product="list" />
        </template>
      </b-carousel-list>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import productBox from "@/components/shop/productBox.vue";

export default {
  components: { productBox },
  computed: {
    ...mapGetters("auth", ["isAuthenticated", "authUser"]),
    ...mapGetters("product", ["products"]),
  },
  data() {
    return {
      showElements: false,
      hash: process.env.VUE_APP_GIT_HASH,
      tag: process.env.VUE_APP_GIT_TAG,
      tag_distance: process.env.VUE_APP_GIT_DISTANCE,
    };
  },

  methods: {
    ...mapActions("product", ["getProducts"]),
  },
  mounted() {
    this.showElements = true;
    this.getProducts({ latest: true });
  },
};
</script>
<style scoped lang="scss">
@import "@/styles/colors.scss";

section.hero.is-primary {
  background-image: linear-gradient($primary, $secondary);
}
.home-top {
  background-size: 100% auto;
  height: 500px;
}
@keyframes disappear {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}
@keyframes slideDown {
  0% {
    opacity: 0;
    transform: translateY(-1rem);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(1rem);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
@keyframes slowIn {
  0% {
    opacity: 0;
    transform: scale(0.9);
  }
  100% {
    opacity: 1;
    transform: scale(1);
  }
}
//Animation: Slide down • 0s
.slide-down-enter-active {
  animation: slideDown 0.4s ease-out;
}
.slide-down-enter,
.slide-down-leave-to {
  opacity: 0;
  transform: translateY(-1rem);
}
.slide-down-leave,
.slide-down-enter-to {
  opacity: 1;
  transform: translateY(0);
}
//Animation: Slide up • 0.2s
.slide-up-200ms-enter-active {
  animation: disappear 0s forwards, slideUp 0.4s ease-out 0.2s; //name, duration, timing-function, delay, iteration-count, direction, fill-mode.
}
.slide-up-200ms-enter,
.slide-up-200ms-leave-to {
  opacity: 0;
  transform: translateY(1rem);
}
.slide-up-200ms-leave,
.slide-up-200ms-enter-to {
  opacity: 1;
  transform: translateY(0);
}
//Animation: Slow in • 0.3s, 0.4s, 0.5s, 0.6s, 0.7s
.slow-in-300ms-enter-active {
  animation: disappear 0s forwards, slowIn 0.4s ease-out 0.3s;
}
.slow-in-400ms-enter-active {
  animation: disappear 0s forwards, slowIn 0.4s ease-out 0.4s;
}
.slow-in-500ms-enter-active {
  animation: disappear 0s forwards, slowIn 0.4s ease-out 0.5s;
}
.slow-in-600ms-enter-active {
  animation: disappear 0s forwards, slowIn 0.4s ease-out 0.6s;
}
.slow-in-700ms-enter-active {
  animation: disappear 0s forwards, slowIn 0.4s ease-out 0.7s;
}
.slow-in-300ms-enter,
.slow-in-300ms-leave-to,
.slow-in-400ms-enter,
.slow-in-400ms-leave-to,
.slow-in-500ms-enter,
.slow-in-500ms-leave-to,
.slow-in-600ms-enter,
.slow-in-600ms-leave-to,
.slow-in-700ms-enter,
.slow-in-700ms-leave-to {
  opacity: 0;
  transform: scale(0.9);
}
.slow-in-300ms-leave,
.slow-in-300ms-enter-to,
.slow-in-400ms-leave,
.slow-in-400ms-enter-to,
.slow-in-500ms-leave,
.slow-in-500ms-enter-to,
.slow-in-600ms-leave,
.slow-in-600ms-enter-to,
.slow-in-700ms-leave,
.slow-in-700ms-enter-to {
  opacity: 1;
  transform: scale(1);
}

.home {
  margin-top: -30pt;
}
</style>
