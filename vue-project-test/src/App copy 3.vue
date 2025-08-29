


<template>
  <div>
    <ul>
      <li v-for="item in goodsList" :key="item.id">
        <h3>{{ item.name }} - ${{ item.price }}</h3>
        <p>可选颜色:</p>
        <ul>
          <li v-for="color in item.colors" :key="color">
            <Button>{{ color }}</Button>
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

let goodsList=[
  {id:1, name:'商品1', price:100, colors:['red', 'blue', 'green']},
  {id:2, name:'商品2', price:200, colors:['yellow', 'purple']},
  {id:3, name:'商品3', price:300, colors:['orange']}
]

</script>

<style>

</style>
