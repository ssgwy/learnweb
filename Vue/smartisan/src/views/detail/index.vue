<template>
    <div>
        <h1>详情页面</h1>
        <h2>
            {{detail.productName}}
        </h2>
        <img :src="detail.productImageBig" alt="" style="width:200px">
        <div v-html="detail.detail"></div>
    </div>
</template>
<script>
export default {

    data(){
        return{

            detail:{}

        }
    },
    created(){
        this.getData()

    },
    methods:{
        //接口
        //http://api.mm2018.com:8090/api/goods/productDet?productId=150642571432851
        getData(){
            this.$axios.get(`http://api.mm2018.com:8090/api/goods/productDet?productId=${this.$route.query.productId}`)
            .then(res=>{
                console.log(res.data)
                this.detail=res.data
            })
        }

    }
    
}
</script>
<style scoped>

</style>