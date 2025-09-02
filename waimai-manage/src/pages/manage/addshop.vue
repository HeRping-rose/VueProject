<template>
    <h1>添加店铺</h1>
    <br>
    <div>
        <el-form
            ref="ruleFormRef"
            
            label-width="120px"
            class="demo-ruleForm"
            status-icon
        >
            <el-form-item label="店铺分类" prop="name">
                <!-- <el-input v-model="ruleForm.name"  aria-placeholder="请输入店铺分类"/> -->
                <el-select
                    v-model="value"
                    class="m-2"
                    placeholder="Select"
                    size="large"
                    style="width: 240px"
                >
                    <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                    />
                </el-select>
            </el-form-item>
            <el-form-item label="店铺名称" prop="name">
                <el-input v-model="ruleForm.name" aria-placeholder="请输入店铺名称"/>
            </el-form-item>
            

            <el-form-item label="店铺图标" prop="icon">
                <!-- <el-input v-model="ruleForm.icon" aria-placeholder="请输入店铺图标"/> -->
                <el-upload
                    class="avatar-uploader"
                    action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
                    :show-file-list="false"
                    :on-success="handleAvatarSuccess"
                    :before-upload="beforeAvatarUpload"
                >
                    <img v-if="imageUrl" :src="imageUrl" class="avatar" />
                    <el-icon v-else class="avatar-uploader-icon"><Plus /></el-icon>
                </el-upload>
            </el-form-item>

            <!-- 店铺电话 -->
            <el-form-item label="店铺电话" prop="phone">
                <el-input v-model="ruleForm.phone" aria-placeholder="请输入店铺电话"/>
            </el-form-item>
            <!-- 店铺地址 -->
            <el-form-item label="店铺地址" prop="address">
                <el-input v-model="ruleForm.address" aria-placeholder="请输入店铺地址"/>
            </el-form-item>
            <!-- 店铺活动 -->
            <el-form-item label="店铺活动" prop="activity">
                <el-input v-model="ruleForm.activity" aria-placeholder="请输入店铺活动"/>
            </el-form-item>
            <!-- 店铺营业时间 -->
             <el-form-item label="营业时间" prop="time"> 
                <el-time-picker
                    v-model="value1"
                    is-range
                    range-separator="To"
                    start-placeholder="Start time"
                    end-placeholder="End time"
                    />
             </el-form-item>
             <!-- 是否营业 -->
            <el-form-item label="是否营业" prop="status">
                <el-switch
                    v-model="value3"
                    class="ml-2"
                    style="--el-switch-on-color: #13ce66; --el-switch-off-color: #ff4949"
                />
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

const value = ref('')
const value1 = ref<[Date, Date]>([
  new Date(2016, 9, 10, 8, 40),
  new Date(2016, 9, 10, 9, 40),
])
const value3 = ref(true)

const options = [
  {
    value: 'Option1',
    label: 'Option1',
  },
  {
    value: 'Option2',
    label: 'Option2',
  },
  {
    value: 'Option3',
    label: 'Option3',
  },
  {
    value: 'Option4',
    label: 'Option4',
  },
  {
    value: 'Option5',
    label: 'Option5',
  },
]

interface RuleForm {
  category: String,
  name: String,
  icon: String,
  // description: String,
  phone: String,
  address: String,
  activity: String,
  business_hours:string,
  is_open: Boolean,
  created_at: String,
  updated_at: String,
  time: [Date, Date],
}
const ruleForm = ref<RuleForm>({
  category: '',
  name: '',
  icon: '',
  // description: '',
  phone: '',
  address: '',
  activity: '',
  business_hours: '',
  is_open: true,
  created_at: '',
  updated_at: '',
  time: [new Date(), new Date()],
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
const submitForm = async () => {
  await ruleFormRef.value?.validate((valid, fields) => {
    if (valid) {
      console.log('submit!')
      router.push('/manage')
    } else {
      console.log('error submit!', fields)
    }
  })
}
import { ElMessage } from 'element-plus'
import { Plus } from '@element-plus/icons-vue'

import type { UploadProps } from 'element-plus'

const imageUrl = ref('')

const handleAvatarSuccess: UploadProps['onSuccess'] = (
  response,
  uploadFile
) => {
  imageUrl.value = URL.createObjectURL(uploadFile.raw!)
}

const beforeAvatarUpload: UploadProps['beforeUpload'] = (rawFile) => {
  if (rawFile.type !== 'image/jpeg') {
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

.demo-range .el-date-editor {
  margin: 8px;
}

.demo-range .el-range-separator {
  box-sizing: content-box;
}
</style>