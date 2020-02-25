<template>
<div>
	<div class="header">
		<m-header></m-header>
	</div>








<div style="height: 12px;"></div>
<div style="margin: auto; width: 1350px">
	

	<el-container>
	  <!-- <div :class="{hasFixed: needFixed}"> -->
	  <div>
		  <div style="width: 300px">
		  <el-col :span="20">
			  
			  <h4 style="margin-top: 0px; margin-bottom: 18px; text-align: left;padding-left: 19px; color: #606266;">{{pageSort + "相关的接口"}}</h4>
			  <el-scrollbar >
		      <el-menu class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose">
				<router-link v-for="(items, idx) in navInfo" :to="items.to" style="width: 300px; text-decoration: none; color: #1c9caa;" target="_blank" :key="idx">
					<el-menu-item  style="text-align: left;">
						  <a style="width: 300px; text-decoration: none; color: #1c9caa;">{{items.name }}</a>
					</el-menu-item>
				</router-link>
				
		      </el-menu>
			  </el-scrollbar>
		    </el-col>
		  </el-row>
		  </div>
	  </div>
	  
	 <!-- <div style="width: 300px" v-show="needFixed"></div> -->
	



	<div style="width: 1000px;">
		<el-row :gutter="20">
		  <el-col :span="24" :offset="0"><div class="el-col" style="text-align: left; margin-left: 5px;">
		  <!-- <a href="/">数据抓取平台</a>><a href="">京东</a>>基本信息 -->
		  <!-- <router-link to="/detail?sort=京东&api=1" target="_blank">hahhahahah</router-link> -->
		  <el-breadcrumb separator-class="el-icon-arrow-right">
			<el-breadcrumb-item :to="{ path: '/', target: '_blank'}" target="_blank">首页</el-breadcrumb-item>
			<el-breadcrumb-item :to="{ path: '/List?aa=0&bb=0&cc=0&page=1&dd='+pageSort, target: '_blank'}">{{pageSort}}</el-breadcrumb-item>
			<el-breadcrumb-item>{{pageAPI}}</el-breadcrumb-item>
		  </el-breadcrumb>
		  
		  </div>
		  </el-col>
		
		
		</el-row>	
		<el-row>
		<div >
			<el-col :span="12" style="text-align: left;" :offset="0">
				<img src="../../static/API.png" style="width: 46%; height: 55%;">
			</el-col>
			<el-col :span="10" style="text-align: left;">
				<el-row>
					<el-col :span="24">
						<div style="vertical-align: top;">
							<span style="font-size: 25px;">{{baseInfo.useful}}  </span>
							<sup style="display: inline; text-align: center; font-size: 0.3em; padding: 2px; color: #FFFFFF; background-color: #1c9caa;">{{baseInfo.apiType}}</sup>
						</div>
					</el-col>
				</el-row>
				
				<el-row>
					<span style="font-size: 0.8em;">{{baseInfo.produce}}</span>
				</el-row>
				<el-row :gutter="20">
					<el-col :span="10">
						<span style="font-size: 0.8em;">版本： {{baseInfo.version}}</span>
					</el-col>
					<el-col :span="10">
						<span style="font-size: 0.8em;">上架时间： {{baseInfo.creatTime}}</span>
					</el-col>
				</el-row>
				<el-row :gutter="20">
					<el-col :span="10">
						<span style="font-size: 0.8em;">热度： {{baseInfo.hot}}</span>
					</el-col>
					<el-col :span="10">
						<span style="font-size: 0.8em;">更新时间： {{baseInfo.updateTime}}</span>
					</el-col>
				</el-row>
				<!-- 点击的按钮 -->
				<el-row :gutter="20">
					<el-col :span="10">
						<a @click="goAnchor('#directions')">
							<el-button round  ><i class="el-icon-document"></i> 使用说明</el-button>
						</a>
					</el-col>
					<el-col :span="10">
						<router-link @mouseenter="useOffOne" @mouseleave="useOffOne" :to="'/use?sort='+pageSort + '&api=' + pageAPI">
							<el-button round type="primary"><i class="el-icon-video-play"></i> 开始使用</el-button>
						</router-link>
					</el-col>
				</el-row>
			</el-col>
		</div>
		</el-row>
		
		
		
		<el-row :gutter="20" style="margin-bottom: 0px;">
		  <el-col :span="24" :offset="0" class="" style="border-radius: 0px; padding-top: 0.5em; padding-bottom: 0.5em;">
				<div id="directions" style="text-align: left;" >
					<h3 style="display: inline; color: #606266;" >使用说明</h3>
				</div>
		  </el-col>
		</el-row>
		
		<el-row :gutter="20">
		  <el-col :span="24" :offset="0">
			<el-tabs v-model="activeName" type="card" @tab-click="handleClick">
				
				
				
				
				<el-tab-pane label="调用说明" name="first">
					<el-row>
						<el-row :style="tapPageTitle">
							<el-col :span="24" style="text-align: left; padding-top: 3px; padding-bottom: 3px;" class="bg-purple-light">
								<span style="margin-left: 5px;">请求</span>
							</el-col>
						</el-row>
						<el-row>
							<el-col>
								<p :style="tapPageLine">API地址：{{baseInfo.requestInfo.uri}}</p>
								<hr style='background-color:#DCDFE6; height:1px; border:none;'>
								<p :style="tapPageLine">数据格式：{{baseInfo.requestInfo.struct}}</p>
								<hr style='background-color:#DCDFE6; height:1px; border:none;'>
								<p :style="tapPageLine">请求方法：{{baseInfo.requestInfo.method}}</p>
								<hr style='background-color:#DCDFE6; height:1px; border:none;'>
								<p :style="tapPageLine">DEMO：{{baseInfo.requestInfo.demo}}</p>
								<hr style='background-color:#DCDFE6; height:1px; border:none;'>
							</el-col>
						</el-row>
					</el-row>
					<el-row>
						<el-row :style="tapPageTitle">
							<el-col :span="24" style="text-align: left; padding-top: 3px; padding-bottom: 3px;" class="bg-green">
								<span style="margin-left: 5px;">参数</span>
							</el-col>
						</el-row>
						<el-row>
							<el-col>
								<el-table :data="baseInfo.requestInfo.data" style="margin-bottom: 20px;" row-key="id" border default-expand-all :tree-props="{children: 'children', hasChildren: 'hasChildren'}">
									<el-table-column prop="key" label="字段" sortable></el-table-column>
									<el-table-column prop="name" label="名称" sortable></el-table-column>
									<el-table-column prop="type" label="类型" sortable></el-table-column>
									<el-table-column prop="comment" label="注释" sortable>
									</el-table-column>
								</el-table>
							</el-col>
						</el-row>
					</el-row>
					<el-row>
						<el-row :style="tapPageTitle">
							<el-col :span="24" style="text-align: left; padding-top: 3px; padding-bottom: 3px;" class="bg-purple-light">
								<span style="margin-left: 5px;">响应</span>
							</el-col>
						</el-row>
						<el-row>
							<el-col>
								<el-table :data="baseInfo.requestInfo.return" style="margin-bottom: 20px;" row-key="id" border default-expand-all :tree-props="{children: 'children', hasChildren: 'hasChildren'}">
									<el-table-column prop="key" label="字段" sortable></el-table-column>
									<el-table-column prop="name" label="名称" sortable></el-table-column>
									<el-table-column prop="type" label="类型" sortable></el-table-column>
									<el-table-column prop="comment" label="注释" sortable>
										<template slot-scope="scope"> <a @click="showFileds(scope.row.comment)">{{scope.row.comment}}</a> </template>
									</el-table-column>
								</el-table>
							</el-col>
						</el-row>
					</el-row>
				</el-tab-pane>
				
				
				<el-tab-pane label="字段说明" name="second" style="text-align: left;">
					<el-button @click="jsonShow = true;">JSON示例</el-button>
					<el-button @click="jsonShow = false;">字段意义</el-button>
					<json-viewer v-show="jsonShow" :value="baseInfo.jsonExample" :expand-depth=10 copyable sort theme="my-awesome-json-theme"></json-viewer>
					<div v-show="!jsonShow">
						<el-table :data="baseInfo.filedMean" style="margin-bottom: 20px;" row-key="id" border default-expand-all :tree-props="{children: 'children', hasChildren: 'hasChildren'}">
							<el-table-column prop="key" label="字段" sortable></el-table-column>
							<el-table-column prop="name" label="名称" sortable></el-table-column>
							<el-table-column prop="type" label="类型" sortable></el-table-column>
							<el-table-column prop="comment" label="注释" sortable></el-table-column>
						</el-table>
					</div>
				</el-tab-pane>
				
				
				<el-tab-pane label="版本信息" name="third">
					<el-row>
						<el-row :style="tapPageTitle">
							<el-col :span="24" style="text-align: left; padding-top: 3px; padding-bottom: 3px;" class="bg-purple-light">
								<span style="margin-left: 5px;">  介绍  </span>
							</el-col>
						</el-row>
						<el-row>
							<el-col>
								<p :style="tapPageLine">功能：{{baseInfo.useful}}</p>
								<p :style="tapPageLine">版本：{{baseInfo.version}}</p>
								<p :style="tapPageLine">上线时间：{{baseInfo.creatTime}}</p>
								<p :style="tapPageLine">热度：{{baseInfo.hot}}</p>
							</el-col>
						</el-row>
					</el-row>
					<el-row>
						<el-row :style="tapPageTitle">
							<el-col :span="24" style="text-align: left; padding-top: 3px; padding-bottom: 3px;" class="bg-purple-light">
								<span style="margin-left: 5px;">  最新更新  </span>
							</el-col>
						</el-row>
						<el-row>
							<el-col>
								<p :style="tapPageLine">更新时间：{{baseInfo.update.new.updateTime}}</p>
								<p :style="tapPageLine">更新内容：{{baseInfo.update.new.updateInfo}}</p>
								
							</el-col>
						</el-row>
					</el-row>
					<el-row v-if="baseInfo.update.history&&baseInfo.update.history.length > 0">
						<el-row :style="tapPageTitle">
							<el-col :span="24" style="text-align: left; padding-top: 3px; padding-bottom: 3px;" class="bg-purple-light">
								<span style="margin-left: 5px;">  历史更新  </span>
							</el-col>
						</el-row>
						<el-row>
							<el-col>
								<div v-for="(item, index) in baseInfo.update.history" :key="index">
									<p :style="tapPageLine" >更新时间：{{item.updateTime}}</p>
									<p :style="tapPageLine">更新内容：{{item.updateInfo}}</p>
									<el-divider v-if="baseInfo.update.history.length-index > 1"><i class="el-icon-refresh"></i></el-divider>
								</div>
							</el-col>
						</el-row>
					</el-row>
					
				</el-tab-pane>
			</el-tabs>
		  </el-col>
		</el-row>
		

	</div>

	</el-container>


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
	import axios from 'axios'

	function getM_info (url) {
			return new Promise((resolve, reject) => {
			
			// axios.post(url, QS.stringify(params))
			const httpHandler = axios.create({
				// headers: { "Content-Type": "application/json;charset=utf-8" }, //即将被发送的自定义请求头
				withCredentials: false //表示跨域请求时是否需要使用凭证
			});
			// let uri = "api/detail_nav?sort="+this.pageSort;
			httpHandler.get(url)
			.then(result =>{resolve(result.data)})
			.catch(error=>{reject(error.message)});
			})
		};
	
	export default {
	  name: 'contains_test',
	  data () {
	    return {
			"pageSort": this.$route.query["sort"],
			"pageAPI": this.$route.query["api"],
			"activeName": "first",
			"itemsImg":"../../build/logo.png",
			"introduce": false,
			"searchOn": true,
			"useApi": true,
			"useThis":false,
			"baseInfo": {}, /// baseinfo这里结束
			"navInfo":[],
			
			
				
			"needFixed" : false,
			"jsonShow": true,
			"tapPageTitle": {marginBottom: '3px',},
			"tapPageLine": {
				"text-align": 'left',
				"margin-top": "3px",
				"margin-left": "3px",
				"marginBottom": '0.3em',
				"font-size": "15px"
			},
			
			
			
			
		};},// data 在这里结束
		 
	  mounted() {
		// window.addEventListener('scroll', this.handleScroll)
		let self = this;
		getM_info("api/detail_nav?sort="+this.pageSort).then(function(fulfilled){
			self.navInfo = fulfilled.data
		}).catch(function(rejected){self.navInfo = [];});
		
		getM_info("api/detail_base?sort="+this.pageSort + "&api=" + this.pageAPI).then(function(fulfilled){
			self.baseInfo = fulfilled
			console.log(fulfilled)
		}).catch(function(rejected){self.baseInfo = {};});
		
	  },
	  destroyed () {
		window.removeEventListener('scroll', this.handleScroll)
	  },
	   
	  props: {"aaa":String},
	  methods: {
		  searchOffOne: function(){
			  this.searchOn = !this.searchOn;
			  this.introduce = !this.introduce;
			  // alert(999)
		  },
		  useOffOne: function(){
			  this.useApi = !this.useApi;
			  this.useThis = !this.useThis;
		  },
		  goAnchor: function(name) {
			  document.querySelector(name).scrollIntoView(true);
			  
		  },
		  showFileds: function(comment) {
			  if (comment.search("字段说明") < 0) {return};
			  this.activeName = "second";
			  this.jsonShow = false;
			  // console.log(this.$route.query["aaa"]);
			  
		  },
		  handleOpen(key, keyPath) {
			  console.log(key, keyPath);
			},
		  handleClose(key, keyPath) {
			  console.log(key, keyPath);
			},
		  handleScroll() {
				let scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
			   console.log(scrollTop)
			   if (scrollTop > 1) {
				  this.needFixed = true;
			   } else {
				  this.needFixed = false;
			   }
			   console.log(this.needFixed)
		  },
		  
		handleClick(){
			
		}
		
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
	}
</script>

<style scoped>
	#air{
		height: 25px;
	}
	
	#header{
		height: 100px;
		display: flex;
	}
	
	#menus{
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
	
	
	.hasFixed {
	   position: fixed;
	   margin: auto 0px;
	   /* // z-index: 1000; */
	   width: 1500px; 
	}
	  
	
