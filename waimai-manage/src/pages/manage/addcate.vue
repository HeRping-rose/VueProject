<template>
    <h1>添加分类</h1>
    <br>
    <div>
        <el-form
            ref="ruleFormRef"
            :model="ruleForm"
            :rules="rules"
            label-width="120px"
            class="demo-ruleForm"
            status-icon
        >
            <el-form-item label="分类名" prop="name">
                <el-input v-model="ruleForm.name"  aria-placeholder="请输入分类名"/>
            </el-form-item>
            <el-form-item label="分类描述" prop="description">
                <el-input v-model="ruleForm.description" aria-placeholder="请输入分类描述"/>
            </el-form-item>

            <el-form-item label="分类图标" prop="icon">
                <!-- <el-input v-model="ruleForm.icon" aria-placeholder="请输入分类图标"/> -->
                <el-upload
                    class="avatar-uploader"
                    :auto-upload="false"
                    :show-file-list="false"
                    :on-change="onAvatarChange"

                    :before-upload="beforeAvatarUpload"
                >
                    <img v-if="imageUrl" :src="imageUrl" class="avatar" />
                    <el-icon v-else class="avatar-uploader-icon"><Plus /></el-icon>
                </el-upload>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="submitForm()" style="width: 100%">立即添加</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script setup lang="ts">
// import router from '@/router'
import type { FormInstance } from 'element-plus'
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
const selectFile = ref();


interface RuleForm {
  name: String,
  description: String,
}
const ruleForm = ref<RuleForm>({
  name: '',
  description: '',
})
const rules = reactive({
    name: [
        { required: true, message: '请输入分类名', trigger: 'blur' },
        { min: 2, max: 10, message: 'Length should be 2 to 10', trigger: 'blur' },
    ],
    description: [
        { required: true, message: '请输入分类描述', trigger: 'blur' },
        { min: 6, max: 20, message: 'Length should be 6 to 20', trigger: 'blur' },
    ]
})
const ruleFormRef = ref<FormInstance>()
let router = useRouter()
import axios from '@/utils/http'
const submitForm = async () => {
  await ruleFormRef.value?.validate(async (valid, fields) => {
    if (valid) {
      console.log('submit!')
      //提交数据  带图片的提交数据  要使用到 formData
      const formData = new FormData();
      formData.append('name', ruleForm.value.name as string);
      formData.append('description', ruleForm.value.description as string);
      if (selectFile.value) {
        formData.append('icon', selectFile.value);
      }

      //发请求 
      let res = await axios.post('/shop/cate/', formData,{
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      

      console.log(res);

      // 跳转到 manage/catelist
      router.push('/manage/catelist')
    } else {
      console.log('error submit!', fields)
    }
  })
}
import { ElMessage } from 'element-plus'
import { Lightning, Plus } from '@element-plus/icons-vue'

import type { UploadProps } from 'element-plus'

const imageUrl = ref('')

// 用于单独提交
// const handleAvatarSuccess: UploadProps['onSuccess'] = (
//   response,
//   uploadFile
// ) => {
//   imageUrl.value = URL.createObjectURL(uploadFile.raw!)
// }

// const selectFile = ref<File | null>(null);
// 处理图片
// 当选择一张图片是会触发的函数 用于获取 选择到的那张临时图片
const onAvatarChange: UploadProps['onChange'] = (file, fileList) => {
  // handleAvatarSuccess({}, file)
  // file.raw 临时图片
  const rawFile = file.raw; //临时图片
  // selectFile.value = rawFile; //外部存的临时图片
  selectFile.value = rawFile;

  imageUrl.value = URL.createObjectURL(file.raw!)
}

const beforeAvatarUpload: UploadProps['beforeUpload'] = (rawFile) => {
  //验证图片类型 
  if (!(rawFile.type == 'image/jpeg' || rawFile.type == 'image/png' ||rawFile.type == 'image/jpg' ||rawFile.type == 'image/gif' )) {
    ElMessage.error('Avatar picture must be JPG format!')
    return false
  } else if (rawFile.size / 1024 / 1024 > 2) {
    ElMessage.error('Avatar picture size can not exceed 2MB!')
    return false
  }
  return true
}


</script>

<style scoped>
.avatar-uploader .avatar {
  width: 178px;
  height: 178px;
  display: block;
}
</style>

<style>

.avatar-uploader .el-upload {
  border: 1px dashed var(--el-border-color);
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: var(--el-transition-duration-fast);
}

.avatar-uploader .el-upload:hover {
  border-color: var(--el-color-primary);
}

.el-icon.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  text-align: center;
}
</style>