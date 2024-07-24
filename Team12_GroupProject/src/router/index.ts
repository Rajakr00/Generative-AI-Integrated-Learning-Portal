import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from "../components/LoginPage.vue"

const routes = [
    {
      path: '/',
      name: 'LoginPage',
      component: LoginPage
    },
  
  ];


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes
})

export default router