.el-row {
	    margin-bottom: 20px;
	    &:last-child {
	      margin-bottom: 0;
	    }
	  }
	  .el-col {
	    border-radius: 4px;
	  }
	  .bg-purple-dark {
	    background: #99a9bf;
	  }
	  .bg-purple {
	    background: #d3dce6;
	  }
	  .bg-purple-light {
	    /* background: #e5e9f2; */
		background: #E7F5F6;
		color: #1c9caa;
		font-family: "思源黑体";
		font-size: 18px;
		font-weight: bold;
	  }
	  .bg-green {
		/* #E7F5F6  */
		background: #E7F5F6;
		color: #1c9caa;
		font-family: "思源黑体";
		font-size: 18px;
		font-weight: bold;
	  }
	  .grid-content {
	    border-radius: 4px;
	    min-height: 36px;
	  }
	  .row-bg {
	    padding: 10px 0;
	    background-color: #f9fafc;
	  }
	

.el-header {
    /* background-color: #B3C0D1; */
    color: #333;
    text-align: left;
    line-height: 60px;
  }
  .el-footer {
      background-color: #B3C0D1;
      color: #333;
      text-align: center;
      line-height: 60px;
    }
  
  .el-aside {
    /* background-color: #D3DCE6; */
    /* color: #333; */
    text-align: center;
    line-height: 200px;
  }
  
  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 160px;
  }
  
  body > .el-container {
    margin-bottom: 40px;
  }
  
  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }
  
  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }
	
	
	
