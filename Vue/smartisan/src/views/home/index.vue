<template>
  <div>
    <div class="banner">
      <el-carousel height="415px">
        <el-carousel-item v-for="(item,i) in lunbo" :key="i">
          <img :src="item.picUrl" alt />
        </el-carousel-item>
      </el-carousel>
    </div>

    <div v-for="(item,i) in allList" :key="i">
      <div class="ad" v-if="item.type==1">
        <ul>
          <li v-for="(ad,i) in item.panelContents" :key="i">
            <img :src="ad.picUrl" alt />
          </li>
        </ul>
      </div>

      <div class="hotdetail" v-if="item.type==2">
        <div class="hotdetail_menu">{{item.name}}</div>
        <div class="hotdetail_main">
          <ul>
            <li v-for="(hotDetail,i) in item.panelContents" :key="i">
              <img :src="hotDetail.picUrl" alt />
              {{hotDetail.productName}}
              <p>{{hotDetail.salePrice}}</p>
            </li>
          </ul>
        </div>
      </div>

      <div class="product" v-if="item.type==3">
        <div class="product_menu">{{item.name}}</div>
        <div class="jingxuan">
          <ul>
            <li style="width:580px;" class="ck" v-for="(bigImg,i) in item.panelContents" :key='i' v-if="bigImg.type==3||bigImg.type==2">
              <img :src="bigImg.productImageBig"/>
            </li>

            <li v-for="(mallImg,i) in item.panelContents" :key="i" v-if="mallImg.type==0">
              <img
                :src="mallImg.productImageBig"
                style="width:150px;"
              />
              <p>{{mallImg.productName}}</p>
              <span>{{mallImg.salePrice}}</span>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      allList: [],
      lunbo: [],
    };
  },
  created() {
    this.getData();
  },
  methods: {
    getData() {
      this.$axios
        .get("http://api.mm2018.com:8090/api/goods/home")
        .then((res) => {
          this.allList = res.data.result;
          this.lunbo = this.allList[0].panelContents;
        });
    },
  },
};
</script>
<style scoped>
.banner {
  width: 1180px;
  height: 415px;
  margin: 0 auto;
  margin-top: 20px;
  border-radius: 10px;
  overflow: hidden;
}
ul {
  margin: 0px;
  padding: 0px;
  list-style-type: none;
}
.ad {
  width: 1180px;
  height: 180px;
  margin: 20px auto;
  background: #000;
  border-radius: 10px;
  border: 1px solid #ccc;
  overflow: hidden;
}

.ad ul {
  width: 100%;
  display: flex;
}

.ad ul li {
  flex: 1;
}

.ad ul li img {
  width: 100%;
}

.hotdetail {
  width: 1180px;
  height: auto;
  margin: 0 auto;
  border: 1px solid #ccc;
  overflow: hidden;
  border-radius: 10px;
  background: #fff;
}

.hotdetail_menu {
  height: 51px;
  border-bottom: 1px solid #ccc;
  line-height: 51px;
  text-indent: 30px;
}

.hotdetail_main {
  width: 100%;
}

.hotdetail_main ul {
  display: flex;
}

.hotdetail_main ul li {
  flex: 1;
  text-align: center;
}

.hotdetail_main ul li p {
  color: red;
}

.hotdetail_main ul li img {
  display: block;
  width: 170px;
  margin: 30px auto;
}

.ck img {
  display: block;
  width: 580px;
  margin: 0 !important;
  padding: 0px !important;
}
.product {
  width: 1180px;
  height: auto;
  margin: 0 auto;
  margin-top: 25px;
  border-radius: 15px;
  overflow: hidden;
  border: 1px solid #dbdbdb;
}

.jingxuan {
  width: 1180px;
  height: 716px;
  background: #fff;
}

.jingxuan ul {
  display: flex;
  flex-flow: wrap;
  justify-content: space-between;
}

.jingxuan ul li {
  width: 284px;
  box-sizing: border-box;
  background: #fff;
  height: 350px;
  margin-bottom: 16px;
  overflow: hidden;
  text-align: center;
}

.jingxuan ul li img {
  display: block;
  margin: 0 auto;
  margin-top: 50px;
}

.jingxuan ul li:hover img {
  opacity: 0.8;
}

.jingxuan ul li p {
  padding-bottom: 15px;
  padding-top: 20px;
}

.jingxuan ul li span {
  color: red;
}

.product_menu {
  width: 1180px;
  height: 50px;
  background: #fafafa;
  line-height: 50px;
  text-indent: 30px;
  border-bottom: 1px solid #e1e1e1;
}

.product_main {
  width: 1180px;
}

.product_main ul {
  display: flex;
  justify-content: space-between;
}

.product_main ul li {
  width: 586px;
  height: 350px;
  background: #fff;
  text-align: center;
}

.product_main ul li img {
  display: block;
  margin: 0 auto;
  width: 170px;
  height: 170px;
  margin-top: 35px;
}

.product_main ul li p {
  padding-top: 30px;
  padding-bottom: 30px;
}

.product_main ul li span {
  color: red;
}
</style>