(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-60cbebfe"],{c2e8:function(t,s,a){"use strict";var e=a("d18c"),l=a.n(e);l.a},cb43:function(t,s,a){"use strict";a.r(s);var e=function(){var t=this,s=t.$createElement,a=t._self._c||s;return a("d2-container",{staticClass:"page",attrs:{type:"card"}},[a("template",{slot:"header"},[t._v("数字动画组件")]),a("el-row",{attrs:{gutter:20}},[a("el-col",{attrs:{span:6}},[a("el-card",{staticClass:"d2-card d2-mb",attrs:{shadow:"never"}},[a("p",{attrs:{slot:"title"},slot:"title"},[t._v("只设置目标数字")]),a("div",{staticClass:"group"},[a("d2-count-up",{attrs:{end:100}})],1)])],1),a("el-col",{attrs:{span:6}},[a("el-card",{staticClass:"d2-card d2-mb",attrs:{shadow:"never"}},[a("p",{attrs:{slot:"title"},slot:"title"},[t._v("设置起止数值")]),a("div",{staticClass:"group"},[a("d2-count-up",{attrs:{start:14,end:100}})],1)])],1),a("el-col",{attrs:{span:6}},[a("el-card",{staticClass:"d2-card d2-mb",attrs:{shadow:"never"}},[a("p",{attrs:{slot:"title"},slot:"title"},[t._v("小数位数")]),a("div",{staticClass:"group"},[a("d2-count-up",{attrs:{end:100,decimals:2}})],1)])],1),a("el-col",{attrs:{span:6}},[a("el-card",{staticClass:"d2-card d2-mb",attrs:{shadow:"never"}},[a("p",{attrs:{slot:"title"},slot:"title"},[t._v("动画时长")]),a("div",{staticClass:"group"},[a("d2-count-up",{attrs:{end:100,duration:6}})],1)])],1),a("el-col",{attrs:{span:6}},[a("el-card",{staticClass:"d2-card",attrs:{shadow:"never"}},[a("p",{attrs:{slot:"title"},slot:"title"},[t._v("回调函数")]),a("div",{staticClass:"group"},[a("d2-count-up",{class:t.className,attrs:{end:100,callback:function(){t.className="end"}}})],1)])],1),a("el-col",{attrs:{span:6}},[a("el-card",{staticClass:"d2-card d2-mb-0",attrs:{shadow:"never"}},[a("p",{attrs:{slot:"title"},slot:"title"},[t._v("结束一秒后更新数值")]),a("div",{staticClass:"group"},[a("d2-count-up",{attrs:{end:t.end,callback:t.update}})],1)])],1)],1)],2)},l=[],c={data:function(){return{className:"",end:50}},methods:{update:function(){var t=this;setTimeout((function(){t.end=100}),1e3)}}},r=c,d=(a("c2e8"),a("2877")),n=Object(d["a"])(r,e,l,!1,null,"5a385a7a",null);s["default"]=n.exports},d18c:function(t,s,a){}}]);