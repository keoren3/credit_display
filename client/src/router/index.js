import Vue from "vue";
import Router from "vue-router";
import Ping from "../components/Ping.vue";
import Upload from "../components/Upload.vue";
import MainPage from "../components/MainPage.vue";
import Register from "../components/Register.vue";
import Login from "../components/Login.vue";

Vue.use(Router);

const router = new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "MainPage",
      component: MainPage,
    },
    {
      path: "/login",
      name: "Login",
      component: Login,
    },
    {
      path: "/register",
      name: "Register",
      component: Register,
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
    { path: "*", redirect: "/" },
  ],
});

export default router;

router.beforeEach((to, from, next) => {
  const publicPages = ["/login", "/register"];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = localStorage.getItem("user");
  if (authRequired && !loggedIn) {
    return next("/login");
  }
  next();
});
