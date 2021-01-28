<template>
<div>
    <h1>侦听属性</h1>   
    <input type="text" v-model="num"> 
    <hr>
     <input type="text" v-model="user">
    <input type="text" v-model="pass">
    <input type="button" value="点击" :class={active:isactive}>

</div>
    
</template>
<script>
export default {
   data(){
       return{
           num:10,
           user:'',
           pass:'',
           isactive:false
       }
   },
   watch:{
       num(){
           console.log(111)
       },
       user(){
           if(this.user==''||this.pass==''){
               this.isactive=false
           }
           else{
               this.isactive=true
           }
       },
       pass(){
           if(this.user==''||this.pass==''){
               this.isactive=false
           }
           else{
               this.isactive=true
           }
       }

   }

    
}
</script>
<style scoped>
.active{background: red;}
</style>