<template>
    <h2>News Page</h2>
    <div>
        <p>News ID: {{ route.params.id }}</p>
    </div>
</template>

<script setup lang="ts">
import { useRoute } from 'vue-router'

const route = useRoute()
</script>
