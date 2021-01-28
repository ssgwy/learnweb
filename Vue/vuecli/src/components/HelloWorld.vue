<template>
  <div class="hello">  
    <h1>{{num|toFixed(3,'￥')}}</h1>  
    <h1>{{num1|toFixed1(2)}}</h1>  
    <h1>{{ msg }}</h1>
    <h2>Essential Links</h2>
    <ul>
      <li>
        <a
          href="https://vuejs.org"
          target="_blank"
        >
          Core Docs
        </a>
      </li>
      <li>
        <a
          href="https://forum.vuejs.org"
          target="_blank"
        >
          Forum
        </a>
      </li>
      <li>
        <a
          href="https://chat.vuejs.org"
          target="_blank"
        >
          Community Chat
        </a>
      </li>
      <li>
        <a
          href="https://twitter.com/vuejs"
          target="_blank"
        >
          Twitter
        </a>
      </li>
      <br>
      <li>
        <a
          href="http://vuejs-templates.github.io/webpack/"
          target="_blank"
        >
          Docs for This Template
        </a>
      </li>
    </ul>
    <h2>Ecosystem</h2>
    <ul>
      <li>
        <a
          href="http://router.vuejs.org/"
          target="_blank"
        >
          vue-router
        </a>
      </li>
      <li>
        <a
          href="http://vuex.vuejs.org/"
          target="_blank"
        >
          vuex
        </a>
      </li>
      <li>
        <a
          href="http://vue-loader.vuejs.org/"
          target="_blank"
        >
          vue-loader
        </a>
      </li>
      <li>
        <a
          href="https://github.com/vuejs/awesome-vue"
          target="_blank"
        >
          awesome-vue
        </a>
      </li>
    </ul>
    <hr>
    <myslot :sendMsg="msg">
      
      <div slot="msg">
        {{num1}}
      </div>

      <div slot="num">
        {{num}}
      </div>
     
    </myslot>
    <hr>
      <!-- <el-button type="primary">主要按钮</el-button>
      <el-button type="danger">危险按钮</el-button> -->

      <mt-button type="primary" @click="btn">primary</mt-button>
      <mt-button type="danger" @click="mytab">选项卡</mt-button>

      <hr>
      <router-link to="/mytab">选项卡</router-link>
      <hr>
       <router-link to="/mydetail">详情页面</router-link>
       <router-link to="/mycart">购物车页面</router-link>
      <router-link to="/myorder">订单页面</router-link>

      <hr>
      <h1>Vuex</h1>
      <h2>{{$store.state.num}}</h2>

      <input type="text" :value="$store.state.num">
      <input type="button" value="点击" @click="addBtn">

       <hr>
       <h1>getters</h1>
       <h2>
         {{$store.getters.getNum}}
       </h2>

       <hr>
       <h1>辅助函数</h1>
       <h2>
         {{islogin}}
       </h2>
       <h2>
         {{num123}}
       </h2>

       <h2>
         {{getNum}}
       </h2>
        
        

     

     
     
  </div>
</template>

<script>
import {mapState,mapGetters,mapMutations,mapActions} from 'vuex'

import { Toast } from 'mint-ui';
import myslot from './myslot'
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      num:5,
      num1:10,
      list:''
    }
  },
  computed:{
    ...mapState(['islogin','num123']),
    ...mapGetters(['getNum'])

  },
  created(){
    //this.getDate()
    //this.getParams()
    //this.getAll()

  },
  methods:{
    ...mapMutations(['getAdd']),
    ...mapActions(['getAddAction']),
   addBtn(){
     //错误写法
     //this.$store.state.num++

     //正确的使用方法
     //this.$store.commit('getAdd',{id:1,name:'123'})
     //this.$store.dispatch('getAddAction',123)
     //this.getAdd()

     this.getAddAction()

    
   },
    getDate(){
    this.$axios.get('/api/goods/home')
    .then(res=>{
      console.log(res)
    })
    },

    getParams(){
      this.$axios.get('http://getlink.mm2018.com:8081/selectDemo',{
        params:{
          id:100
        }
      }).then(res=>{
        console.log(res)
        this.list=res
      })

      //post请求
      // this.$axios.post('http://getlink.mm2018.com:8081/selectDemo',{
      //   params:{
      //     id:100
      //   }
      // }).then(res=>{
      //   console.log(res)
      // })

    },

    getAll(){
      //解决跨域
      this.$axios.get('/api').then(res=>{
        console.log(res)
      })

    },

    btn(){
      Toast('提示信息11111');
    },
    mytab(){
      //this.$router.push({name:'mytab'})
      this.$router.push({path:'/mytab',query:{id:1}})
    }

  },
  filters:{
    toFixed(val,data,data1){
      return data1+val.toFixed(data)
    }
  },
  components:{
    myslot
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
