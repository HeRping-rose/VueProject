<template>
  <div>
    <!-- <p>当前数字: {{ num }}</p> -->
     <input type="text" v-model="num" name="" id="">
    <button @click="num++">增加</button>
    <button @click="num>1 && num--">减少</button>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';
let num = ref(1);
// 定义一个自定义事件
let event =defineEmits(["getNum"])
// 监听num的变化  当num变化时  把最新的值传给父组件
watch(num,()=>{
  // 调用函数  ,携带数据回传   ,,父组件接收
  event("getNum",num.value)
})
</script>



<style scoped>
  p{font-size: 20px;}
</style>
