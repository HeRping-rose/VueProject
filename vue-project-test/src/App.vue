<template>
  <div>
    <!-- 头部组件 -->
    <my-header > 首页 </my-header>
    <my-header > 我的 </my-header>

    <my-header >
      <!-- 模板用于定义一个专用的结构
       把这个模板内容 插入到插槽名字为 left的中 -->
      <template v-slot:left>
        <!-- 返回箭头 -->
        <!-- <div>左侧内容</div> -->
         <img src="./assets/logo.svg" width="20" alt="">
      </template>
      首页
      <template v-slot:right>
        右
      </template>
    </my-header>
  </div>

</template>


<script setup lang="ts">
import MyHeader from './components/myHeader.vue'
import { reactive } from 'vue';


</script>


<style>
*{
  margin: 0;
  padding: 0;
}

</style>

