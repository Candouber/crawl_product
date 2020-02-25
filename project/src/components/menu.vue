<template>
	<div >
		<router-link :to="{name:'List', query:{aa:0, bb:0, cc:0, dd:0, page:1}}">
			<div class="route-but">首页
			</div>
		</router-link>
		<router-link :to="{name:'List', query:{aa:0, bb:0, cc:0, dd:0, page:1}}">
			<div class="route-but">数据
			</div>
		</router-link>
		<router-link :to="{name:'List', query:{aa:0, bb:0, cc:0, dd:0, page:1}}">
			<div class="route-but">API
			</div>
		</router-link>
		<router-link :to="{name:'List', query:{aa:0, bb:0, cc:0, dd:0, page:1}}">
			<div class="route-but">产品介绍
			</div>
		</router-link>
		<router-link :to="{name:'List', query:{aa:0, bb:0, cc:0, dd:0, page:1}}">
			<div class="route-but">开发者模式
			</div>
		</router-link>
	</div>
		<!-- <el-menu
		class="el-menu-demo"
		mode="horizontal"
		style="height: 80px;"
		background-color="#fff"
		text-color="#008287"
		active-text-color="#008287"
		>
		<el-menu-item index="1" id="title" style="color: black; font-size: 18px; margin-right: 20px;">导航1</el-menu-item>
			<el-menu-item index="2" id="title" style="color: black; font-size: 18px; margin-right: 20px;">导航2</el-menu-item>
		<el-menu-item index="3" id="title" style="color: black; font-size: 18px; margin-right: 20px;">导航3</el-menu-item>

		</el-menu> -->
</template>

<script>
	export default{
		name:'menu'
	}
</script>

<style>
	.route-but:hover{
		background-color: white !important; 
		color: #1C9CAA !important;
	}
	.el-menu-demo{
		height: 60px !important;
	}
	.route-but{
		color: black;
		font-size: 20px;
		height: 50px;
		float: left;
		margin-left: 5px;
		margin-right: 60px;
		margin-top: 10px;
		display: inline-block;
		text-align: center;
		/* text-align: center; */
	}
	.uu li{
		float: left;
		text-decoration: none;
		list-style: none;
		display: inline;
		margin-right: 20px;
		padding-right: 20px;
	}
</style>
