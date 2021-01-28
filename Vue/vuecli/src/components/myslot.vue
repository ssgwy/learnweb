<template>
<div>
    <h1>slot插槽的使用</h1>
    <h2>{{sendMsg}}</h2>
    <h3><slot name="msg"></slot></h3>
    <h4><slot name="num"></slot></h4>
</div>
    
</template>
<script>
export default {
    props:['sendMsg']
    
}
</script>
<style scoped>

</style>