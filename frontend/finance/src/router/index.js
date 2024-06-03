import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Deposit from '@/views/Deposit.vue'
import Savings from '@/views/Savings.vue'
import Exchange from '@/views/Exchange.vue'
import MyPage from '@/views/MyPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/deposit',
      name: 'deposit',
      component: Deposit
    },
    {
      path: '/savings',
      name: 'savings',
      component: Savings
    },
    {
      path: '/exchange',
      name: 'exchange',
      component: Exchange
    },
    {
      path: '/mypage',
      name: 'myPage',
      component: MyPage
    },
  ]
})

export default router
