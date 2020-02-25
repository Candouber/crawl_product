<template>
<div>
		
	<el-row type="flex" class="row-bg" justify="space-between" style="padding: 14px 0px; margin-top: 0px; border-bottom: 1px solid #ededed;">
		<router-link to="/">
		<div style="display: inline; padding-left: 10px; ">
			<!-- <h1 style="display: inline;">工作台</h1> -->
			
			<img src="../../static/log1111o.png" alt="" width="50px" height="50px"> 
			<p style="margin-top: 0px; margin-bottom: 0px; margin-left: 6px;width: 20px; height: 50px; display: inline-block;vertical-align:top; font-size: 18px;font-weight: bold;color: #1c9caa;">呆塔</p>
		</div>
		</router-link>
	  <!-- <el-col :span="6" :offset="0"><h1 style="display: inline;">LOGO</h1></el-col> -->
		<p class="usertitle"><span >{{username}}的工作台</span></p>
		<div style="display: flex;justify-content: space-between;align-items: center; width: 100px; padding-right: 50px;">
		  
		<el-button type="text" style="font-size: 25px;" class="hoverButton">
				<!-- <el-tooltip class="item" effect="dark" content="GITHUB" placement="top" :hide-after="hide"> -->
				<!-- <i><i class="fab fa-github"></i></i> -->
				<!-- </el-tooltip> -->
		</el-button>
				  
			<el-dropdown trigger="click" >
			
			<el-button type="text" class="hoverButton" style="font-size: 25px;">
		  	    <el-tooltip class="item" effect="dark" content="更多" placement="top" :hide-after="hide" >
				<i class="el-icon-more" ></i>
		  	  </el-tooltip>
			</el-button>
			
		  	<el-dropdown-menu slot="dropdown">
		  	  <el-dropdown-item ><router-link to="/" >个人中心</router-link></el-dropdown-item>
		  	  <el-dropdown-item ><router-link to="/" >退出</router-link></el-dropdown-item>
		  	</el-dropdown-menu>
		</el-dropdown>
		
		  
	  </div>
	</el-row>
	
	<el-row type="flex" style="margin-top: 0px;">
		
	<!-- <el-col  class="el-menu-vertical-demo" > -->
	
	
	
	<el-menu default-active="1-4-1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" :collapse="isCollapse" style="height: 100vh;">
	  <el-menu-item index="0" @click="isCollapse=!isCollapse" style="text-decoration: none; color: #1c9caa;">
		<i class="el-icon-d-arrow-right" v-if="isCollapse" style="color: #1c9caa;"></i>
		<span slot="title" v-if="isCollapse">展开</span>
		<i class="el-icon-d-arrow-left" v-if="!isCollapse" style="color: #1c9caa;"></i>
		<span slot="title" v-if="!isCollapse" >收起</span>
	  </el-menu-item>
	  
	  <!-- <el-submenu index="1">
	    <template slot="title">
	      <i class="el-icon-location"></i>
	      <span slot="title">导航一</span>
	    </template>
	    <el-menu-item-group>
	      <span slot="title">分组一</span>
	      <el-menu-item index="1-1">选项1</el-menu-item>
	      <el-menu-item index="1-2">选项2</el-menu-item>
	    </el-menu-item-group>
	    <el-menu-item-group title="分组2">
	      <el-menu-item index="1-3">选项3</el-menu-item>
	    </el-menu-item-group>
	    <el-submenu index="1-4">
	      <span slot="title">选项4</span>
	      <el-menu-item index="1-4-1">选项1</el-menu-item>
	    </el-submenu>
	  </el-submenu> -->
	  <el-menu-item index="1" style="text-decoration: none; color: #1c9caa;">
		<a href="/" style="text-decoration: none; color: #1c9caa;" target="_blank">
			<i class="el-icon-location" style="color: #1c9caa;"></i>
			<span slot="title">首页</span>
		</a>
	  </el-menu-item>
	  <!-- <el-menu-item index="2">
	    <i class="el-icon-menu"></i>
	    <span slot="title">导航二</span>
	  </el-menu-item>
	  <el-menu-item index="3" disabled>
	    <i class="el-icon-document"></i>
	    <span slot="title">导航三</span>
	  </el-menu-item> -->
	  <el-menu-item index="4">
		<a href="/" style="text-decoration: none; color: #1c9caa;" target="_blank">
			<i class="el-icon-setting" style="color: #1c9caa;"></i>
			<span slot="title">设置</span>
		</a>
	  </el-menu-item>
	</el-menu>
	<!-- </el-col> -->
	<el-col style="margin-left: 30px;width: 92vw;margin-top: 10px;">
		
			
	<el-form ref="form" :model="form" label-width="80px">
		
		<!-- 折叠页面 -->
		<el-collapse v-model="activeNames" @change="handleChange" style="font-size: 50px;border-top: 0px">
			<el-collapse-item title="选择要使用的API" name="0" >
				<el-select v-model="apiName" filterable placeholder="选择一个API"  style="width: 100%;" @change="onChange">
					<el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value"></el-option>
				</el-select>
			</el-collapse-item>				  
		
			<el-collapse-item :title="'请求参数'+ (loading_param? '-加载中': '')" name="1" >
				<el-row style="display: flex;justify-content: space-between;" v-loading="loading_param">
					
				
				<el-col :span="11">
					
				<el-card shadow="never">
				<div slot="header" class="clearfix" style="font-size: 16px;font-weight: bold;color: #6a6a6a;">
					<span>请求填写区域</span>
				</div>
				<el-form-item :label="i.name" v-for="(i, name) in form" :key="name" v-if="name != 'product_id'" >
					<el-input v-model="i.value" :placeholder="'请输入'+i.name" clearable></el-input>
				</el-form-item>
				<el-form-item :label="form.product_id.name" key="product_id" v-if="'product_id' in form" >
					<el-input type="textarea" v-model="form.product_id.value" :placeholder="'请输入'+form.product_id.name" clearable autosize></el-input>						
				</el-form-item>
				<el-form-item>
					<el-button type="primary" @click="onSubmit">开始请求</el-button>
					<el-popover placement="top" width="160" v-model="visibleCancel">
						<p>这是一段内容这是一段内容确定删除吗？</p>
							<div style="text-align: right; margin: 0">
								<el-button size="mini" type="text" @click="visibleCancel = false">取消</el-button>
								<el-button type="primary" size="mini" @click="visibleCancel = false; onCancel()">确定</el-button>
							</div>
						<el-button slot="reference">清除数据</el-button>
					</el-popover>
				</el-form-item>
				</el-card>
				
				</el-col>
				<el-col :span="11">
				
					<el-card shadow="never" style="height: 100%;">
						<div slot="header" class="clearfix"  style="font-size: 16px;font-weight: bold;color: #6a6a6a;">
							<span>请求整合</span>
						</div>
						<div style="width: 100%;white-space:pre-wrap;word-break:break-word">{{allUrl? allUrl:'点击开始请求后，总请求将在这里呈现'}}</div>
					    </el-card>
					
					<!-- <el-form-item :label="'请求整合'" style="height: 100%;"> -->
						<!-- <el-input type="textarea" v-model="allUrl" :placeholder="'点击开始请求后，总请求将在这里呈现'" style="height: 100%;"></el-input>						 -->
					<!-- </el-form-item> -->
				</el-col>
				</el-row>
			</el-collapse-item>
		
			<el-collapse-item :title="'数据结果' + (result_loading? '-结果加载中': '')" name="2" >
				<div v-loading="result_loading">
				<el-button @click="jsonShow = true;">请求结果</el-button>
				<el-button @click="jsonShow = false;">字段意义</el-button>
				<json-viewer v-show="jsonShow" :value="baseInfo.jsonExample" :expand-depth=3 copyable sort theme="my-awesome-json-theme"></json-viewer>
				<div v-show="!jsonShow">
					<el-table :data="baseInfo.filedMean" style="margin-bottom: 20px;" row-key="id" border default-expand-all :tree-props="{children: 'children', hasChildren: 'hasChildren'}">
						<el-table-column prop="key" label="字段" sortable></el-table-column>
						<el-table-column prop="name" label="名称" sortable></el-table-column>
						<el-table-column prop="type" label="类型" sortable></el-table-column>
						<el-table-column prop="comment" label="注释" sortable></el-table-column>
					</el-table>
				</div>
				</div>
			</el-collapse-item>
		  
		  
		  
		</el-collapse>
		
		
	</el-form>
		
		
	
	</el-col>
	</el-row>
