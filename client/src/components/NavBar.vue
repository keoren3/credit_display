<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <router-link
      class="navbar-brand"
      to="/"
    >
      Credit Display Web
    </router-link>
    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbarNav"
      aria-controls="navbarNav"
      aria-expanded="false"
      aria-label="Toggle navigation"
    />
    <div
      id="navbarNav"
      class="collapse navbar-collapse"
    >
      <div class="navbar-nav">
        <v-btn to="/register">
          Register
        </v-btn>
        <v-btn to="/login">
          Login
        </v-btn>
        <v-btn
          v-if="isAuthenticated"
          to="/upload"
        >
          Upload
        </v-btn>
        <div class="navbar-nav mr-auto">
          <v-btn
            v-if="isAuthenticated"
            @click="logout"
          >
            Logout
          </v-btn>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapGetters, mapState } from "vuex";
import { AUTH_LOGOUT } from "../store/actions/auth";

export default {
  Main: "NavBar",

  computed: {
    ...mapGetters(["getProfile", "isAuthenticated", "isProfileLoaded"]),
    ...mapState({
      authLoading: (state) => state.auth.status === "loading",
    }),
  },
  methods: {
    logout() {
      this.$store.dispatch(AUTH_LOGOUT)
        .then(() => {
          this.$router.push({ name: "MainPage" });
        });
    },
  },
};
</script>

<style scoped>
.topnav-right {
  float: right;
}
</style>
