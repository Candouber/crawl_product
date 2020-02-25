<template>
	<div>
		<el-row >
			<a href="#">
			<el-col :span="8" v-for="o in len" :key="o"  class="elcol">
				<router-link style="text-decoration: none; color: white;" :to="cardMsg.url[o-1]" target="_blank">
					<el-card  class="elbody">
						<img src="../assets/list_api.png" class="image">
						<div class="bottom_text">
						<span>{{cardMsg.name[o-1]}}</span> 
							<div class="time">{{ c }}</div>
					</div>
						<el-button type="primary" icon="el-icon-search" class="button" >查看详情</el-button>
				
					</el-card>
					</router-link>
			</el-col>
			</a>
		</el-row>
		<div class="slide" v-show="len">
				<m-page></m-page>
		</div>
	</div>
</template>


<style>
  .time {
    font-size: 13px;
    color: #999;
	text-align: center;
	
  }
  
  .bottom {
	width: 100px;
    margin-top: 13px;
    line-height: 12px;
  }


  .image {
    width: 105px;
	height: 105px;
    margin-left: 30px;
  }

 /* .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  } */
  
  /* .clearfix:after {
      clear: both
  } */
  .elcol{
	width: 200px;
	display: block;
	margin-top: 20px;
	margin-right: 40px;
	float: left;
	height: 245px;

  }
  .elbody{
	margin-bottom: 20px;
	width: 200px;
	height: 200px;
	position: relative;
	margin-left: 13px;
  }
  .bottom_text{
	margin: auto;
	text-align: center;
	margin-top: 10px;
  }
  .elbody:hover{
	width: 200px;
	height: 245px;
	position: relative;
  }
  .button {
	margin: auto;
	margin-left: 20px;
	margin-top: 20px;
	visibility: hidden;
	background-color: #1C9CAA;
	border-color: #1C9CAA;
  }
  
  
  .el-button--primary:focus, .el-button--primary:hover {
	background-color: #1C9CAA !important;
	border-color: #FFFFFF;
  }
  .elbody:hover .button{
	visibility: visible;
  }
  .slide{
	margin-bottom: 30px;
	display: flex;
	/* margin-left: 30%; */
  
  }
</style>

<script>
	import axios from 'axios'
	import page from '../components/slidePage.vue'
export default {
  name:'ele_card',
  data() {
    return {
		desp: '这是我的身价！',
		num: 10,
		currentPage: this.$route.query.page,
		l: ''
    };
  },
  props:{
	cardMsg: Object,
	len: Number
  },
  components:{
	'm-page': page
  },
  mounted() {
	let self = this;
	axios.get("api/getMsg").then(function(res){
		self.csrfToken = res.data
		
		
		axios.post('api/getMsg',
		{
			'type1': 0,
			'type2': 0,
			'type3': 0,
			'type4': 0
		},
		{
			headers: {
				"Content-Type":"application/json;charset=utf-8",
				"X-CSRFToken": self.csrfToken,
			},
		},
		).then(function(res){
			self.cardMsg = res.data
			self.len = res.data.name.length
		});
	
	
	})
	
	
	
	}
  
}
</script>