</div>
	
</template>

<script>
	import axios from 'axios'
	import QS from 'qs'
	
const urlCodeStr = function(string){return encodeURIComponent(string).replace(/%20/gi, '').replace(/(!)|(')|(\()|(\))|(\~)/gi, item => {
    return '%' + item.charCodeAt(0).toString(16).toLocaleUpperCase();
  })};
function getM_info (url) {
			return new Promise((resolve, reject) => {
				
			// axios.post(url, QS.stringify(params))
			const httpHandler = axios.create({
				headers: { "Content-Type": "application/json;charset=utf-8" }, //即将被发送的自定义请求头
				withCredentials: false //表示跨域请求时是否需要使用凭证
			});
			// let uri = "api/detail_nav?sort="+this.pageSort;
			httpHandler.get(url)
			.then(result =>{resolve(result.data)})
			.catch(error=>{reject(error.message)});
			})
		};

function postM_info (url, params, csrf) {
	return new Promise((resolve, reject) => {
		
	// axios.post(url, QS.stringify(params))
	const httpHandler = axios.create({
		headers: { 
			"Content-Type": "application/json;charset=utf-8" ,
			"X-CSRFToken": csrf,
			}, //即将被发送的自定义请求头
		withCredentials: true ,//表示跨域请求时是否需要使用凭证
	});
	// let uri = "api/detail_nav?sort="+this.pageSort;
	httpHandler.post(url, params)
	.then(result =>{resolve(result.data)})
	.catch(error=>{reject(error.message)});
	})
}
	
	
export default {
  name: 'userUse',
  

  beforeCreate () {
        document.querySelector('body').setAttribute('style', 'margin: 0px;')
  },
  
  beforeDestroy () {
        document.querySelector('body').removeAttribute('style')
  },
  
mounted : function(){
  	console.log('mounted');
	// alert(this.$route.query["sort"]);
	// alert(this.$route.query["api"]);
	console.log(this)
	let self = this;
	getM_info("api/table_api?sort="+this.pageSort + "&api=" + this.pageAPI).then(function(fulfilled){
		self.options = fulfilled
		console.log(fulfilled)
		self.loading_param = false;
	}).catch(function(rejected){self.options = [];});
	
	
	this.baseInfo = {}
	// setTimeout(() => {
	//           this.loading_param = false;
	// 	// 	  this.form = {
	// 	// 	prom_id : {"name": "优惠名称", "value":""},
	// 	//     product_id : {"name": "商品id", "value":""},
	// 	// };
	//         }, 3000);
	
	
	getM_info("api/getMsg").then(function(fulfilled){
		self.csrfToken = fulfilled;
	}).catch(function(rejected){self.csrfToken = null;});
  
  
  },
  
  data () {
    return {
		username: "游客",
		"pageSort": this.$route.query["sort"],
		"pageAPI": this.$route.query["api"],
		hide:1000,
		visibleCancel: false,
		isCollapse: true,
		activeNames: ["0", "1", "2"],
		"jsonShow": true,
		options: [],
		apiName: "",
		allUrl: '',
		form: {},
		result:'',
		loading_param: true,
		result_loading: false,
		"baseInfo": {
				"jsonExample": {
					total: 25,
					limit: 10,
					skip: 0,
					links: {
					  previous: undefined,
					  next: function () {},
					},
					data: [
					  {
						id: '5968fcad629fa84ab65a5247',
						firstname: 'Ada',
						lastname: 'Lovelace',
						awards: null,
						known: [
						  'mathematics',
						  'computing'
						],
						position: {
						  lat: 44.563836,
						  lng: 6.495139
						},
						description: `哈哈哈哈哈Augusta Ada King, Countess of Lovelace (née Byron; 10 December 1815 – 27 November 1852) was an English mathematician and writer,
						chiefly known for her work on Charles Babbage's proposed mechanical general-purpose computer,
						the Analytical Engine. She was the first to recognise that the machine had applications beyond pure calculation,
						and published the first algorithm intended to be carried out by such a machine.
						As a result, she is sometimes regarded as the first to recognise the full potential of a "computing machine" and the first computer programmer.`,
						bornAt: '1815-12-10T00:00:00.000Z',
						diedAt: '1852-11-27T00:00:00.000Z'
					  }, {
						id: '5968fcad629fa84ab65a5246',
						firstname: 'Grace',
						lastname: 'Hopper',
						awards: [
						  'Defense Distinguished Service Medal',
						  'Legion of Merit',
						  'Meritorious Service Medal',
						  'American Campaign Medal',
						  'World War II Victory Medal',
						  'National Defense Service Medal',
						  'Armed Forces Reserve Medal',
						  'Naval Reserve Medal',
						  'Presidential Medal of Freedom'
						],
						known: null,
						position: {
						  lat: 43.614624,
						  lng: 3.879995
						},
						description: `Grace Brewster Murray Hopper (née Murray; December 9, 1906 – January 1, 1992)
						was an American computer scientist and United States Navy rear admiral.
						One of the first programmers of the Harvard Mark I computer,
						she was a pioneer of computer programming who invented one of the first compiler related tools.
						She popularized the idea of machine-independent programming languages, which led to the development of COBOL,
						an early high-level programming language still in use today.`,
						bornAt: '1815-12-10T00:00:00.000Z',
						diedAt: '1852-11-27T00:00:00.000Z'
					  }
					]
				  },
				"filedMean": [
					{"id": 1, "key": "product_id", "name": "商品id", "type": "int", "comment":"商品在京东平台的唯一编码"},
					{"id": 2, "key": "price", "name": "价格", "type": "int", "comment":""},
					{"id": 3, "key": "prom", "name": "优惠信息", "type": "list", "comment":"包含券和优惠活动", "children": [
					{"id": 31, "key": "activate", "name": "优惠活动", "type": "list", "comment":"", "children":[{"id": 311, "key": "start_time", "name": "开始时间", "type": "datatime", "comment":""}, {"id": 312, "key": "end_time", "name": "结束时间", "type": "datatime", "comment":""}]},
					{"id": 32, "key": "coupon", "name": "优惠券", "type": "list", "comment":"", "children":[{"id": 321, "key": "start_time", "name": "开始时间", "type": "boolean", "comment":""}, {"id": 322, "key": "end_time", "name": "结束时间", "type": "string", "comment":""}]},
				]},
			],
				  
		}, /// baseinfo这里结束
      };
    },
    methods: {
	handleChange(val) {
              console.log(val);
        },
	handleOpen(key, keyPath) {
		        // console.log(key, keyPath);
		      },
	handleClose(key, keyPath) {
		        // console.log(key, keyPath);
		      },
	onSubmit() {
			console.log(this.apiName);
			if (!this.apiName) {
				this.$message.error('请选择API再发送请求');
				return;
			}
			// 检查api选择
			
			let param = {}
			
			console.log(this.apiName);
			for (let i in this.form) {
				if(this.form[i]["value"]) {
					param[i] = this.form[i]["value"]
				} else {
					//检查字段是否填写成功
					this.$message.error(this.form[i]["name"]+ '未填写！');
				}
				
			};
			
			// 检查参数的正确性
			if (Object.keys(param).length < Object.keys(this.form).length) {
				// this.$message.error('必要参数参数为空，无法发送请求，请检查！');
				// ..........
				return;
			}
			this.allUrl = this.apiName + "?";
			let all_info = {}
			
			let item = JSON.parse(this.apiName)
			console.log(item)
			all_info["API"] = item.val
			all_info["data"] = param
			all_info["sort"] = this.pageSort
			all_info["name"] = item.name
			console.log(all_info)
			
			this.allUrl = JSON.stringify(all_info)
			
			
			this.result_loading = true;
			
			this.baseInfo = {}
			
			let self = this;
			postM_info("api/api_data", all_info, this.csrfToken).then(function(fulfilled){
				self.baseInfo = fulfilled
				console.log(fulfilled)
				self.result_loading = false;
			}).catch(function(rejected){self.baseInfo = {};});
			
			
			// let keys = Object.keys(param)
			// for(var index = 1;index <= keys.length;index++){
			// 	let i = keys[index-1]
			// 	this.allUrl += (i + "=" + urlCodeStr(param[i]))
			// 	if (keys.length == index) {break}
			// 	this.allUrl += '&'
			// }
			
			
			
			
			
			
			
			
			// this.result_loading = true;
			// let backup = this.baseInfo;
			// this.baseInfo = {};
			
			// setTimeout(() => {
			//           this.result_loading = false;
			// 			// this.baseInfo = backup;
			//         }, 1000);
	      },
	
	
	onChange() {
		// console.log(this.apiName);
		
		let item = JSON.parse(this.apiName)
		console.log(item)
		
		this.allUrl = '';
		this.loading_param = true;
		this.form = {};
		// console.log(item)
		let self = this;
		getM_info("api/api_params?sort="+this.pageSort + "&api=" + item.name).then(function(fulfilled){
			self.form = fulfilled
			self.loading_param = false;
		}).catch(function(rejected){self.form = {};});
		
		
		
	},
	onCancel() {
		this.allUrl = '';
		for (var i in this.form) {
			this.form[i]["value"] = ""
		};
	},  
  }
};





