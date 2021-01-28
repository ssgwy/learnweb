import Vue from 'vue'
import Router from 'vue-router'
import index from '@/views/index'
import Home from '@/views/home'
import allgoods from '@/views/allgoods'
import detail from '@/views/detail'


Vue.use(Router)

export default new Router({
    routes: [{
            path: '/',
            name: 'index',
            component: index,
            children: [{
                    path: '/',
                    name: 'Home',
                    component: Home
                },
                {
                    path: '/allgoods',
                    name: 'allgoods',
                    component: allgoods

                }
            ]
        }, {
            path: '/detail',
            name: 'detail',
            component: detail
        }



    ]
})