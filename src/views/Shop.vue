<template>
  <div class="container">
    <div class="tile is-ancestor">
      <div class="tile is-parent is-child is-3 pr-1">
        <Menu />
      </div>
      <div class="tile is-parent is-child is-9 pl-1">
        <mainShopTile />
      </div>
    </div>
  </div>
</template>

<script>
import Menu from "@/components/shop/Menu.vue";
import mainShopTile from "@/components/shop/mainShopTile.vue";
export default {
  name: "Sklep",
  components: {
    Menu,
    mainShopTile,
  },
};
</script>
