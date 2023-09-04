

<template>
<el-container>
    <el-aside>目录导航</el-aside>
    <el-main>
        <div v-html="content" class="markdown-body"></div>
    </el-main>
</el-container>

</template>

<script setup>

import { useRoute } from 'vue-router';
import {onMounted, ref} from 'vue'
import Showdown from 'showdown';
import axios from 'axios';
import 'github-markdown-css/github-markdown.css'
let content = ref("")
const converter = new Showdown.Converter();
onMounted(()=>{
    const route = useRoute(); // Get the current route
    const articleId = route.params.articleId;
    axios.get('/blog/'+articleId).then(response => {
        content.value = converter.makeHtml(response.data.content)
        console.log(content.value);
    })
})
</script>

<style scoped>
@import '../assets/github-markdown.css'
/* .content {
    padding: 100px;
    padding-left: 4%;
    border: 2px solid wheat;
    background-color: aliceblue;
    color: black;
} */

</style>