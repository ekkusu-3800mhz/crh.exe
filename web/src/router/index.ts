import { createRouter, createWebHashHistory } from 'vue-router';
import InfoView from '../view/InfoView.vue';
import QueueView from '../view/QueueView.vue';

const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/info',
      name: 'info',
      component: InfoView,
    },
    {
      path: '/queue',
      name: 'queue',
      component: QueueView,
    },
  ],
});

export default router;
