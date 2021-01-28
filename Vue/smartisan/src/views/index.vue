<template>
    <div>
        <myHeader></myHeader>
        <router-view></router-view>
    </div>
</template>
<script>
import myHeader from '../components/myHeader'
export default {
    components:{
        myHeader
    }
    
}
</script>
<style scoped>

</style>