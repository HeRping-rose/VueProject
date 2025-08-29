

<template>
  <div>
    <h1 class="main">主页面</h1>
    <!-- 父传子 -->
    <!-- <MyBtn></MyBtn> -->
    <!-- 当标签用 但 html 不区分大小写   -->
     <!-- html中用中间- 来连接两个单词 -->
      <!-- <my-btn></my-btn> -->
       <!-- 在传入props时  除了直接写字符串传入外  都需要用v-bind : -->
       <!-- <MyBtn :title=Register color="red"   :num="1" />
       <MyBtn title="Login" color="blue">  </MyBtn>
       <MyBtn title="logout">  </MyBtn> -->

       <p>名称: {{ goods.title }}</p>
       <p>价格: {{ goods.price }}</p>

       <myNum @getNum="addNum"></myNum>
  </div>

</template>

<script setup lang="ts">
import { reactive } from 'vue';

//局部注册  严格区分大小写 命名时候用小驼峰
// import myBtn from './components/MyBtn.vue';
let goods =reactive({
    id: 1, title: '商品1', price: 100

    // 收集到你要几件的那个数量的值   (子传给父)
});

function addNum(num: number) {
  goods.price = num;
  console.log(num);
}

</script>

<style>

</style>

