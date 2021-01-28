<template>
    <div>
        <h1>
            订单组件
        </h1>
    </div>
</template>
<script>
export default {
    beforeRouteEnter:(to,from,next)=>{
        var islogin=1
        if(islogin==1){
            next()
        }else{            
             next({ name: 'login' })

        }
    },

    beforeRouteLeave:(to,from,next)=>{
        if(confirm('是否离开？')==true){
            next()
        }else{
            next(false)
        }
    }


    
}
</script>
<style scoped>

</style>