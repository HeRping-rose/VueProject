import { createRouter, createWebHistory } from 'vue-router'

import Login from '@/pages/login.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: Login,
      name: 'login'
    },
    {
      path: '/manage',
      component: () => import('@/pages/manage.vue'),
      name: 'manage',
      children: [
        {
          path: '',
          component: () => import('@/pages/manage/managehome.vue'),
          name: 'managehome',
          meta: {
            title: ['']
          }
        },
        {
          path: 'catelist',
          component: () => import('@/pages/manage/catelist.vue'),
          name: 'catelist',
          meta: {
            title: ['分类管理','分类列表']
          }
        },
        {
          path: 'addcate',
          component: () => import('@/pages/manage/addcate.vue'),
          name: 'addcate',
          meta: {
            title: ['分类管理','添加分类']
          }
        },
        {
          path: 'shoplist',
          component: () => import('@/pages/manage/shoplist.vue'),
          name: 'shoplist',
          meta: {
            title: ['店铺管理','店铺列表']
          }
        },
        {
          path: 'addshop',
          component: () => import('@/pages/manage/addshop.vue'),
          name: 'addshop',
          meta: {
            title: ['店铺管理','添加店铺']
          }
        },
        // 食品管理
        {
          path: 'foodlist',
          component: () => import('@/pages/manage/foodlist.vue'),
          name: 'foodlist',
          meta: {
            title: ['食品管理','食品列表']
          }
        },
        {
          path: 'addfood',
          component: () => import('@/pages/manage/addfood.vue'),
          name: 'addfood',
          meta: {
            title: ['食品管理','添加食品']
          }
        }
      ]
    },
    
  ],
})

export default router
