import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import './scss/styles.scss'
const urlServiceWeb = 'http://127.0.0.1:5000/'
window.urlServiceWeb = urlServiceWeb
const $ = require('jquery')
window.$ = $

Vue.config.productionTip = false
new Vue({
  render: h => h(App),
  router
}).$mount('#app')
