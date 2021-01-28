<template>
<div>
    <div class="top">
      <img src="../assets/images/logo.png" alt="">
    </div>
    <div class="menu">
      <ul>
        <li><router-link to="/">首页</router-link></li>
        <li><router-link to='/allgoods'>全部商品</router-link></li>
      </ul>
    </div>
</div>
    
</template>
<script>
export default {
    
}
</script>
<style scoped>

ul{margin: 0px;padding: 0px;list-style-type:none ;}

.top{width: 100%;height: 58px;background: #000;display: flex;align-items: center;}

.top img{margin-left: 20px;}

.menu{width: 100%;height: 74px;background: #fff;}

.menu ul{width: 1180px;display: flex;margin: 0 auto;}

.menu ul li{flex: 1;text-align: center;line-height: 74px;}

.menu ul li a{color: #333;text-decoration: none;}


</style>