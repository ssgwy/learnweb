import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import mytab from '@/components/mytab'
import mycomputed from '@/components/computed'
import mywatch from '@/components/watch'
import myslot from '@/components/myslot'

import mylogin from '@/components/login'
import mydetail from '@/components/detail'
import mycart from '@/components/cart'

import myorder from '@/components/order'


Vue.use(Router)

export default new Router({
    routes: [{
            path: '/',
            name: 'HelloWorld',
            component: HelloWorld
        },
        {
            path: '/mytab',
            name: 'mytab',
            component: mytab
        },
        {
            path: '/computed',
            name: 'computed',
            component: mycomputed
        },
        {
            path: '/watch',
            name: 'watch',
            component: mywatch
        },
        {
            path: '/myslot',
            name: 'myslot',
            component: myslot
        },
        {
            path: '/login',
            name: 'login',
            component: mylogin
        },
        {
            path: '/mydetail',
            name: 'mydetail',
            component: mydetail
        },
        {
            path: '/mycart',
            name: 'mycart',
            component: mycart,
            meta: {
                needAuth: true
            }
        },
        {
            path: '/myorder',
            name: 'myorder',
            component: myorder
        },


    ]
})