<template>
    <div class="manage-home">
        <div class="welcome">
            <el-icon class="welcome-icon"><User /></el-icon>
            <div>
                <h2>欢迎来到管理后台</h2>
                <p>您好，管理员！祝您工作愉快。</p>
            </div>
        </div>
        <div class="card-grid">
            <div class="card">
                <el-icon><User /></el-icon>
                <span>注册信息</span>
            </div>
            <div class="card">
                <el-icon><ShoppingCart /></el-icon>
                <span>销售信息</span>
            </div>
            <div class="card">
                <el-icon><Document /></el-icon>
                <span>订单管理</span>
            </div>
            <div class="card">
                <el-icon><Goods /></el-icon>
                <span>商品管理</span>
            </div>
            <div class="card">
                <el-icon><Star /></el-icon>
                <span>评价管理</span>
            </div>
            <div class="card">
                <el-icon><Bell /></el-icon>
                <span>通知公告</span>
            </div>
            <div class="card">
                <el-icon><Setting /></el-icon>
                <span>系统设置</span>
            </div>
        </div>
        <div class="chart-section">
            <h3>数据总览</h3>
            <div id="mainChart" class="chart-box"></div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { User, ShoppingCart, Document, Goods, Star, Bell, Setting } from '@element-plus/icons-vue'
import { onMounted } from 'vue'
import * as echarts from 'echarts'

onMounted(() => {
    const chartDom = document.getElementById('mainChart')
    if (chartDom) {
        const myChart = echarts.init(chartDom)
        myChart.setOption({
            title: { text: '本月注册与销售统计' },
            tooltip: {},
            legend: { data: ['注册', '销售'] },
            xAxis: { data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日'] },
            yAxis: {},
            series: [
                { name: '注册', type: 'bar', data: [5, 20, 36, 10, 10, 20, 15] },
                { name: '销售', type: 'bar', data: [15, 10, 26, 20, 30, 10, 25] }
            ]
        })
    }
})
</script>

<style scoped>
.manage-home {
    padding: 32px;
    background: #f6f8fa;
    min-height: 100vh;
}
.welcome {
    display: flex;
    align-items: center;
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    padding: 24px 32px;
    margin-bottom: 32px;
}
.welcome-icon {
    font-size: 48px;
    color: #67c23a;
    margin-right: 24px;
}
.welcome h2 {
    margin: 0 0 8px 0;
    font-size: 28px;
}
.welcome p {
    margin: 0;
    color: #888;
}
.card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 24px;
    margin-bottom: 40px;
}
.card {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    padding: 32px 0 24px 0;
    transition: box-shadow 0.2s;
    cursor: pointer;
}
.card:hover {
    box-shadow: 0 4px 16px rgba(0,0,0,0.12);
}
.card .el-icon {
    font-size: 40px;
    color: #409eff;
    margin-bottom: 12px;
}
.card span {
    font-size: 18px;
    font-weight: 500;
}
.chart-section {
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    padding: 24px 32px 32px 32px;
}
.chart-section h3 {
    margin-bottom: 16px;
}
.chart-box {
    width: 100%;
    height: 320px;
}
</style>