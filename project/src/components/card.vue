<template>
	<div class="mcard">
		<img src="../assets/广告位1.png">
		<img src="../assets/广告位1.png">
		<img src="../assets/广告位1.png">
	</div>
</template>

<script>
	export default{
		name:'card'
	}
</script>

<style>
	.mcard{
		width: 800px;
		height: 200px;
		margin: auto;
		z-index: -1;
	}
	.mcard img{
		width: 240px;
		margin-right: 20px;
		border-radius:20px; 
		transition-duration: 0.5s;
		top: 0px;
	}
	.mcard img:hover{
		position: relative;
		top: -10px;
		transform:skewY(-10px);
	}
	
</style>
