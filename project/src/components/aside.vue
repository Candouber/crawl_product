<template>
	<div class="menuDiv">
			<ul>
				<li v-for="x in msg" v-bind:key="x.id">
					<a href="#">{{x.title}}</a>
					<div class="stext">
						<div class="title">
							<p>
							{{x.title}}
							<p id="line">________________________</p>
							
						</div>
						<div class="con">
							<ul>
								<li v-for="i in x.con" v-bind:key="i.id"><router-link :to="{name:'List', query:{aa:0, bb:0, cc:0, dd:0, page:1}}">{{i}}</router-link></li>
							</ul>
						</div>
						
					</div>
			</li> 

			</ul>
		</div>
</template>

<script>
	export default{
		name: 'aside',
		data(){
			return{
				msg:[
					{title: '淘宝', con: ['优惠券', '价格', '商品', '店铺', '促销']},
					{title: '京东', con:  ['优惠券', '价格', '商品', '店铺', '促销']},
					{title: '新浪', con: ['KFC', 'MC', 'BurgerKing', '李白', 'LiBai', '陶渊明', 'Peach']},
					{title: '抖音', con: ['hi', 'world', 'hello']},
					{title: '新浪新闻', con: ['morning', 'evening', 'afternoon']},
					{title: '今日头条', con: ['KFC', 'MC', 'BurgerKing']},
					{title: '美团', con: ['hi', 'world', 'hello', 'what', 'how', 'dare', '嘿嘿', '吃饭', '睡觉', '工作', 'evening', 'afternoon', 'KFC', 'MC', 'BurgerKing', '李白', 'LiBai', '陶渊明', 'Peach']},
					{title: '微信', con: ['morning', 'evening', 'afternoon', '今天', '昨天', '明天', '黑天', '白天', 'Steven', 'James','KFC', 'MC', 'BurgerKing', '李白', 'LiBai', '陶渊明', 'Peach','hi', 'world', 'hello', 'what', 'how', 'dare', '嘿嘿', '吃饭',]},
				]
			}
		}
	}
</script>

<style>
		.menuDiv { 
			height: 400px;
			width: 200px;
			border:  solid #f5f5f5;
			overflow: visible; 
			background: #fcfcfc;
			box-shadow: 0 0 40px rgba(0,0,0,0.2);
		}

		/* 去掉a标签的下划线 */
		.menuDiv a {
			text-decoration: none;
		}

		/* 设置ul和li的样式 */
		.menuDiv ul , .menuDiv li {
			list-style: none;
			margin: 0;
			padding: 0;
			width: 100px;
			float: left;
		} 

		.menuDiv > ul > li:hover ul {
			display: block;
		}

		/* 一级菜单 */
		.menuDiv > ul > li > a {
			width: 200px;
			line-height: 60px;
			background-color: #fcfcfc;
			text-align: center;
			color: black;
			font-size: 18px;
			/* border-left: 1px solid #bbf; */
			display: block;
		}

		/* 在一级菜单中，第一个不设置左边框 */
		.menuDiv > ul > li:first-child > a {
			border-left: none;
		}

		/* 在一级菜单中，鼠标放上去的样式 */
		.menuDiv > ul > li > a:hover {
			/* color: mediumpurple; */
			background-color: #1C9CAA;
		}

		.stext{
			background-color: #fff;
			top: 0;
			left: 200px;
			min-height: 400px;
			width: 300px;
			overflow: hidden;
			display: none;
			position: absolute;
			border:1px solid  #ececec;
			box-shadow: 0 0 10px rgba(0,0,0,0.1);
			
		}

		.menuDiv > ul > li:hover .stext {
			display: block;
		}
		.title{
			color: #1C9CAA;
			font-size: 20px;
			text-shadow: 0px 1px #AA44FF;
			position: relative;
			left: 20px;
			top: -7px;
		}
		#line{
			position: relative;
			top: -30px;
			text-shadow: none;
			color: #99A9BF;
		}
		.con{
			height: 200px;
			position: relative;
			top: -30px;
			left: 20px;
		}
		.con ul{
			width: 270px;
		}
		.con ul li{
			width: 90px;
			line-height: 25px;
			float: left !important;
			display: inline-block !important;
			
		}
		.con ul li a{
			color: black;
		}
		.con ul li a:hover{
			color: #1C9CAA;
		}
		.menuDiv > ul > li > a:hover::before, a:hover::after { position: relative; }
		.menuDiv > ul > li > a::before { content: "\5B"; left: 0px; visibility: hidden;}
		.menuDiv > ul > li > a::after { content: "\5D"; right:  0px;  visibility: hidden;}
		.menuDiv > ul > li > a:hover::before { content: "\5B"; left: -20px; visibility: visible; transition-duration: 1s;}
		.menuDiv > ul > li > a:hover::after { content: "\5D"; right:  -20px;  visibility: visible; transition-duration: 1s;}
</style>
