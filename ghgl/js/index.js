const app = new Vue({
    el:'#app',
    data:{
        students: [],  //所有的学生信息

        //====分页相关的变量====
        total:100,   //数据总行数 
        currentpage:1,   //当前页
        pagesize:10,  //每页显示行数
    },
    mounted() {
        //自动加载数据
        this.getStudents();
    },
    methods: {
        //获取所有学生信息
        getStudents:function(){
            //记录this的地址
            let that = this
            //使用Axios实现Ajax请求
            axios
            .get(that.baseURL + "students/")
            .then(function)(res){
                //请求成功后执行的函数
                if(res.data.code === 1){
                    //把数据给students
                    that.students = res.data.data;
                    //提示：
                    that.$message({
                        message: '数据加载成功！',
                        type: 'success'
                    });
                } else {
                    //失败的提示！
                    that.$message.error(res.data.msg);
                }
            }
           
        }
    }
})