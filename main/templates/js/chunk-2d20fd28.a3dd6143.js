(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d20fd28"],{b4ee:function(e,t,l){"use strict";l.r(t);var i=function(){var e=this,t=e.$createElement,l=e._self._c||t;return l("div",[l("el-table",{directives:[{name:"loading",rawName:"v-loading",value:e.loading,expression:"loading"}],staticStyle:{width:"70%"},attrs:{data:e.currentTableData,size:"mini",stripe:""},on:{"selection-change":e.handleSelectionChange}},[l("el-table-column",{attrs:{type:"selection",width:"50"}}),l("el-table-column",{attrs:{label:"id",width:"100",align:"center","show-overflow-tooltip":!0},scopedSlots:e._u([{key:"default",fn:function(t){return[e._v(" "+e._s(t.row.id)+" ")]}}])}),l("el-table-column",{attrs:{label:"头像",width:"120",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){return[l("el-image",{staticStyle:{width:"120px",height:"120px"},attrs:{src:e.APP_API+"user/img?url="+t.row.avatar},on:{click:function(l){return e.imagePreview(t.row.avatar)}}})]}}])}),l("el-table-column",{attrs:{label:"昵称",width:"120",align:"center","show-overflow-tooltip":!0},scopedSlots:e._u([{key:"default",fn:function(t){return[e._v(" "+e._s(t.row.nick)+" ")]}}])}),l("el-table-column",{attrs:{label:"位置",width:"200",align:"center","show-overflow-tooltip":!0},scopedSlots:e._u([{key:"default",fn:function(t){return[e._v(" "+e._s(t.row.location)+" ")]}}])}),l("el-table-column",{attrs:{label:"简介",width:"200",align:"center","show-overflow-tooltip":!0},scopedSlots:e._u([{key:"default",fn:function(t){return[e._v(" "+e._s(t.row.introduction)+" ")]}}])}),l("el-table-column",{attrs:{label:"创建时间",width:"200",align:"center","show-overflow-tooltip":!0},scopedSlots:e._u([{key:"default",fn:function(t){return[e._v(" "+e._s(t.row.create_time)+" ")]}}])})],1),l("el-dialog",{attrs:{visible:e.imageVisible},on:{"update:visible":function(t){e.imageVisible=t}}},[l("el-image",{staticStyle:{height:"60vh"},attrs:{fit:"fit",src:e.imageUrl}})],1)],1)},a=[],n=(l("9c5c"),{props:{tableData:{default:function(){return[]}},loading:{default:!1}},data:function(){return{APP_API:"https://gathering.cooltian.cn/v1/",currentTableData:[],imageVisible:!1,imageUrl:""}},watch:{tableData:{handler:function(e){this.currentTableData=e},immediate:!0}},methods:{handleSelectionChange:function(e){this.$emit("select",e)},imagePreview:function(e){this.imageUrl=this.APP_API+"user/img?url="+e,this.imageVisible=!0}}}),o=n,r=l("2877"),s=Object(r["a"])(o,i,a,!1,null,null,null);t["default"]=s.exports}}]);