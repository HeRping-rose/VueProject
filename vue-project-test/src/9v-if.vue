<template>
  <div>
    <h2>购物车</h2>

    <p v-if="isLogin">欢迎回来！</p>
    <p v-else>请登录以查看购物车内容。</p>

    <button @click="toggleLogin">{{ isLogin ? '退出登录' : '登录' }}</button>

  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

let isLogin=ref(true)

function toggleLogin() {
  isLogin.value = !isLogin.value
}

</script>

<style scoped>
p {
  font-size: 16px;
  color: #333;
}
</style>