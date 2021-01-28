const app = new Vue({
    el:'#app',
    data:{
        msg:'工会记账管理',
        accounts: [
            {
                id: 1, a_date: '2020-01-01', matters: '会费收入', a_type: '会费收入', a_count: 25000, remark: '2020年上半年会费'
            },
            {
                id: 2, a_date: '2020-02-02', matters: '教职工篮球赛服装', a_type: '工会活动支出', a_count: 5000, remark: ''                
            },
            {
                id: 3, a_date: '2020-03-03', matters: '教职工篮球赛服装', a_type: '工会活动支出', a_count: 5000, remark: ''                
            },
            {
                id: 4, a_date: '2020-04-04', matters: '教职工篮球赛服装', a_type: '工会活动支出', a_count: 5000, remark: ''                
            },
            {
                id: 5, a_date: '2020-05-05', matters: '教职工篮球赛服装', a_type: '工会活动支出', a_count: 5000, remark: ''                
            },
            {
                id: 6, a_date: '2020-06-06', matters: '教职工篮球赛服装', a_type: '工会活动支出', a_count: 5000, remark: ''                
            },
            {
                id: 7, a_date: '2020-07-07', matters: '教职工篮球赛服装', a_type: '工会活动支出', a_count: 5000, remark: ''                
            },
            {
                id: 8, a_date: '2020-08-08', matters: '教职工篮球赛服装', a_type: '工会活动支出', a_count: 5000, remark: ''                
            },
            {
                id: 9, a_date: '2020-09-09', matters: '教职工篮球赛服装', a_type: '工会活动支出', a_count: 5000, remark: ''                
            },
            {
                id: 10, a_date: '2020-10-10', matters: '教职工篮球赛服装', a_type: '工会活动支出', a_count: 5000, remark: ''                
            },
        ],
        total: 100,    //数据总行数
        currentpage: 1,   //当前所在页
        pagesize: 10,    //每页显示10行
    }
})