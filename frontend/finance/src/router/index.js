import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Deposit from '@/views/Deposit.vue'
import Savings from '@/views/Savings.vue'
import Exchange from '@/views/Exchange.vue'
import MyPage from '@/views/MyPage.vue'
import Login from '@/views/Login.vue'
import Signin from '@/views/Signin.vue'
import Detail from '@/views/Detail.vue'

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
      path: '/detail',
      name: 'detail',
      component: Detail,
    },
    {
      path: '/mypage',
      name: 'myPage',
      component: MyPage
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/signin',
      name: 'signin',
      component: Signin
    },
  ]
})

export default router
