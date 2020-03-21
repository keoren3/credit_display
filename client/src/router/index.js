import Vue from 'vue';
import Router from 'vue-router';
import Ping from '../components/Ping.vue';
import Upload from '../components/Upload.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/upload',
      name: 'Upload',
      component: Upload,
    },
  ],
});
