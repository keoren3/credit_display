<template>
  <div id="app">
    <router-view />
    <PieChart
      width="100px"
      height="20px"
    />
  </div>
</template>

<script>
import PieChart from "./components/PieChart.vue";

export default {
  name: "App",
  components: {
    PieChart,
  },
};
</script>

<style>
#app {
  margin-top: 60px;
}
</style>
