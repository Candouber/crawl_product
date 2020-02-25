<template>
	<div class="search_board">
		<div class="col">
			<div class="search_title"><p>类型</p></div>
			<div class="aair"></div>
			<div class="search_ul">
				<li v-for="(c, index1) in msg.a" v-bind:key="index1" v-bind:class="$route.query.aa==index1 ? 'change':''">
					<a v-on:click="jump(index1)">{{c}}</a>
				</li>
			</div>
		</div>
		<div class="col">
			<div class="search_title"><p>价格</p></div>
			<div class="aair"></div>
			<div class="search_ul">
				<li v-for="(c, index2) in msg.b" v-bind:key="index2" v-bind:class="$route.query.bb==index2 ? 'change':''">
					<a v-on:click="jump1(index2)">{{c}}</a>
				</li>
			</div>
		</div>
		<div class="col">
			<div class="search_title"><p>套餐</p></div>
			<div class="aair"></div>
			<div class="search_ul">
				<li v-for="(c, index3) in msg.c" v-bind:key="index3" v-bind:class="$route.query.cc==index3 ? 'change':''">
					<a id="aaa" v-on:click="jump2(index3)">{{c}}</a>
				</li>
			</div>
		</div>
		<div class="col">
			<div class="search_title"><p>分类</p></div>
			<div class="aair"></div>
			<div class="search_ul">
				<li v-for="(c, index4) in msg.d" v-bind:key="index4" v-bind:class="$route.query.dd==index4 ? 'change':''">
					<a v-on:click="jump3(index4)">{{c}}</a>
				</li>
			</div>
		</div>
		<div class="list">
			<m-card :cardMsg="cardMsg" :len="len"></m-card>
		</div>
	</div>
</template>
<script>
	import axios from 'axios'
	import ele_card from '../components/ele_card.vue'
	export default{
		name:'select',
		data(){
			return{
				aa:this.$route.query.aa, bb:this.$route.query.bb, cc:this.$route.query.cc, dd:this.$route.query.dd, page: this.$route.query.page,
				cardMsg: '',
				len: ''
				}
		},
		props:{
			msg: Object,
			nowid: String
		},
		components:{

			'm-card': ele_card,

		},

		methods:{
			jump:function(index){
				this.$router.push({name:'List', query:{aa:index, bb:this.bb, cc:this.cc, dd:this.dd, page:this.$route.query.page}})
				this.aa = this.$route.query.aa
				this.bb = this.$route.query.bb
				this.cc = this.$route.query.cc
				this.dd = this.$route.query.dd
				// axios.get('/apis/getMsg').then(function(res) {
				// 	alert(res)
				// })
				let self = this;
				axios.post('/apis/card/now',
				{
					'type1': this.aa,
					'type2': this.bb,
					'type3': this.cc,
					'type4': this.dd
				},
				).then(function(res){
					self.cardMsg = res.data
					self.len = res.data.name.length
					alert(self.len)
				})
				// const httpHandler = axios.create({
				// // headers: { "Content-Type": "application/json;charset=utf-8" }, //即将被发送的自定义请求头
				// withCredentials: false //表示跨域请求时是否需要使用凭证
				// });
				// // let uri = "api/detail_nav?sort="+this.pageSort;
				// httpHandler.get('/apis/getMsg')
				// .then(result =>{alert(result.data.AAA)})
				// .catch(error=>{alert(error.message)});
				// })
			},
			jump1:function(index){
				this.$router.push({name:'List', query:{aa:this.aa, bb:index, cc:this.cc, dd:this.dd, page:this.$route.query.page}})
				this.aa = this.$route.query.aa
				this.bb = this.$route.query.bb
				this.cc = this.$route.query.cc
				this.dd = this.$route.query.dd
				let self = this;
				axios.post('/apis/card/now',
				{
					'type1': this.aa,
					'type2': this.bb,
					'type3': this.cc,
					'type4': this.dd
				},
				).then(function(res){
					self.cardMsg = res.data
					self.len = res.data.name.length
					alert(self.len)
				})
			},
			jump2:function(index){
				this.$router.push({name:'List', query:{aa:this.aa, bb:this.bb, cc:index, dd:this.dd, page:this.$route.query.page}})
				this.aa = this.$route.query.aa
				this.bb = this.$route.query.bb
				this.cc = this.$route.query.cc
				this.dd = this.$route.query.dd
				let self = this;
				axios.post('/apis/card/now',
				{
					'type1': this.aa,
					'type2': this.bb,
					'type3': this.cc,
					'type4': this.dd
				},
				).then(function(res){
					self.cardMsg = res.data
					self.len = res.data.name.length
					alert(self.len)
				})
			},
			jump3:function(index){
				this.$router.push({name:'List', query:{aa:this.aa, bb:this.bb, cc:this.cc, dd:index, page:this.$route.query.page}})
				this.aa = this.$route.query.aa
				this.bb = this.$route.query.bb
				this.cc = this.$route.query.cc
				this.dd = this.$route.query.dd
				let self = this;
				axios.post('/apis/card/now',
				{
					'type1': this.aa,
					'type2': this.bb,
					'type3': this.cc,
					'type4': this.dd
				},
				).then(function(res){
					self.cardMsg = res.data
					self.len = res.data.name.length
					alert(self.len)
				})
			}
		}
	}
</script>

<style>
	.search_board{
		color: black;
		font-weight: 500;
		width: 1200px;
		background-color: white;
		margin: auto;
		min-height: 200px;
		box-shadow: 0 0 10px rgba(0,0,0,0.1);
	}
	.col{
		height: 50px;
		min-width: 200px;
		/* background-color: #9370DB; */
	}
	.search_title{
		background-color: #E7F5F6;
		float: left;
		text-align: center;
		height: 100%;
		/* background-color: steelblue; */
		width: 120px;
	}

	.search_title p{
		/* padding-left: 10px; */
		color: #1C9CAA;
		left: 30px;
		position: relative;
		float: left;
		position: relative;
		left: 45px;
	}
	.search_ul{
		height: 50px;
		/* background-color: #999999; */
		width: 1000px;
		float: left;
		list-style: none;
	}
	.search_ul li{
		top: 10px;
		position: relative;
		display: inline-block;
		float: left;
		margin-right: 10px;
		border-top-left-radius:5px;
		border-top-right-radius:5px;
		border-bottom-left-radius:5px;
		border-bottom-right-radius:5px;
		padding: 5px;
	}
	.search_ul a{
		color: black;
		text-decoration: none;
	}
	.change{
		background-color: #1C9CAA;
		color: white;
	}
	.change a{
		color: white;
	}
	.aair{
		height: 100%;
		width: 10px;
		float: left;
	}
</style>
