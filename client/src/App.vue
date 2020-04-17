<template>
  <div id="app">
    <NavBar />
    <router-view />
  </div>
</template>

<script>
import axios from "axios";
// import PieChart from "./components/PieChart.vue";
import { AUTH_LOGOUT } from "./store/actions/auth";
import NavBar from "./components/NavBar.vue";

export default {
  name: "App",
  components: {
    NavBar,
    // PieChart,
  },
  created() {
    axios.interceptors.response.use(undefined, (err) => new Promise(() => {
      if (err.status === 401 && err.config && !err.config.__isRetryRequest) {
      // if you ever get an unauthorized, logout the user
        this.$store.dispatch(AUTH_LOGOUT);
      // you can also redirect to /login if needed !
      }
      throw err;
    }));
  },
};
</script>

<style>
#app {
  margin-top: 60px;
}
</style>
