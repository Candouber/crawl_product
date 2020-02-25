<template>
	<div>
		<el-input class="inp" v-model="input" @focus="input"  placeholder="请输入内容" ></el-input>
		<div class="but">
			<el-button slot="append" @click="sear" icon="el-icon-search"></el-button>
		</div>
		
	</div>
	
</template>

<script>
	import axios from 'axios'
	export default {
      data() {
        return {
			input: '',
			len: '',
			aa: '',
			bb: '',
			cc: '',
			dd: ''
        }
      },
	methods:{
		sear:function(){
			var msg = this.input
			let self = this;
			axios.post('/apis/getMsg/two',
			{
				'name': msg
			},
			).then(function(res){
				self.aa = res.data.type1
				self.bb = res.data.type2,
				self.cc = res.data.type3,
				self.dd = res.data.type4,
				self.$route.push({name:'List', query:{aa:self.aa, bb:self.bb, cc:self.cc, dd:self.dd, page:1}})
				alert(self.len)
			})
		}
	},
	
}
</script>

<style>
	.inp{
		float: left;
		width: 550px;
		border: #1C9CAA;
	}
	.but{
		float: left;
		position: relative;
		left: -5px;
	}
	.inp input{
		border-right: none;
		border-color: #1C9CAA;
	}
	.but button:hover{
		background-color: #1C9CAA;
	}
	.but button{
		border-color: #1C9CAA;
		color: white;
		background-color: #1C9CAA;
	}
	.el-input__inner:focus {
		border-color: #1c9caa;
	}
</style>
