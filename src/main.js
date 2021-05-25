import Vue from 'vue'
import App from './App.vue' // Notre application
import './registerServiceWorker'
import router from './router'
import './scss/styles.scss' // votre fichier de style qui importe tous les autres.
const urlServiceWeb = 'http://127.0.0.1:5000/'
window.urlServiceWeb = urlServiceWeb
// inclusion de JQuery. Si vous ne le prenez pas, enlevez ces deux lignes et faites npm uninstall jquery
const $ = require('jquery')
window.$ = $

Vue.config.productionTip = false
new Vue({
  render: h => h(App),
  router
}).$mount('#app')
