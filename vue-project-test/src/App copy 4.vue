
<!-- 鼠标移动 移入移除 照片放大 缩小 -->

<template>

  <div>
    <img
      v-for="item in imagesList"
      :key="item.id"
      :src="item.image"
      @mouseover="handleMouseOver(item.id)"
      @mouseleave="handleMouseLeave(item.id)"
      :style="{ transform: `scale(${item.scale})` }"
    />
  </div>

</template>

<script setup lang="ts">

import { ref } from 'vue'
const imagesList = ref([
  {
    id: 1,
    image: 'https://picsum.photos/id/1/200/300',
    scale: 1
  },
  {
    id: 2,
    image: 'https://picsum.photos/id/2/200/300',
    scale: 1
  },
  {
    id: 3,
    image: 'https://picsum.photos/id/3/200/300',
    scale: 1
  }
])



const handleMouseOver = (id: number) => {
  // 放大图片
  const img = imagesList.value.find(item => item.id === id);
  if (img) {
    img.scale = 1.2;
  }
}

const handleMouseLeave = (id: number) => {
  // 缩小图片
  const img = imagesList.value.find(item => item.id === id);
  if (img) {
    img.scale = 1;
  }
}

</script>

<style>

</style>
