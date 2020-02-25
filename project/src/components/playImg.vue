<template>
  <el-carousel indicator-position="outside">
	<router-link :to="{name:'List', query:{aa:0, bb:0, cc:0, dd:0, page:1}}"><div style="width: 100%; height: 100%; "></div></router-link>
    <el-carousel-item  style="height: 350px; z-index: -1;" > <img class="im" src="../assets/banner1.jpg"/></el-carousel-item>
	<el-carousel-item  style="height: 350px; z-index: -1;"><img class="im" src="../assets/banner2.jpg"/></el-carousel-item>
	<el-carousel-item  style="height: 350px; z-index: -1;"><img class="im" src="../assets/banner3.jpg"/></el-carousel-item>
	<el-carousel-item  style="height: 350px; z-index: -1;"><img class="im" src="../assets/banner4.jpg"/></el-carousel-item>
  </el-carousel>
</template>


<style>
  .el-carousel__item h3 {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    line-height: 300px;
    margin: 0;
  }
  
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }
  
  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
  .im{
	width: 100%;
	height: 100%;
  }
</style>