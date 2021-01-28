<template>
<div>
<h1>选项卡---{{this.$route.query.id}}</h1>
<div class="menu">
    <ul>
        <li :class="{active:isactive==0}" @click="selectActive(0)">娱乐新闻</li>
        <li :class="{active:isactive==1}" @click="selectActive(1)">体育新闻</li>
        <li :class="{active:isactive==2}" @click="selectActive(2)">汽车新闻</li>
    </ul>
</div>
<div class="main">
    <ul>
        <li v-for="(item,i) in list[isactive]" :key="i">
            {{item}}
        </li>
       
    </ul>

</div>
</div>
 
</template>

<script>
export default {
    data(){
        return{
            isactive:0,
            list:[
                ['娱乐新闻','娱乐新闻1','娱乐新闻2'],
                ['体育新闻','体育新闻1','体育新闻3'],
                ['汽车新闻','汽车新闻1','汽车新闻2']
            ]
        }
    },
    methods:{
        selectActive(i){
            this.isactive=i
        }
    }
    
}
</script>

<style scoped>
.menu{width: 800px;margin:0 auto}

.menu ul{display: flex;margin:0px;padding: 0px;list-style-type: none;justify-content: space-between;}

.active{color: red;}

</style>


