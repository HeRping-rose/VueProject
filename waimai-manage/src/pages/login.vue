<template>
    <!-- 后台管理系统登录页面 -->
     <div class="login-container">
       <div class="login-box">
         <h2 class="login-title">后台管理系统</h2>
         <el-form
            ref="ruleFormRef"
            :model="ruleForm"
            :rules="rules"
            label-width="120px"
            class="demo-ruleForm"
            status-icon
        >
            <el-form-item label="用户名" prop="username">
                <el-input v-model="ruleForm.username"  aria-placeholder="请输入用户名"/>
            </el-form-item>
            <el-form-item label="密码" prop="password">
                <el-input v-model="ruleForm.password" type="password" aria-placeholder="请输入密码"/>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="submitForm()" style="width: 100%">登录</el-button>
            </el-form-item>
        </el-form>
         
       </div>
     </div>
</template>
<script setup lang="ts">
// import router from '@/router'
// import axios from 'axios'
import axios from '@/utils/http'
import { log } from 'echarts/types/src/util/log.js'
import type { FormInstance } from 'element-plus'
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'

interface RuleForm {
  username: String,
  password: String
}
const ruleForm = ref<RuleForm>({
  username: '',
  password: ''
})
const rules = reactive({
    username: [
        { required: true, message: '请输入用户名', trigger: 'blur' },
        { min: 2, max: 10, message: 'Length should be 2 to 10', trigger: 'blur' },
    ],
    password: [
        { required: true, message: '请输入密码', trigger: 'blur' },
        { min: 2, max: 20, message: 'Length should be 2 to 20', trigger: 'blur' },
    ]
})
const ruleFormRef = ref<FormInstance>()
let router = useRouter()
interface Res {
  user: User
  msg: string
  token: string
}

interface User {
  avatar: string
  email: string
  id: number
  nickname: string
  phone: string
  username: string
}
const submitForm = async () => {
  await ruleFormRef.value?.validate(async (valid, fields) => {
    if (valid) {
      console.log('submit!')
      let res:Res = await axios.post('/user/login/', ruleForm.value)

      console.log(res);
      

      // router.push('/manage')
      localStorage.setItem('token', res.token)
      localStorage.setItem('user', JSON.stringify(res.user))

      router.push('/manage')

    } else {
      console.log('error submit!', fields)
    }
  })
}


</script>

<style>
.login-container {
  
  width: 100%;
  height: 100%;
  position: fixed;
  left: 0;
  top: 0;
  background-color: rgb(210, 229, 250);
}
.login-box {
  width: 400px;
  padding: 20px;
  background-color: #fff;
  padding: 15px;
  position: absolute;
  left: 0;
  right: 0;
  top: 50%;
  margin: auto;
  transform: translateY(-50%);
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}
.login-title {
  text-align: center;
  margin-bottom: 20px;
}
</style>