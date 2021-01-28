<template>
<div>
    <h1>计算属性</h1>
    <h2>{{getMsg}}</h2>
    <h3>{{getAvg}}</h3>
    <input type="text" v-model="user">
    <input type="text" v-model="pass">
    <input type="button" value="点击" :class="{active:getActive}">
</div>
    
</template>
<script>
export default {
    data(){
        return{
            num1:10,
            num2:20,
            num3:30,
            user:'',
            pass:''
        }
    },
    computed:{
        getMsg(){
            return this.num1+this.num2+this.num3
        },
        getAvg(){
            return this.getMsg/3
        },
        getActive(){
            if(this.user==''||this.pass==''){
                return false
            }
            return true
        }
    }
    
}
</script>

<style scoped>

.active{background: red;}

</style>