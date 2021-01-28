<template>
    <div>
        <div class="topheader">
            <ul>
                <li :class="{active:isActive==1}" @click="selectBtn(1)">综合排序</li>
                <li :class="{active:isActive==2}" @click="selectBtn(2)">价格由低到高</li>
                <li :class="{active:isActive==3}" @click="selectBtn(3)">价格由高到低</li>
                <li><input type="text" v-model="min"></li>
                <li>-</li>
                <li><input type="text" v-model="max"></li>
                <li><input type="button" value="确认" @click="btn"></li>
            </ul>
        </div>

        <div class="allgoods">
            <ul>

             <li v-for="(item,i) in allList" :key="i" @click="detailBtn(item.productId)">
                 <img :src="item.productImageBig" alt="">{{item.productName}}<p>{{item.salePrice}}</p></li>
           
            </ul>
        </div>
    </div>
</template>
<script>

//全部数据的接口
//http://api.mm2018.com:8090/api/goods/allGoods?page=1&size=8&sort=''&priceGt='100'&priceLte='1000'
export default {
    data(){
        return{     
            allList:[],
            isActive:1,
            sort:'',
            min:'',
            max:''




        }
    },
    created(){  
        this.getDate() 
       
    },
    methods:{ 
        getDate(){
            this.$axios.get(`http://api.mm2018.com:8090/api/goods/allGoods?page=1&size=16&sort=${this.sort}&priceGt=${this.min}&priceLte=${this.max}`)
            .then(res=>{
                this.allList=res.data.data
                console.log(res.data.data)
            })
        },
        selectBtn(i){
            this.isActive=i
            if(i==1){
                this.sort=''
                this.getDate()
            }
            if(i==2){
                this.sort=1
                this.getDate()
            }

            if(i==3){
                this.sort=-1
                this.getDate()
            }
        },
        btn(){
            if(this.max>this.min){
                 this.getDate()
            }
        },
        detailBtn(id){
            //console.log(id)
            this.$router.push({
                path:`/detail?productId=${id}`
            })

        }
       
    }
    
}
</script>
<style scoped>
.active{color: blue;}
.topheader{width: 1180px;margin: 0 auto;}
ul{margin: 0px;padding:0px;list-style-type: none;}

.topheader ul{width: 100%;display: flex;justify-content: space-between;}

.topheader ul li{line-height: 60px;}

.allgoods{width: 1180px;margin: 0 auto;background: #fff;border-radius: 10px;overflow: hidden;;}

.allgoods ul{width: 100%;display: flex;justify-content: space-between;flex-flow: wrap;}
.allgoods ul li{width: 25%;text-align: center;}
.allgoods ul li img{width: 150px;display: block;margin: 0 auto;}
.allgoods ul li p{color: red;}

</style>