// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import JsonViewer from 'vue-json-viewer'




// import fontawesome from '@fortawesome/fontawesome'
// import FontAwesomeIcon from '@fortawesome/vue-fontawesome'
// import solid from '@fortawesome/fontawesome-free-solid'
// import regular from '@fortawesome/fontawesome-free-regular'
// import brands from '@fortawesome/fontawesome-free-brands'
// fontawesome.library.add(solid)
// fontawesome.library.add(regular)
// fontawesome.library.add(brands)
// Vue.component('font-awesome-icon', FontAwesomeIcon)



import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)
// axios.defaults.baseURL = '/api'
// axios.defaults.headers.post['Content-Type'] = 'application/json';
// Vue.config.productionTip = false





Vue.use(ElementUI)
Vue.use(JsonViewer)
Vue.config.productionTip = false



/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
