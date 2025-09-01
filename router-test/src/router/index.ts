import { createRouter, createWebHistory } from 'vue-router'
import { default as Cate1 } from '@/pages/catepage/cate1.vue';
import { default as Cate2 } from '@/pages/catepage/cate2.vue';
import { default as Cate3 } from '@/pages/catepage/cate3.vue';
import { default as Cate4 } from '@/pages/catepage/cate4.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    //每配置一个页面的路由 ,你就需要告诉我 在浏览器上访问那个路径时加载对应组件
    // {path: '/', redirect: '/home'},
    {path: '/', component: () => import('../pages/home.vue')},
    { 
      path: '/cate', 
      component: () => import('../pages/cate.vue'),
      //子路由 配置
      children: [
        { path: '', component: Cate1 },// 默认可以不写
        { path: 'cate2', component: Cate2 },  //子路由不加/
        { path: 'cate3', component: Cate3 },
        { path: 'cate4', component: Cate4 },
      ]
    },
    {path: '/list', component: () => import('../pages/list.vue')},
    {path: '/detail', component: () => import('../pages/detail.vue')},
    {path: '/news/:id', component: () => import('../pages/news.vue')},
    

  ],
})

export default router
