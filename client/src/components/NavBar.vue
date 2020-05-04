<template>
  <nav>
    <v-app-bar
      class="background: grey lighten-4"
      flat
      app
    >
      <v-app-bar-nav-icon
        class="grey--text"
        @click="drawer = !drawer"
      />
      <v-toolbar-title class="text-uppercase grey--text">
        <span class="font-weight-dark">Credit Display</span>
      </v-toolbar-title>
      <v-spacer />
      <v-menu offset-y>
        <template v-slot:activator="{ on }">
          <v-btn
            text
            v-on="on"
          >
            Menu
            <v-icon right>
              mdi-chevron-down
            </v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item
            v-for="(link, index) in linksFilter"
            :key="index"
            rotuer
            :to="link.route"
          >
            <v-list-item-title>{{ link.text }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>

      <v-btn
        v-if="isAuthenticated"
        text
        @click="logout"
      >
        <span>Logout</span>
        <v-icon right>
          mdi-exit-to-app
        </v-icon>
      </v-btn>
    </v-app-bar>

    <v-navigation-drawer
      v-model="drawer"
      dark
      app
      class="primary"
    >
      <v-list>
        <v-list-item
          v-for="(link, index) in linksFilter"
          :key="index"
          :to="link.route"
        >
          <v-list-item-action>
            <v-icon class="white--text">
              {{ link.icon }}
            </v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title class="white--text">
              {{ link.text }}
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </nav>
</template>


<script>


import { mapGetters, mapState } from "vuex";
import { AUTH_LOGOUT } from "../store/actions/auth";

export default {
  Main: "NavBar",
  data () {
    return {
      drawer: false,
      links: {
        auth: this.$store.getters.isAuthenticated,
        arr: [
          { icon: "mdi-view-dashboard", text: "Dashboard", route: "/" },
          { icon: "mdi-login", text: "Login", route: "/login" },
          { icon: "mdi-account", text: "Register", route: "/register" },
          { icon: "mdi-account-group", text: "Team", route: "/team" }
        ]
      }
    };
  },
  computed: {
    ...mapGetters(["getProfile", "isAuthenticated", "isProfileLoaded"]),
    ...mapState({
      authLoading: (state) => state.auth.status === "loading",
    }),
    linksFilter () {
      if (!this.links.auth) { return this.links.arr; }
      return this.links.arr.filter((link) => link.text !== "Login" && link.text !== "Register");
    }
  },
  methods: {
    logout () {
      this.$store.dispatch(AUTH_LOGOUT).then(() => {
        this.$router.push({ path: "/" }).catch(() => { });
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
