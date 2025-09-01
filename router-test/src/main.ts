import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)
router.beforeEach((to, from ,next) => {
  // ...
    // console.log(to, from)

    let isLogin=false   //token判断  假如没有登录去list页面  那么跳转到登录页
    if(!isLogin && to.path=='/cate'){ 
        // 如果没有登录，并且还想要去 分类页 那么跳转到登录页
      next({path:'/list'})
    }
    next()
})


app.use(router)

app.mount('#app')

// const router = createRouter({ ... })

