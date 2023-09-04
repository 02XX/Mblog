<script setup>
import ArticleCard from '../components/ArticleCard.vue'
import { onMounted, ref } from 'vue'
import axios from 'axios'
const articles = ref()
onMounted(() => {
  axios.get("/blog")
  .then(response => {
    articles.value = response.data;
  })
})
</script>
<template>
    <el-container>
            <el-aside width="200px">Aside</el-aside>
            <el-main>
              <ArticleCard 
              v-for="article in articles"
              :key="article.id"
              :articleTitle="article.title" 
              :articleBrief="article.brief" :articleId="article.id"></ArticleCard>
            </el-main>
            
      </el-container>
</template>


<style scoped>
.el-aside {
  border: 2px solid red;
}
.el-main {
  border: 2px solid rgb(63, 14, 143);
}
.el-main {
  flex-direction: column;
  display: flex;
  gap: 10%;
}
#a {
  position: relative;
}
</style>