</script>

<style scoped>
	
	.usertitle {
	font-size: 30px;
	margin: 0;
	display:flex;
	align-items:center;
	color: #1c9caa;
	font-weight: 500;
	}
	
	.el-menu-vertical-demo:not(.el-menu--collapse) {
	    width: 200px;
	    min-height: 800px;
	  }
	
	.hoverButton:hover {
		color: #1c9caa;
	}
	
	.el-button--text {
		color: #000000;
	}
	
	.router-link-active {
		text-decoration: none;
		color: #666666;
	}
	
	.router-link-active:hover {
		text-decoration: none;
		color: #1c9caa;
	}
	
	
	.el-select-dropdown__item.selected {
		color: #1c9caa;
	}
	
	
	
	
	
	
	
	
	
	.el-row {
	    margin-top: 20px;
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
	    background: #e5e9f2;
	  }
	  .grid-content {
	    border-radius: 4px;
	    min-height: 36px;
	  }
	  .row-bg {
	    padding: 10px 0;
	    /* background-color: #AAAAAA; */
	  }
	  
	  .el-dropdown-link {
	      cursor: pointer;
	      color: #409EFF;
	    }
	    .el-icon-arrow-down {
	      font-size: 12px;
	    }
	    .demonstration {
	      display: block;
	      color: #8492a6;
	      font-size: 14px;
	      margin-bottom: 20px;
	    }
	  
	
