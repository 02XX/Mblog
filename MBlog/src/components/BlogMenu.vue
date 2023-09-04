<template>
    <el-menu
        :default-active="activeIndex"
        class="main-menu"
        mode="horizontal"

        @select="handleSelect"
      >
        <el-menu-item index="1"><el-icon><Reading /></el-icon>文章</el-menu-item>
        
        <el-menu-item index="2"><el-icon><Search /></el-icon>搜索</el-menu-item>

        <el-menu-item index="3"><el-icon><Collection /></el-icon>归档</el-menu-item>

        <el-sub-menu index="4">
          <template #title>其他</template>
          <el-menu-item index="4-1">item one</el-menu-item>
          <el-menu-item index="4-2">item two</el-menu-item>
          <el-menu-item index="4-3">item three</el-menu-item>
        </el-sub-menu>
      </el-menu>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
const activeIndex = ref('1')
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
</script>

<style scoped>
* {
  font-size: 2rem;
  font-weight: bold;
}
.el-icon {
  height: 100%;
}
.el-menu {
  height: 100%;
}
:deep .el-sub-menu__title {
  font-size: 2rem;
  font-weight: bold;
}
</style>