</style>
  
<style lang="scss" scoped="scoped">
	@import "../font/font.css";
	
	/deep/ .el-scrollbar__wrap {
	  height: 100vh;
	  overflow-x: hidden;
	  
	}
	
	
	/deep/ .el-tabs__item:hover {
		color: #1c9caa;
	}
	/deep/ .el-tabs__item.is-active {
		background: #1c9caa;
		color: #FFFFFF;
		font-family: "思源黑体";
	}
	/deep/ .el-button--default:hover {
		color: #1c9caa;
	}
	/deep/ .el-button--default:focus {
		background: #1c9caa;
		color: #FFFFFF;
		font-family: "思源黑体";
	}
	
	/deep/ .el-button--primary {
	 background: #ED958D;
	 color: #FFFFFF;
	 font-family: "思源黑体";
	 border-color: #FFFFFF;
	}
	
	
	/deep/ .el-menu-item:hover {
		color: #1c9caa;
		outline: 0;
		background: #E7F5F6;
	}
	
	/deep/ .el-menu-item:focus {
		background: #E7F5F6;
		color: #1c9caa;
		font-family: "思源黑体";
		font-weight: bold;
		outline: 0;
	}
	
	/deep/ .el-breadcrumb__inner:hover {
		color: #1c9caa;
	}
	
	/deep/ .el-input__inner:focus {
		border-color: #1c9caa;
	}
	
	
	/deep/ .el-textarea__inner:focus {
		border-color: #1c9caa;
	}
	
	
	/deep/ .my-awesome-json-theme {
	  background: #fbfbfb;
	  white-space: nowrap;
	  color: #525252; 
	  font-size: 16px;
	  font-family: Consolas, Menlo, Courier, monospace;
	
	  .jv-ellipsis {
	    color: #999;
	    background-color: #eee;
	    display: inline-block;
	    line-height: 0.9;
	    font-size: 0.9em;
	    padding: 0px 4px 2px 4px;
	    border-radius: 3px;
	    vertical-align: 2px;
	    cursor: pointer;
	    user-select: none;
	  }
	  .jv-button { color: red }
	  .jv-key { color: #92278f ; font-weight:bold}
	  .jv-item {
	    &.jv-array { color: #111111 }
	    &.jv-boolean { color: #fc1e70 }
	    &.jv-function { color: #067bca }
	    &.jv-number { color: #fc1e70 }
	    &.jv-object { color: #111111 }
	    &.jv-undefined { color: #e08331 }
	    &.jv-string {
	      color: #42b983;
	      word-break: break-word;
	      white-space: normal;
	    }
	  }
	  .jv-code {
	    .jv-toggle {
	      &:before {
	        padding: 0px 2px;
	        border-radius: 2px;
	      }
	      &:hover {
	        &:before {
	          background: #eee;
	        }
	      }
	    }
	  }
	}
	
	
</style>
