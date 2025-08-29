<template>
  <div>
    <button @click="myHeight++">change</button>
    <button @click="myColor = 'blue'">changeColor</button>

    <div class="box" :style="{height: `${myHeight}px`, background: `${myColor}`}">你好呀</div>

  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

let myHeight = ref(100)
let myColor = ref('red')

</script>

<style scoped>
.box{
  width: 100px;
  height: 100px;
  background: #6e6666;
}
</style>