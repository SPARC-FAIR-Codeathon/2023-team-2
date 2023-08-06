import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/home/HomeView.vue'
import AboutView from '@/views/about/AboutView.vue'
import VisualizeView from '@/views/visualize/VisualizeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
    },
    {
      path: '/visualize',
      name: 'visualize',
      component: VisualizeView
    }
  ]
})

export default router
