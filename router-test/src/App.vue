<script setup lang="ts"></script>

<template>
  <h1>Click me jump to</h1>
  <nav>
    <router-link to="/">Home</router-link>
    <!-- <router-link to="/news">News</router-link> -->
    <router-link to="/cate">Category</router-link>
    <router-link to="/list">List</router-link>
  </nav>
  <main>
    <RouterView />
  </main>
</template>

<style scoped>
nav {
  display: flex;
  gap: 20px;
  margin-top: 20px;
}
</style>
