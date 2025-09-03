<template>
    <h1>分类列表</h1>
    <br>
    <el-table :data="tableData" style="width: 100%">

      <!-- id -->
    <el-table-column label="id" width="50">
      <template #default="scope">
        <div style="display: flex; align-items: center">
          <!-- <el-icon><timer /></el-icon> -->
          <span style="margin-left: 10px">{{ scope.row.id }}</span>
        </div>
      </template>
    </el-table-column>

    <!-- name -->
    <el-table-column label="Name" width="180">
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

    <!-- 描述 -->
    <el-table-column label="描述" width="180">
      <template #default="scope">
        <el-popover effect="light" trigger="hover" placement="top" width="auto">
          <template #default>
            <!-- <div>name: {{ scope.row.name }}</div>
            <div>address: {{ scope.row.address }}</div> -->
          </template>
          <template #reference>
            <el-tag>{{ scope.row.description }}</el-tag>
          </template>
        </el-popover>
      </template>
    </el-table-column>

    <!-- icon -->
    <el-table-column label="icon" width="180">
      <template #default="scope">
        <div style="display: flex; align-items: center">
          <!-- <span style="margin-left: 10px">{{ scope.row.icon }}</span> -->
           <!-- <el-image
            style="width: 50px; height: 50px"
            :src="scope.row.icon"
            fit="fill"
          ></el-image> -->
          <img :src="'http://127.0.0.1:8000'+scope.row.icon" width="50px" >
           <!-- <img :src=' $serverpath+scope.row.icon' width="50px" ></img> -->
        </div>
      </template>
    </el-table-column>

    <!-- description -->


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
      </template>
    </el-table-column>
  </el-table>

  <br>
  <el-pagination background layout="prev, pager, next" :total="1000" />
</template>

<script lang="ts" setup>
import { ref } from 'vue'

import { Timer } from '@element-plus/icons-vue'

interface Cate {
  id: number
  name: string
  description: string
  icon: string
  created_at: string
  updated_at: string
}
const tableData = ref<Cate[]>()

const handleEdit = (index: number, row: Cate) => {
  console.log(index, row)
}
const handleDelete = async (index: number, row: Cate) => {
  // let res = await axios.delete('/shop/cate/' + row.id)
  let res = await axios.delete('/shop/cate/' ,{ params: { id: row.id } })

  // console.log(index, row)
  console.log(res)
  // getCateList()

  tableData.value=(tableData.value)?.filter(item=>item.id!=row.id)

}


async function getCateList() {
  const res = await axios.get('/shop/cate')
  console.log(res)
  tableData.value = res.data
}

getCateList()

//测试一下接口能不能用
import axios from '@/utils/http'

async function test() {
  const res = await axios.get('/shop/cate')
  console.log(res)
}
test()

</script>