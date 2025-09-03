<template>
    <h1>添加店铺</h1>
    <br>
    <div>
        <el-form
            ref="ruleFormRef"
            :model="ruleForm"
            label-width="120px"
            class="demo-ruleForm"
            status-icon
        >
            <el-form-item label="店铺分类" prop="name">
                <!-- <el-input v-model="ruleForm.name"  aria-placeholder="请输入店铺分类"/> -->
                <el-select
                    v-model="ruleForm.category"
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
                    :auto-upload="false"
                    :show-file-list="false"
                    :on-change="onAvatarChange"
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
                    v-model="ruleForm.business_hours"
                    is-range
                    range-separator="To"
                    start-placeholder="Start time"
                    end-placeholder="End time"
                    />
             </el-form-item>
             <!-- 是否营业 -->
            <el-form-item label="是否营业" prop="status">
                <el-switch
                    v-model="ruleForm.is_open"
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
// import { formatTime } from 'element-plus/es/components/countdown/src/utils.mjs'
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import { Plus } from '@element-plus/icons-vue'
import type { UploadProps } from 'element-plus'
import axios from 'axios'
import { ru } from 'element-plus/es/locales.mjs'

const value = ref('')
const value1 = ref<[Date, Date]>([
  new Date(2016, 9, 10, 8, 40),
  new Date(2016, 9, 10, 9, 40),
])
const value3 = ref(true)

interface Options {
  value: string
  label: string
}

const options =reactive<Options[]> ([
  // {
  //   value: 'Option1',
  //   label: 'Option1',
  // },
])

interface Cate {
  id: number
  name: string
  description: string
  icon: string
  created_at: string
  updated_at: string
}


interface RuleForm {
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
const ruleForm = reactive<RuleForm>({
  category: 0,
  name: '',
  // icon: '',
  // description: '',
  phone: '',
  address: '',
  activity: '',
  business_hours: [],
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
const selectFile = ref();
let router = useRouter()
const submitForm = async () => {
  await ruleFormRef.value?.validate(async (valid, fields) => {
    if (valid) {
      console.log('submit!')
      // 提交时需要携带图片
      let formData = new FormData()
      formData.append('category',`${ruleForm.category}`)
      formData.append('name', `${ruleForm.name}`)
      formData.append('phone', `${ruleForm.phone}`)
      formData.append('address', `${ruleForm.address}`)
      formData.append('activity', `${ruleForm.activity}`)
      formData.append('business_hours', formatTime(ruleForm.business_hours))
      formData.append('is_open', `${ruleForm.is_open}`)
      if (selectFile.value) {
        formData.append('icon', selectFile.value);
      }
    
      //发请求 
      console.log(formData);

      let res = await axios.post('/shop/shop/', formData,{
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });

      console.log('submit!')
      console.log(res);
      router.push('/manage/shoplist')
    } else {
      console.log('error submit!', fields)
    }
  })
}

function formatTime(arr:string[]){
  return arr.map(i=>new Date(i)).map(i=>`${i.getHours()}:${i.getMinutes()}`).join('-')
}

// import { Option } from 'element-plus/es/components/select-v2/src/select.types.mjs'

const imageUrl = ref('')

const onAvatarChange: UploadProps['onChange'] = (file, fileList) => {
  const rawFile = file.raw; //临时图片
  selectFile.value = rawFile;
  imageUrl.value = URL.createObjectURL(file.raw!)
}
const beforeAvatarUpload: UploadProps['beforeUpload'] = (rawFile) => {
  if (!(rawFile.type == 'image/jpeg' || rawFile.type == 'image/png' ||rawFile.type == 'image/jpg' ||rawFile.type == 'image/gif' )) {
    ElMessage.error('Avatar picture must be JPG format!')
    return false
  } else if (rawFile.size / 1024 / 1024 > 2) {
    ElMessage.error('Avatar picture size can not exceed 2MB!')
    return false
  }
  return true
}

interface Res {
  code:string,
  msg:string,
  data:Cate[]
}
async function getCateList() {
  const res:Res = await axios.get('/shop/cate')
  console.log(res)
  res.data.forEach((element: Cate) => {
    options.push({
      value: element.id.toString(),
      label: element.name
    })
    ruleForm.category = element.id
  });

}

getCateList()

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