(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2c92ea87","chunk-2d0bd9e3","chunk-2d0dd10e","chunk-2d22d5f9"],{"2d83":function(e,n,o){"use strict";o.r(n),n["default"]="<template>\n  <div>\n    <d2-crud\n      :columns=\"columns\"\n      :data=\"data\"\n      :rowHandle=\"rowHandle\"\n      @row-remove=\"handleRowRemove\"/>\n  </div>\n</template>\n\n<script>\nexport default {\n  data () {\n    return {\n      columns: [\n        {\n          title: '日期',\n          key: 'date'\n        },\n        {\n          title: '姓名',\n          key: 'name'\n        },\n        {\n          title: '地址',\n          key: 'address'\n        }\n      ],\n      data: [\n        {\n          date: '2016-05-02',\n          name: '王小虎',\n          address: '上海市普陀区金沙江路 1518 弄',\n          forbidRemove: true,\n          showRemoveButton: true\n        },\n        {\n          date: '2016-05-04',\n          name: '王小虎',\n          address: '上海市普陀区金沙江路 1517 弄',\n          forbidRemove: false,\n          showRemoveButton: true\n        },\n        {\n          date: '2016-05-01',\n          name: '王小虎',\n          address: '上海市普陀区金沙江路 1519 弄',\n          forbidRemove: false,\n          showRemoveButton: false\n        },\n        {\n          date: '2016-05-03',\n          name: '王小虎',\n          address: '上海市普陀区金沙江路 1516 弄',\n          forbidRemove: false,\n          showRemoveButton: true\n        }\n      ],\n      rowHandle: {\n        remove: {\n          icon: 'el-icon-delete',\n          size: 'small',\n          fixed: 'right',\n          confirm: true,\n          show (index, row) {\n            if (row.showRemoveButton) {\n              return true\n            }\n            return false\n          },\n          disabled (index, row) {\n            if (row.forbidRemove) {\n              return true\n            }\n            return false\n          }\n        }\n      }\n    }\n  },\n  methods: {\n    handleRowRemove ({ index, row }, done) {\n      setTimeout(() => {\n        console.log(index)\n        console.log(row)\n        this.$message({\n          message: '删除成功',\n          type: 'success'\n        })\n        done()\n      }, 300)\n    }\n  }\n}\n<\/script>"},"73fd":function(e,n,o){"use strict";o.r(n);var t=function(){var e=this,n=e.$createElement,o=e._self._c||n;return o("d2-container",[o("template",{slot:"header"},[e._v("删除数据")]),o("d2-crud",{attrs:{columns:e.columns,data:e.data,rowHandle:e.rowHandle},on:{"row-remove":e.handleRowRemove}}),o("el-card",{staticClass:"d2-mb",attrs:{shadow:"never"}},[o("d2-markdown",{attrs:{source:e.doc}})],1),o("el-card",{staticClass:"d2-mb",attrs:{shadow:"never"}},[o("d2-highlight",{attrs:{code:e.code}})],1),o("d2-link-btn",{attrs:{slot:"footer",title:"文档",link:"https://d2.pub/zh/doc/d2-crud-v2"},slot:"footer"})],2)},d=[],r=(o("8099"),o("f6e8")),s=o.n(r),a=o("2d83"),l={data:function(){return{doc:s.a,code:a["default"],columns:[{title:"日期",key:"date"},{title:"姓名",key:"name"},{title:"地址",key:"address"}],data:[{date:"2016-05-02",name:"王小虎",address:"上海市普陀区金沙江路 1518 弄",forbidRemove:!0,showRemoveButton:!0},{date:"2016-05-04",name:"王小虎",address:"上海市普陀区金沙江路 1517 弄",forbidRemove:!1,showRemoveButton:!0},{date:"2016-05-01",name:"王小虎",address:"上海市普陀区金沙江路 1519 弄",forbidRemove:!1,showRemoveButton:!1},{date:"2016-05-03",name:"王小虎",address:"上海市普陀区金沙江路 1516 弄",forbidRemove:!1,showRemoveButton:!0}],rowHandle:{remove:{icon:"el-icon-delete",size:"small",fixed:"right",confirm:!0,show:function(e,n){return!!n.showRemoveButton},disabled:function(e,n){return!!n.forbidRemove}}}}},methods:{handleRowRemove:function(e,n){var o=this,t=e.index,d=e.row;setTimeout((function(){console.log(t),console.log(d),o.$message({message:"删除成功",type:"success"}),n()}),300)}}},i=l,u=o("2877"),m=Object(u["a"])(i,t,d,!1,null,null,null);n["default"]=m.exports},8099:function(e,n,o){"use strict";o.r(n);var t=o("8bbf"),d=o.n(t),r=o("d075"),s=o.n(r);d.a.use(s.a)},f6e8:function(e,n){e.exports="通过给 `D2 Crud` 传入 `rowHandle` 可开启表格操作列，传入 `remove` 对象可以开启删除模式，`confirm` 属性的值为 `Boolean` 类型，控制删除前是否弹出confirm框进行提示， `row-remove` 事件控制数据删除，参数： `index` 是当前删除行的索引， `row` 是当前删除行的数据， `done` 用于控制删除成功，可以在 `done()` 之前加入自己的逻辑代码。代码如下：\n"}}]);