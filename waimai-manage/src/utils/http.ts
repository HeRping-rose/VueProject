import axios from 'axios';

// const http = axios.create({
//   baseURL: 'http://localhost:3000/api',
//   timeout: 10000,
// });
//
axios.defaults.baseURL = 'http://127.0.0.1:8000';
axios.defaults.timeout = 10000;

//拦截器
axios.interceptors.request.use(
  (config) => {
    // 在请求发送之前做些什么
    return config;
  },
  (error) => {
    // 对请求错误做些什么
    return Promise.reject(error);
  }
);

//响应拦截器
axios.interceptors.response.use(
  (response) => {
    // 对响应数据做些什么
    return response.data;
  },
  (error) => {
    // 对响应错误做些什么
    return Promise.reject(error);
  }
);

export default axios;
