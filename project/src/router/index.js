import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import contains_test from '../components/contains'
import userUse from '../components/userUse'
import Home from '../views/t1'
import List from '../views/t2'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/List',
      name: 'List',
      component: List,
    },
	{
		path: '/detail',
		name: 'contains',
		component: contains_test
	},
	{
		path: '/use',
		name: 'userUse',
		component: userUse
	},
	{
		path: '/hello',
		name: 'HelloWorld',
		component: HelloWorld
	},
  ]
})
userUse