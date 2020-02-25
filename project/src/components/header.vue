<template>
	<div>
		<div id="air"></div>
		<div id="header">
			<m-logo></m-logo>
			<p class="daita">呆塔</p>
			<div class="menu">
				<div id="search">
					<m-search></m-search>
				</div>
				<div class="inner-menu">
					<m-menu></m-menu>
				</div>
			</div>
			
			<div class="ic">
				<div>
					<el-button class="a" size="medium" circle>登 录</el-button>
				</div>
				<div>
					<el-button class="a" circle>注 册</el-button>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
  import menu from '../components/menu.vue'
  import logo from '../components/logo.vue'
  import search from '../components/search.vue'
  export default {
	"name": 'Home',
    data() {
      return {
        activeIndex: '1',
        activeIndex2: '1'
      };
    },
	components:{
		'm-menu':menu,
		'm-logo': logo,
		'm-search': search
	},

  }
</script>

<style>
#air{
	height: 25px;
}
#header{
	height: 160px;
	display: flex;
	width: 1400px;
	margin-left: 100px;
}
.menu{
	float: right;
	margin-left: 350px;
	width: 800px;
	height: 100px;
	padding-top: 10px;
	/* display: flex; */
}
.ic{
	width: 200px;
	height: 60px;
	font-size: 32px;
	margin: auto;
	float: right;
}
.ic div{
	float: left;
	margin-right:20px ;
}
.a{
	top: -20px;
	height: 60px;
	width: 60px;
	font-size: 16px;
	position: relative;
}
.a:hover{
	background-color: #1C9CAA;
	color: #000000 !important;
}
.inner-menu{
	height: 30px;
	/* background-color: yellow; */
	width: 800px;
	/* margin-left: 20px; */
	margin-top: 60px;
}
#search{
	float: left;
	height: 40px;
	width: 500px;
	/* background-color: #000000; */
	float: right;
	margin-left: 200px;
	width: 800px;
	padding-top: 10px;
}
.daita{
	float: left;
	width: 5px;
	display: inline;
	position: relative;
	left: 140px;
	font-size: 30px;
	color: #1C9CAA;
	top: -20px;
}
</style>
