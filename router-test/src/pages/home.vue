<template>

    <h2>Home Page</h2>
    <ul>
        <li v-for="(item, index) in newsList" :key="index" @click="jump(item)">
            <!-- 路由携带时需要携带query查询字符串 -->
            <!-- <router-link :to="{ path: `/detail`, query: { id: item.id } }">
                {{ item.title }}
            </router-link> -->
                {{ item.title }}

        </li>
    </ul>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter() // 获取路由实例  路由操作对象  路由跳转的方法

let newsList = ref<{ id: number; title: string }[]>([
    { id: 1, title: 'News 1' },
    { id: 2, title: 'News 2' },
    { id: 3, title: 'News 3' }
])

// 编程式跳转 在js中实现跳转
function jump(item: { id: number; title: string }) {
    // router.push('/detail') //不带参数
    router.push({ path: '/detail', query: { id: item.id } })
}
// jump({ id: 1, title: 'News 1' })
</script>