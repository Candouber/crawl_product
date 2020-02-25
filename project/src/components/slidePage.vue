<template>
	<el-pagination
		@current-change="pageChange"
		
		background
		layout="prev, pager, next"
		:total="currentTotal"
		:page-size="pageSize"
		class="page"
		:current-page="currentPage"
	>
	</el-pagination>
</template>

<script>
	export default{
		name:'page',
		methods:{
			pageChange(val){
				this.currentPage = val
				window.console.log(this.currentPage)
				this.$router.push({name:'List', query:{aa:this.$route.query.aa, bb:this.$route.query.bb, cc: this.$route.query.cc, dd: this.$route.query.dd, page:this.currentPage}})
			}
		},
		props:{
			currenPage:{
				type: Number,
				default:1
			}
		},
		data() {
			return {
				currentPage: this.$route.query.page,
				pageSize: 8,
				currentTotal: 1,
				tableData: [],
				aa: this.$route.query.aa,
				bb: this.$route.query.bb,
				cc: this.$route.query.cc,
				dd: this.$route.query.dd,
			}
		}
	}
</script>

<style>
	.page{
		margin: auto;
	}
	.el-pagination.is-background .el-pager li:not(.disabled).active{
		background-color: #1C9CAA;
	}
</style>