</style>



<style lang="scss" scoped="scoped">
	
	@import "../font/font.css";
	
	
	/deep/ .el-collapse-item__header {
		font-size: 20px;
	}
	
	
	/deep/ .el-scrollbar__wrap {
	  height: 80vh;
	  overflow-x: hidden;
	  
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
	
	
	/deep/ .el-collapse-item__header{
		background: #E7F5F6;
		color: #1c9caa;
		font-family: "思源黑体";
		font-weight: bold;
		border-top-left-radius: 10px;
		border-top: 0px !important;
		padding-left: 16px
	}
	
	// /deep/ .el-collapse-item__header::before{
	// 	content: '---';
	// 	  color: #E7F5F6;
	// }
	
	/deep/ .el-collapse-item__wrap {
		border: 1px solid #EBEEF5;
		// background-color: #E7F5F6;
		// box-shadow:2px 2px 10px #909090;
	}
	
	/deep/ .el-collapse-item.is-active{
		box-shadow:-3px 5px 9px #e1e1e1;
	}
	/deep/ .el-collapse-item__header.is-active{
		background-color: #1c9caa;
		color: #FFFFFF;
	}
	
	
	/deep/ .el-select .el-input.is-focus .el-input__inner{
		border-color: #1c9caa;
	}
	
	/deep/ .el-select .el-input__inner:focus{
		border-color: #1c9caa;
	}
	
	
	/deep/ .el-loading-spinner .path {
		stroke: #1c9caa;
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



