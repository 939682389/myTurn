(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-e97412ae"],{"83c0":function(t,e,n){"use strict";n.r(e);var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("d2-container",[n("el-alert",{attrs:{title:"由于演示功能特殊，请注意在需要时刷新您的浏览器（以重置路由设置）查看效果",type:"warning","show-icon":""}}),n("d2-highlight",{attrs:{code:t.dataView}}),n("el-form",{attrs:{"label-position":"top"}},[n("el-form-item",{attrs:{label:"创建路由（你可以假设上面是接口数据）"}},[n("el-button-group",t._l(t.setting,(function(e){return n("el-button",{key:e.component,on:{click:function(n){return t.onClick(e)}}},[t._v(" "+t._s(e.title)+" ")])})),1)],1)],1)],1)},o=[],i=(n("99af"),n("c740"),n("b0c0"),n("d3b7"),n("2909")),r=n("5530"),u=n("60bb"),c=n("5880"),d=n("d046"),l=n("0778"),s={data:function(){return{title:"",setting:[{title:"追加页面 1",name:"add-routes-1",path:"add-routes/1",component:"1"},{title:"追加页面 2",name:"add-routes-2",path:"add-routes/2",component:"2"},{title:"追加页面 3",name:"add-routes-3",path:"add-routes/3",component:"3"}]}},computed:Object(r["a"])(Object(r["a"])({},Object(c["mapState"])("d2admin/menu",["header"])),{},{dataView:function(){return JSON.stringify(this.setting,null,2)}}),methods:Object(r["a"])(Object(r["a"])({},Object(c["mapMutations"])({pageInit:"d2admin/page/init",headerSet:"d2admin/menu/headerSet"})),{},{onClick:function(t){var e=t.title,a=t.name,o=t.path,r=t.component,c=[{path:"/demo/playground",component:l["a"],children:[{path:o,name:a,component:function(){return n("a92b")("./"+r+".vue")},meta:{title:e}}]}];this.$router.addRoutes(c),this.pageInit([].concat(Object(i["a"])(d["b"]),c));var s={title:"临时菜单",icon:"plus-square",children:[]},h={path:"/demo/playground/".concat(o),title:e,icon:"file-o"},p=Object(u["cloneDeep"])(this.header),m=p.findIndex((function(t){return t.title===s.title}));m>=0?p[m].children.push(h):(s.children.push(h),p.push(s)),this.headerSet(p),this.$router.push({name:a})}})},h=s,p=n("2877"),m=Object(p["a"])(h,a,o,!1,null,null,null);e["default"]=m.exports},a92b:function(t,e,n){var a={"./1.vue":["7f87","chunk-2d0e2744"],"./2.vue":["81f9","chunk-2d0dda42"],"./3.vue":["8c5f","chunk-2d0e9032"]};function o(t){if(!n.o(a,t))return Promise.resolve().then((function(){var e=new Error("Cannot find module '"+t+"'");throw e.code="MODULE_NOT_FOUND",e}));var e=a[t],o=e[0];return n.e(e[1]).then((function(){return n(o)}))}o.keys=function(){return Object.keys(a)},o.id="a92b",t.exports=o}}]);