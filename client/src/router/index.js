import Vue from "vue";
import Router from "vue-router";
import Ping from "../components/Ping.vue";
import Upload from "../components/Upload.vue";
import MainPage from "../components/MainPage.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "MainPage",
      component: MainPage,
    },
    {
      path: "/ping",
      name: "Ping",
      component: Ping,
    },
    {
      path: "/upload",
      name: "Upload",
      component: Upload,
    },
  ],
});
