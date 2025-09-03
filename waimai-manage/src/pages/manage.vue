

<template>
  <div class="common-layout">
    <el-container>
      <el-aside width="200px">
        <!-- 侧边栏 -->
        <el-menu
        active-text-color="#000"
        background-color="#d2e5fa"
        class="el-menu-vertical-demo"
        default-active="1"
        text-color="#666"
        :router="true"
      >
        <!-- <el-menu-item index="1"> -->
        <el-menu-item index="/manage">
          <!-- <el-icon><icon-menu /></el-icon> -->
          <!-- <el-icon><House /></el-icon> -->
          <el-icon><HomeFilled /></el-icon>
          <span>首页</span>
        </el-menu-item>

        <el-sub-menu index="2">
            <!-- 一级标题 -->
          <template #title>
            <!-- <el-icon><location /></el-icon> -->
             <el-icon><Briefcase /></el-icon>
            <span>分类管理</span>
          </template>
          <!-- <el-menu-item-group title="Group One"> -->
            <el-menu-item index="/manage/addcate">添加分类</el-menu-item>
            <el-menu-item index="/manage/catelist">分类管理</el-menu-item>
          <!-- </el-menu-item-group>
          <el-menu-item-group title="Group Two">
            <el-menu-item index="1-3">item three</el-menu-item>
          </el-menu-item-group>
          <el-sub-menu index="1-4">
            <template #title>item four</template>
            <el-menu-item index="1-4-1">item one</el-menu-item>
          </el-sub-menu> -->
        </el-sub-menu>

        <el-sub-menu index="3">
            <!-- 一级标题 -->
          <template #title>
            <!-- <el-icon><location /></el-icon> -->
            <el-icon><Shop /></el-icon>
            <span>店铺管理</span>
          </template>
            <el-menu-item index="/manage/addshop">添加店铺</el-menu-item>
            <el-menu-item index="/manage/shoplist">店铺管理</el-menu-item>
        </el-sub-menu>

        <el-sub-menu index="4">
            <!-- 一级标题 -->
          <template #title>
             <el-icon><Briefcase /></el-icon>
            <span>食品管理</span>
          </template>
            <el-menu-item index="/manage/addfood">添加食品</el-menu-item>
            <el-menu-item index="/manage/foodlist">食品管理</el-menu-item>
        </el-sub-menu>
        <!-- <el-menu-item index="2">
          <el-icon><icon-menu /></el-icon>
          <span>Navigator Two</span>
        </el-menu-item>

        <el-menu-item index="3" disabled>
          <el-icon><document /></el-icon>
          <span>Navigator Three</span>
        </el-menu-item>
        <el-menu-item index="4">
          <el-icon><setting /></el-icon>
          <span>Navigator Four</span>
        </el-menu-item> -->
      </el-menu>
      </el-aside>
      <el-container>
        <el-header>
            <!-- 头部 -->
            <!-- 左边是面包屑导航 -->
            <el-breadcrumb :separator-icon="ArrowRight">
                <el-breadcrumb-item :to="{ path: '/manage' }">首页</el-breadcrumb-item>
                <el-breadcrumb-item v-for="item in $route.meta.title">{{ item }}</el-breadcrumb-item>
            </el-breadcrumb>
            <!-- 下拉菜单 -->
             <el-dropdown>
                <span class="el-dropdown-link">
                管理员管理
                <el-icon class="el-icon--right">
                    <arrow-down />
                </el-icon>
                </span>
                <template #dropdown>
                <el-dropdown-menu>
                    <el-dropdown-item>{{ username }}</el-dropdown-item>

                    <el-dropdown-item>设置</el-dropdown-item>
                    <el-dropdown-item>个人中心</el-dropdown-item>
                    <el-dropdown-item
                    @click="logout"
                    >退出</el-dropdown-item>
                    <!-- <el-dropdown-item disabled>Action 4</el-dropdown-item>
                    <el-dropdown-item divided>Action 5</el-dropdown-item> -->
                </el-dropdown-menu>
                </template>
            </el-dropdown>

        </el-header>
        <el-main>
          <router-view> </router-view> 
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script lang="ts" setup>
import { ArrowRight } from '@element-plus/icons-vue'
import { useRouter } from 'vue-router';


let username=localStorage.getItem('user')

let router=useRouter()
function logout(){
  localStorage.removeItem('token')
  localStorage.removeItem('user')
  router.push('/')
}
</script>


<style scoped>
.common-layout {
  height: 100%;
}
.el-container {
  height: 100%;
}
.el-aside {
  height: 100%;
  background-color: #d2e5fa;
}

.example-showcase .el-dropdown-link {
  cursor: pointer;
  color: var(--el-color-primary);
  display: flex;
  align-items: center;
}
.el-header{
    background-color: #eee;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

</style>