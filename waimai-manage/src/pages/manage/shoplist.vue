
<template>
    <h1>店铺列表</h1>
    <br>
    <el-table :data="tableData" style="width: 100%">
    <el-table-column label="ID" width="180">
      <template #default="scope">
        <div style="display: flex; align-items: center">
          <el-icon><timer /></el-icon>
          <span style="margin-left: 10px">{{ scope.row.id }}</span>
        </div>
      </template>
    </el-table-column>
    <!-- 店铺名称 -->
    <el-table-column label="店铺名称" width="180">
      <template #default="scope">
        <el-popover effect="light" trigger="hover" placement="top" width="auto">
          <template #default>
            <div>name: {{ scope.row.name }}</div>
            <div>address: {{ scope.row.address }}</div>
          </template>
          <template #reference>
            <el-tag>{{ scope.row.name }}</el-tag>
          </template>
        </el-popover>
      </template>
    </el-table-column>

    <!-- 店铺图片 -->
    <el-table-column label="店铺图片" width="180">
      <template #default="scope">
        <div style="display: flex; align-items: center">
          <img :src="'http://127.0.0.1:8000'+scope.row.image" alt="店铺图片" style="width: 100%; max-width: 100px; height: auto;" />
        </div>
      </template>
    </el-table-column>

    <!-- 店铺电话 -->
    <el-table-column label="店铺电话" width="180">
      <template #default="scope">
        <span>{{ scope.row.phone }}</span>
      </template>
    </el-table-column>

    <!-- 操作 -->
    <el-table-column label="操作">
      <template #default="scope">
        <el-button size="small" @click="handleEdit(scope.$index, scope.row)"
          >编辑</el-button
        >
        <el-button
          size="small"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)"
          >删除</el-button
        >
        <el-button
          size="small"
          type="primary"
          @click="handleDelete(scope.$index, scope.row)"
          >添加食品</el-button
        >
        <el-button
          size="small"
          @click="handleDelete(scope.$index, scope.row)"
          >食品列表</el-button
        >
      </template>
    </el-table-column>
  </el-table>

  <br>
  <el-pagination background layout="prev, pager, next" :total="1000" />
</template>

<script lang="ts" setup>
import router from '@/router'
import { Timer } from '@element-plus/icons-vue'
import axios from 'axios'
import { ref } from 'vue'

interface User {
  date: string
  name: string
  address: string
}

const handleEdit = (index: number, row: Shop) => {
  console.log(index, row)
}
const handleDelete = (index: number, row: Shop) => {
  console.log(index, row)
}
//添加食品
const handleAddFood = (index: number, row: Shop) => {
  console.log(index, row)

  router.push({ name: '/manage/addfood', params: { shopId: row.id } })
}

// const tableData: User[] = [
//   {
//     date: '2016-05-03',
//     name: 'Tom',
//     address: 'No. 189, Grove St, Los Angeles',
//   },
// ]
interface Shop{
  id: number,
  category: number,
  name: String,
  // icon: String,
  // description: String,
  phone: String,
  address: String,
  activity: String,
  business_hours:string[],
  is_open: Boolean,
  created_at: String,
  updated_at: String,
  time: [Date, Date],
}

const tableData = ref<Shop[]>()
async function getShopList() {
  const res = await axios.get('/shop/shop')
  tableData.value = res.data
  console.log(res)

}

getShopList()

</script>