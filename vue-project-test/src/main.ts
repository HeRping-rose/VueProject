import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import MyBtn from './components/MyBtn.vue';
import myNum from './components/myNum.vue';

const app = createApp(App)

app.use(createPinia())
app.use(router)

//全局注册组件
app.component('MyBtn',MyBtn)
app.component('myNum',myNum)

app.mount('#app')

