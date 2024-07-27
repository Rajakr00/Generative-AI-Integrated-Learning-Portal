import { createRouter, createWebHistory } from 'vue-router'
import CoursePage from '@/components/CoursePage.vue'
import LoginPage from '../components/LoginPage.vue'
import Dashboard from '../components/Dashboard.vue'

const routes = [
  {
    path: '/',
    name: 'LoginPage',
    component: LoginPage,
    meta: {
      heading: 'Student Login'
    }
  },
  {
    path: '/studentDashboard',
    name: 'studentDashboard',
    component: Dashboard,
    meta: {
      heading: 'Dashboard'
    }
  },
  {
    path: '/coursePage',
    name: 'coursePage',
    component: CoursePage,
    meta: {
      heading: ''
    }
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes
})

export default router
