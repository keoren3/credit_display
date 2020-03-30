<template>
  <div id="app">
    <NavBar />
    <router-view />
  </div>
</template>

<script>
// import PieChart from "./components/PieChart.vue";
import NavBar from "./components/NavBar.vue";

export default {
  name: "App",
  components: {
    NavBar,
    // PieChart,
  },
};
</script>

<style>
#app {
  margin-top: 60px;
}
</style>
