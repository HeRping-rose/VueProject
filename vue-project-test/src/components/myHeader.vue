<template>
  <div class="box">
    <!-- 外部在组件对上传入的内容 需要使用<slot>插槽组件来接收 -->

    <!-- 自定义多个插槽需要命名 -->
    <slot name="left"></slot>
    <!-- 默认的插槽可以省略不写 -->
    <!-- <slot name="content"></slot> -->
    <slot ></slot>
    <slot name="right"></slot>
  </div>
</template>

<script setup lang="ts">
import { defineProps } from 'vue';

</script>


<style scoped>
.box {
  border: 1px solid #d49d9d;
  padding: 16px;
  text-align: center;
  margin-bottom: 16px;
  background-color: rgb(163, 179, 173);
  height: 50px;

  line-height: 50px;
  width: 100%;
  display: inline-block;
}
</style>
