(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-e92fb26e","chunk-2d0dae4a","chunk-2d0dd10e","chunk-2d0a3877"],{"0320":function(n,t){n.exports="在 `columns` 中设置 `sortable` 属性为 `true` ，即可实现以该列为基准的排序。可以通过 `options` 的 `defaultSort` 属性设置默认的排序列和排序顺序。代码如下：\n"},"6e16":function(n,t,e){"use strict";e.r(t),t["default"]="<template>\n  <div>\n    <d2-crud\n      :columns=\"columns\"\n      :data=\"data\"\n      :options=\"options\"/>\n  </div>\n</template>\n\n<script>\nexport default {\n  data () {\n    return {\n      columns: [\n        {\n          title: '日期',\n          key: 'date',\n          sortable: true\n        },\n        {\n          title: '姓名',\n          key: 'name'\n        },\n        {\n          title: '地址',\n          key: 'address'\n        }\n      ],\n      data: [\n        {\n          date: '2016-05-02',\n          name: '王小虎',\n          address: '上海市普陀区金沙江路 1518 弄'\n        },\n        {\n          date: '2016-05-04',\n          name: '王小虎',\n          address: '上海市普陀区金沙江路 1517 弄'\n        },\n        {\n          date: '2016-05-01',\n          name: '王小虎',\n          address: '上海市普陀区金沙江路 1519 弄'\n        },\n        {\n          date: '2016-05-03',\n          name: '王小虎',\n          address: '上海市普陀区金沙江路 1516 弄'\n        }\n      ],\n      options: {\n        defaultSort: {\n          prop: 'date',\n          order: 'descending'\n        }\n      }\n    }\n  }\n}\n<\/script>"},8099:function(n,t,e){"use strict";e.r(t);var a=e("8bbf"),d=e.n(a),s=e("d075"),r=e.n(s);d.a.use(r.a)},b4f1:function(n,t,e){"use strict";e.r(t);var a=function(){var n=this,t=n.$createElement,e=n._self._c||t;return e("d2-container",[e("template",{slot:"header"},[n._v("排序")]),e("d2-crud",{attrs:{columns:n.columns,data:n.data,options:n.options}}),e("el-card",{staticClass:"d2-mb",attrs:{shadow:"never"}},[e("d2-markdown",{attrs:{source:n.doc}})],1),e("el-card",{staticClass:"d2-mb",attrs:{shadow:"never"}},[e("d2-highlight",{attrs:{code:n.code}})],1),e("d2-link-btn",{attrs:{slot:"footer",title:"文档",link:"https://d2.pub/zh/doc/d2-crud-v2"},slot:"footer"})],2)},d=[],s=(e("8099"),e("0320")),r=e.n(s),o=e("6e16"),l={data:function(){return{doc:r.a,code:o["default"],columns:[{title:"日期",key:"date",sortable:!0},{title:"姓名",key:"name"},{title:"地址",key:"address"}],data:[{date:"2016-05-02",name:"王小虎",address:"上海市普陀区金沙江路 1518 弄"},{date:"2016-05-04",name:"王小虎",address:"上海市普陀区金沙江路 1517 弄"},{date:"2016-05-01",name:"王小虎",address:"上海市普陀区金沙江路 1519 弄"},{date:"2016-05-03",name:"王小虎",address:"上海市普陀区金沙江路 1516 弄"}],options:{defaultSort:{prop:"date",order:"descending"}}}}},c=l,u=e("2877"),i=Object(u["a"])(c,a,d,!1,null,null,null);t["default"]=i.exports}}]);