

<template>
  <div>
    <button class="login" :style="{ backgroundColor: props.color }">{{ props.title }}</button>
  </div>

</template>

<script setup lang="ts">
// 用一个数组接收 prop 不带任何的验证
// let props=defineProps(['title','color'])

// 用对象来接收 可以带一点验证  规定传的参数是String类型
// let props=defineProps({
//   title:String,
//   color:String
// })

//传默认值
let props=defineProps({
  title:{type:String, default:'按钮' ,required:true},
  color:{type:String, default:'grey' },
  num:{type:Number, default:0}
})

</script>

<style>
.login{
  width: 100px;
  height: auto;
  background-color: rgb(182, 182, 202);
  color: rgb(151, 221, 209);
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
}
.login:hover{
  background-color: rgb(96, 96, 175);
}

</style>
