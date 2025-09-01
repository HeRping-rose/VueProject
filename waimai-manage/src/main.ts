import { createApp } from 'vue'

import { createPinia } from 'pinia'
// 1.全局引入 elementUI中所有的组件
import ElementPlus from 'element-plus'
// 2.引入UI中通用样式
import 'element-plus/dist/index.css'

import App from './App.vue'
import router from './router'
// 如果您正在使用CDN引入，请删除下面一行。
import * as ElementPlusIconsVue from '@element-plus/icons-vue'

const app = createApp(App)

//注册所有图标
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}

app.use(createPinia())
app.use(router)
// 3.在vue项目中使用第三方的elementplus组件库
app.use(ElementPlus)

app.mount('#app')
