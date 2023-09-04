<script setup>
import {RouterLink} from 'vue-router'
</script>

<template>
    <div>
        <router-link :to="'/'" id="home">
            小马のBlog
        </router-link>
    </div>
</template>

<style scoped>
div {
    display: flex;
    align-items: center;
    height: 100%;
}
#home {
    display: flex;
    color: black;
    font-size: 2rem;
    font-weight: bolder;
    align-items: center;
    height: 100%;
    text-decoration:none;
}
</style>