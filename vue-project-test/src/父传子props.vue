

<template>
  <div>
    <h1 class="main">主页面</h1>
    <!-- 父传子 -->
    <!-- <MyBtn></MyBtn> -->
    <!-- 当标签用 但 html 不区分大小写   -->
     <!-- html中用中间- 来连接两个单词 -->
      <!-- <my-btn></my-btn> -->
       <!-- 在传入props时  除了直接写字符串传入外  都需要用v-bind : -->
       <MyBtn :title=Register color="red"   :num="1" />
       <MyBtn title="Login" color="blue">  </MyBtn>
       <MyBtn title="logout">  </MyBtn>
  </div>

</template>

<script setup lang="ts">
//局部注册  严格区分大小写 命名时候用小驼峰
// import myBtn from './components/MyBtn.vue';

let Register='注册'

</script>

<style>

</style>

