(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d0d7278"],{7636:function(e,t,n){"use strict";n.r(t);var a=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("d2-container",[n("demo-page-header",{ref:"header",attrs:{slot:"header"},on:{submit:e.handleSubmit},slot:"header"}),n("demo-page-main",{attrs:{"table-data":e.table,loading:e.loading}}),n("demo-page-footer",{attrs:{slot:"footer",current:e.page.pageCurrent,size:e.page.pageSize,total:e.page.pageTotal},on:{change:e.handlePaginationChange},slot:"footer"})],1)},o=[],r=(n("99af"),n("d3b7"),n("5530")),i=(n("96cf"),n("1da1")),l={name:"demo-business-table-1",components:{DemoPageHeader:function(){return n.e("chunk-2d0abab8").then(n.bind(null,"15ec"))},DemoPageMain:function(){return n.e("chunk-f64163d6").then(n.bind(null,"b124"))},DemoPageFooter:function(){return n.e("chunk-2d0f0690").then(n.bind(null,"9bf7"))}},data:function(){return{table:[],loading:!1,page:{pageCurrent:1,pageSize:10,pageTotal:0}}},methods:{handlePaginationChange:function(e){var t=this;return Object(i["a"])(regeneratorRuntime.mark((function n(){return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return t.$notify({title:"分页变化",message:"当前第".concat(e.current,"页 共").concat(e.total,"条 每页").concat(e.size,"条")}),t.page={pageCurrent:e.current,pageSize:e.size,pageTotal:e.total},n.next=4,t.$nextTick();case 4:t.$refs.header.handleFormSubmit();case 5:case"end":return n.stop()}}),n)})))()},handleSubmit:function(e){var t=this;this.loading=!0,this.$notify({title:"开始请求模拟表格数据"}),this.$api.DEMO_BUSINESS_TABLE_1_LIST(Object(r["a"])(Object(r["a"])({},e),this.page)).then((function(e){t.loading=!1,t.$notify({title:"模拟表格数据请求完毕"}),t.table=e.list,t.page.pageTotal=e.page.total})).catch((function(e){t.loading=!1,t.$notify({title:"模拟表格数据请求异常"}),console.log("err",e)}))}}},c=l,u=n("2877"),s=Object(u["a"])(c,a,o,!1,null,null,null);t["default"]=s.exports}}]);