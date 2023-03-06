import { createRouter, createWebHashHistory } from 'vue-router';
import InfoView from '../view/InfoView.vue';

const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/info',
      name: 'info',
      component: InfoView
    },
  ],
});

export default router;
