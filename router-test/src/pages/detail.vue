<template>
    <h2>Detail Page</h2>
    <div>
        <!-- <p>Detail ID: {{ route.params.id }}</p> -->
        <p>Detail Query: {{ route.query.id }}</p>
    </div>
</template>

<script setup lang="ts">
import { useRoute } from 'vue-router'

const route = useRoute()
console.log(route.query.id)

// async function fetchData() {
//     const response = await fetch(`https://api.example.com/details/${route.params.id}`)
//     const data = await response.json()
//     console.log(data)
// }

// fetchData()
</script>
