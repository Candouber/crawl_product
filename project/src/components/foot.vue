<template>
	<div>
		<!-- <div class="to">
			<div class="descrip">
				<div class="innerd">
					<ul>
						<li>杭州 海创科技中心</li>
						<li> biz@shenjian.io</li>
						<li> 关于我们</li>
						<li> 加入嘿嘿嘿</li>
					</ul>
				</div>
				<img src="../assets/logo.png"/>
				<p>嘿嘿嘿（heihei.io）是一个大数据和人工智能的云操作系统。您可以在神箭手上快速开发大数据和AI应用，包括爬虫/机器学习/数据清洗/API接口等。</p>
				
			</div>
			<div class="link">
				<p>链接</p>
				<ul>
					<li>首页</li>
					<li> 次页</li>
					<li> 第三页</li>
					<li> 最后一页</li>
				</ul>
			</div>
			<div id="code">
				<div id="img">
					
				</div>
				<p>上面是个二维码 (如果我们有的话)</p>
			</div>
		</div> -->
		<div class="bo">
			<div class="zdmLogo">
				<img src="../assets/zdmlogo.png" />
				<p class="zdmP">什 么 值 得 买</p>
			</div>
			<div class="cr">浙公网安备 33011002013222号ICP证:浙B2-20180926 浙ICP备17014612号</div>
		</div>
		
	</div>
</template>

<script>
	export default{
		name:'foot'
	}
</script>

<style>
	.to{
		background-color: #262626;
		color: #999999;
		height: 320px;
		display: flex;
	}
	.bo{
		height: 120px;
		background-color: #000000;
	}
	.descrip{
		margin-left: 200px;
		line-height: 25px;
		height: 270px;
		width: 500px;
		position: relative;
		top: 20px;
		font-size: 15px;
	}
	.descrip img{
		height: 60px;
		
	}
	.descrip p{
		height: 200px;
		width: 250px;
	}
	.innerd {
		float: right;
		height: 200px;
		width: 200px;
		position: relative;
		top: 70px;
	}
	.link{
		margin-left: 50px;
		float: right;
		height: 300px;
		width: 200px;
	}
	.link p{
		font-size: 25px;
	}
	.link ul{
		margin-top: 22px;
		float: left;
		list-style: none;
		padding-inline-start:0;
	}
	.link ul li{
		margin-bottom: 5px;
	}
	#img{
		height: 200px;
		width: 250px;
		background-color: white;
	}
	#code{
		margin-top: 50px;
		float: right;
		height: 250px;
		width: 250px;
		background-color: #999999;
	}
	#code p{
		color: white;
	}
	.zdmLogo{
		color: white;
		padding-top: 25px;
		width: 300px;
		height: 80px;
		margin: auto;
	}
	.zdmLogo img{
		float: left;
	}
	.zdmP{
		position: relative;
		left: 20px;
		top: -25px;
		font-size: 30px;
	}
	.cr{
		color: white;
		width: 600px;
		margin: auto;
		position: relative;
		top: -20px;
	}
</style>
