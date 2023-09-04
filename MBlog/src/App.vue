<script setup>
import BlogMenu from './components/BlogMenu.vue'
import LogoHome from './components/LogoHome.vue';
import {ref} from 'vue'
import axios from 'axios';
axios.defaults.baseURL = 'http://127.0.0.1:8000';
</script>

<template>
  <div class="common-layout">
    <el-container>
      <el-header>
          <LogoHome id="logo-home"></LogoHome>
          <BlogMenu id="blog-menu"></BlogMenu>
      </el-header>
      <RouterView></RouterView>
    </el-container>
  </div>
</template>
<style scoped>
.common-layout {
  height: 100%;
}
div > .el-container {
  height: 100%;
}
.el-header {
  flex-direction: row;
  display: flex;
  justify-content: space-between;
  background-color: white;
  /* height: 6.25%; */
  width: 100vw;
}
#blog-menu {
  width: 50%;
  justify-content: end;
  gap: 5%;
}
</style>



