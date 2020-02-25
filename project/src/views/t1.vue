<template>
	<div id="app">
		<div class="header">
			<m-header></m-header>
		</div>
		<div id="main" >
			<m-img id="hah"  v-bind:style="{width: wid+'!important'}" ></m-img>
		</div>
	<div id="side">
		<m-aside></m-aside>
	</div>
	<div>
		<m-card></m-card>
	</div>
	<div id="footer">
		<m-foot></m-foot>
	</div>
	</div>
</template>
<script>
  import aside from '../components/aside.vue'
  // import menu from '../components/menu.vue'
  import playImg from '../components/playImg.vue'
  // import logo from '../components/logo.vue'
  import card from '../components/card.vue'
  import foot from '../components/foot.vue'
  import header from '../components/header.vue'
  // var W = '1503px'
  var w = document.body.clientWidth || document.documentElement.clientWidth
  // var W = w>1500? w+'px':'1500px';
  // alert(w)
  export default {
	"name": 'Home',
	
    data() {
		
      return {
		// wid: document.body.clientWidth || document.documentElement.clientWidth,
		
		wid: w,
        activeIndex: '1',
        activeIndex2: '1'
      };
    },
	components:{
		'm-header': header,
		'm-aside':aside,
		// 'm-menu':menu,
		'm-img': playImg,
		// 'm-logo': logo,
		'm-card': card,
		'm-foot': foot
	},
	mounted() {
		// this.clientWidth.width = `${document.documentElement.clientWidth}`;
		// const that = this;
		window.onresize = function temp() {
			this.w = `${document.documentElement.clientWidth}` > 1500? `${document.documentElement.clientWidth}px` : '1500px';
			document.getElementById('hah').style.width = this.w
			// alert(this.w)
			
		};
	},

  }
</script>

<style scoped>

#side{
	top: 176px;
	height: 400px;
	width: 200px;
	margin-left: 100px;
	z-index: 1;
	position: absolute;
}

#main{
	overflow: visible;
	height: 430px;
	position: relative;
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
	height: 400px;
	overflow: hidden;
}

#footer{
	height: 80px;
	background-color: #99A9BF;
}
.header{
	height: 170px;
	width: 1500px;
	margin: auto;
	display: block;
}
</style>
