<template>
  <div id="app">
		<div class="header">
			<m-header></m-header>
		</div>
			<div id="main">
				<m-select :msg='msg' :nowid='nowid'></m-select>
			
			<!-- <div class="slide">
					<m-page></m-page>
			</div> -->
		</div>
	
	<div id="footer">
		<m-foot></m-foot>
	</div>
  </div>
</template>
<script>
  // import menu from '../components/menu.vue'
  // import logo from '../components/logo.vue'
  import foot from '../components/foot.vue'
  import select from '../components/select.vue'
  // import ele_card from '../components/ele_card.vue'
  import header from '../components/header.vue'
  // import page from '../components/slidePage.vue'
  export default {
	name: 'List',
	mounted() {
		this.msg = {
				a: ['全部', 'API接口', '数据'],
				b: ['全部', '免费', '收费'],
				c:['全部', '个人免费版', '个人专业版', '个人旗舰版', '企业标准版', '企业高级版'],
				d:['全部' ,'股票', '本地服务', 'MINIST', '数字', '证券', '交通', '电影', '上市公司', '经纬度', '城市'],
			};
	},
	beforeUpdate:function(){
		
	},
    data() {
      return {
		msg: this.msg,
		nowid: '0'
      };
    },
	components:{
		// 'm-aside':aside,
		// 'm-menu':menu,
		// 'm-img': playImg,
		// 'm-logo': logo,
		// 'm-card': card,
		'm-foot': foot,
		'm-select': select,
		// 'm-card': ele_card,
		'm-header': header
		// 'm-page': page
	},
	

  }
</script>

<style scoped>
#air{
	height: 25px;
}
#side{
	top: 134px;
	height: 400px;
	width: 200px;
	margin-left: 100px;
	z-index: 1;
	position: absolute;
}
#header{
	height: 100px;
	display: flex;
}
#main{
	min-height: 900px;
	z-index: 0;
}
#top {
    font-family: Helvetica, sans-serif;
    text-align: center;
    margin-left: 25%;
    width: 50%;
  
}
#title {
    font-family: Helvetica, sans-serif;
    text-align: center;
    margin-left: 50px;
    color: darkslateblue;
}
#left {
	font-family: Helvetica, sans-serif;
	text-align: center;
	margin-top: 1.25rem;
	/* background-color: #483D8B; */
	height: 25rem;
	margin-left: 12.5%;
	width: 27%;
}
#hah{
	padding: 0;
	margin: 0;
	z-index: inherit;
}
#menu{
	float: right;
	margin: auto;
	width: 70%;
	height: 90px;
	padding-top: 10px;
	display: flex;
}
#footer{
	height: 80px;
	background-color: #99A9BF;
}
.list{
	width: 1200px;
	margin: auto;
	padding-top: 10px;
}
#logo{
	position: absolute;
	left: 100px;
}
/* .slide{
	margin-bottom: 30px;
	display: flex;
	

} */
.header{
	height: 170px;
	width: 1500px;
	margin: auto;
	display: block;
}
</style>
