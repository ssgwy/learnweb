// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'

//Vuex代码分离
import store from './store'




//把axios挂在到Vue原型中
Vue.prototype.$axios = axios
    //axios.defaults.baseURL = "http://api.mm2018.com:8090"

router.beforeEach((to, from, next) => {
    var islogin = 0 //0表示未登录  1表示已经登录
    if (to.meta.needAuth) {
        if (islogin == 0) {
            router.push({ name: 'login' })
        } else {
            next()
        }
    } else {
        next()
    }
})

import 'mint-ui/lib/style.css'
// import { Button } from 'element-ui'
// Vue.use(Button)
import { Button } from 'mint-ui';
Vue.component(Button.name, Button);

Vue.config.productionTip = false
Vue.filter('toFixed1', function(val, data) {
    return val.toFixed(data)

})

/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    store,
    components: { App },
    template: '<App/>'
})