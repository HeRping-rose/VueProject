<template>
    <h1>Category Page</h1>
    <div class="cate">
        <ul>
            <li>
                <router-link to="/cate">Category 1</router-link>
            </li>
            <li>
                <router-link to="/cate/cate2">Category 2</router-link>
            </li>
            <li>
                <router-link to="/cate/cate3">Category 3</router-link>
            </li>
            <li>
                <router-link to="/cate/cate4">Category 4</router-link>
            </li>
        </ul>
        <div class="box2">
            <router-view></router-view>
        </div>
    </div>
</template>
<script setup lang="ts">

</script>


<style scoped>
    .cate {
        display: flex;
        /*  */
        justify-content: space-between; 
        /* padding: 20px; */
    }
    .cate ul{
        list-style: none;
        margin: 0;
        padding: 10px;
        background: #ccc;
        width: 150px;
        text-align: center;
    }
    .cate li {
        margin-bottom: 10px;
        padding: 10px 0;
        border-radius: 5px;
        background: #eee;
        border: 1px solid #eee;
    }

    .box2 {
        /* margin-top: 20px; */
        margin: 0;
        padding: 0;
        /* padding: 10px; */
        border: 1px solid #ccc;
        flex: 2;
    }
</style>