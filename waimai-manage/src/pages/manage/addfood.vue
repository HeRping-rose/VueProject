<template>
    <h1>添加食品</h1>
    <br>
    <el-form :model="form" ref="formRef">
        <el-form-item label="食品分类" prop="category">
        <!-- <el-input v-model="form.category" /> -->
         <el-select v-model="form.category" placeholder="请选择分类">
           <el-option label="分类1" value="category1" />
           <el-option label="分类2" value="category2" />
           <el-option label="分类3" value="category3" />
         </el-select>
      </el-form-item>
      <el-form-item label="食品名称" prop="name">
        <el-input v-model="form.name" />
      </el-form-item>
      <!-- 食品图片 -->
      <el-form-item label="食品图片" prop="image">
        <el-upload
          class="upload-demo"
          drag
          action=""
          :on-change="handleChange"
          :file-list="fileList"
        >
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
          <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过500kb</div>
        </el-upload>
      </el-form-item>

      <!-- 食品价格 -->
      <el-form-item label="食品价格" prop="price">
        <!-- <el-input v-model="form.price" /> -->
        <el-input-number v-model="num" :min="1" :max="10" @change="handleChange" />
      </el-form-item>

      <!-- 购买数量 -->
      <el-form-item label="购买数量" prop="quantity">
        <el-input-number :disabled="true" v-model="num1" :min="1" :max="10" @change="handleChange" />
      </el-form-item>

      <!-- 是否新品 -->
      <el-form-item label="是否新品" prop="isNew">
        <el-switch v-model="value1" />
      </el-form-item>
      <!-- 是否热销 -->
      <el-form-item label="是否热销" prop="isHot">
        <el-switch v-model="value2" />
      </el-form-item>

      <!-- 食品描述 -->
      <el-form-item label="食品描述" prop="description">
        <el-input
            v-model="textarea"
            :rows="2"
            type="textarea"
            placeholder="Please input"
        />
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="handleSubmit">Submit</el-button>
      </el-form-item>
    </el-form>
</template>

<script lang="ts" setup>
import { ref } from 'vue'




const form = ref({
  name: '',
  category: '',
})
const num = ref(1)
const num1 = ref(1)
const value1 = ref(false)
const value2 = ref(false)
const handleChange = (value: number) => {
  console.log(value)
}
const fileList = ref([])
const textarea = ref('')


const handleSubmit = () => {
  console.log(form.value)
}
</script>

