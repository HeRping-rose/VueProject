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
            title: '首页'
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
        }
      ]
    },
    
  ],
})

export default router
