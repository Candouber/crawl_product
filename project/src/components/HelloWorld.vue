<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
	<el-button type="info"><router-link to="/detail?sort=京东&api=1" target="_blank">hahhahahah</router-link></el-button>
	<el-button type="info" v-on:click=req>hahhahahah</el-button>
	<el-button type="info" v-on:click=req1>hahhahahah</el-button>
	<!-- <el-button type="info"><router-link to="/use" target="_blank">hahhahahah</router-link></el-button> -->
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
	methods: {
		req () {
			let self = this
			  self.axios.get('/api/jd')
			  .then(res => {
			    console.log(res.data)
			  })
			
		
		},
		req1 () {
			// this.axios.baseURL = '/api'
			// this.axios.get("/api")
			// .then(res=>{
			// 	console.log(res)
			// })
			// .catch(err=>{
			// 	console.log(err)
			// })
			
			
			const httpHandler = this.axios.create({
				headers: { "Content-Type": "application/json;charset=utf-8" }, //即将被发送的自定义请求头
				withCredentials: false //表示跨域请求时是否需要使用凭证
			});
			let uri = "api/jd";
			httpHandler.get(uri).then(result =>{ 
				console.log(result); this.data = result; }).catch(
				error=>{console.error(error);});
			
			
			
			
		
		},
		
		
		
		
	},
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.hello {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
