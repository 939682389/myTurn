(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-6a07b8b6","chunk-2d21de13"],{"61b7":function(e,t,i){"use strict";i.r(t);var o=function(){var e=this,t=e.$createElement,i=e._self._c||t;return i("div",[i("el-table",{directives:[{name:"loading",rawName:"v-loading",value:e.loading,expression:"loading"}],staticStyle:{width:"100%"},attrs:{data:e.currentTableData,size:"mini",stripe:""},on:{"selection-change":e.handleSelectionChange}},[i("el-table-column",{attrs:{type:"selection",width:"50"}}),i("el-table-column",{attrs:{label:"id",width:"100",align:"center","show-overflow-tooltip":!0},scopedSlots:e._u([{key:"default",fn:function(t){return[e._v(" "+e._s(t.row.id)+" ")]}}])}),i("el-table-column",{attrs:{label:"小组id",width:"100",align:"center","show-overflow-tooltip":!0},scopedSlots:e._u([{key:"default",fn:function(t){return[e._v(" "+e._s(t.row.group_id)+" ")]}}])}),i("el-table-column",{attrs:{label:"封面",width:"80",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){return[i("el-image",{staticStyle:{width:"80px",height:"80px"},attrs:{src:e.APP_API+"user/img?url="+t.row.image},on:{click:function(i){return e.imagePreview(t.row.image)}}})]}}])}),i("el-table-column",{attrs:{label:"标题",width:"160",align:"center","show-overflow-tooltip":!0},scopedSlots:e._u([{key:"default",fn:function(t){return[i("div",{on:{click:function(i){return e.seeDetail(t.row.title,"title",t.row.id)}}},[e._v(e._s(t.row.title))])]}}])}),i("el-table-column",{attrs:{label:"概述",width:"160",align:"center","show-overflow-tooltip":!0},scopedSlots:e._u([{key:"default",fn:function(t){return[i("div",{on:{click:function(i){return e.seeDetail(t.row.summarize,"summarize",t.row.id)}}},[e._v(e._s(t.row.summarize))])]}}])}),i("el-table-column",{attrs:{label:"时间",width:"160",align:"center","show-overflow-tooltip":!0},scopedSlots:e._u([{key:"default",fn:function(t){return[i("div",{on:{click:function(i){return e.seeDetail(t.row.time,"time",t.row.id)}}},[e._v(e._s(t.row.time))])]}}])}),i("el-table-column",{attrs:{label:"地点",width:"120",align:"center","show-overflow-tooltip":!0},scopedSlots:e._u([{key:"default",fn:function(t){return[i("div",{on:{click:function(i){return e.seeDetail(t.row.location,"location",t.row.id)}}},[e._v(e._s(t.row.location))])]}}])}),i("el-table-column",{attrs:{label:"标签",width:"200",align:"center","show-overflow-tooltip":!0},scopedSlots:e._u([{key:"default",fn:function(t){return[i("div",{on:{click:function(i){return e.seeDetail(t.row.tags,"tags",t.row.id)}}},[e._v(e._s(t.row.tags))])]}}])}),i("el-table-column",{attrs:{label:"类型",width:"120",align:"center","show-overflow-tooltip":!0},scopedSlots:e._u([{key:"default",fn:function(t){return[i("div",{on:{click:function(i){return e.seeDetail(t.row.type,"type",t.row.id)}}},[e._v(e._s(t.row.type))])]}}])}),i("el-table-column",{attrs:{label:"成员数量",width:"80",align:"center","show-overflow-tooltip":!0},scopedSlots:e._u([{key:"default",fn:function(t){return[e._v(" "+e._s(t.row.number)+" ")]}}])}),i("el-table-column",{attrs:{label:"申请数量",width:"80",align:"center","show-overflow-tooltip":!0},scopedSlots:e._u([{key:"default",fn:function(t){return[e._v(" "+e._s(t.row.applicantNum)+" ")]}}])}),i("el-table-column",{attrs:{label:"创建时间",width:"180",align:"center","show-overflow-tooltip":!0},scopedSlots:e._u([{key:"default",fn:function(t){return[e._v(" "+e._s(t.row.create_time)+" ")]}}])}),i("el-table-column",{attrs:{label:"操作",width:"200",align:"center","show-overflow-tooltip":!0},scopedSlots:e._u([{key:"default",fn:function(t){return[i("el-button",{attrs:{type:"primary",size:"small",round:""},on:{click:function(i){e.newImageVisible=!0,e.rowId=t.row.id}}},[e._v("新封面")]),i("el-button",{attrs:{type:"danger",size:"small",round:""},on:{click:function(i){return e.handleDelete(t.row.id)}}},[e._v("删除")])]}}])})],1),i("el-dialog",{attrs:{visible:e.imageVisible},on:{"update:visible":function(t){e.imageVisible=t}}},[i("el-image",{staticStyle:{height:"60vh"},attrs:{fit:"fit",src:e.imageUrl}})],1),i("el-dialog",{attrs:{visible:e.contentVisible,title:"查看详情"},on:{"update:visible":function(t){e.contentVisible=t},close:function(t){e.modifyVisible=!1}}},[0==e.modifyVisible?i("span",{domProps:{innerHTML:e._s(e.content)}},[e._v(e._s(e.content))]):e._e(),e.modifyVisible&&"time"==e.type?i("el-date-picker",{attrs:{type:"datetime",placeholder:"请选择时间"},model:{value:e.time,callback:function(t){e.time=t},expression:"time"}}):e._e(),e.modifyVisible&&"type"==e.type?i("el-select",{attrs:{placeholder:"请选择类型"},model:{value:e.type_select,callback:function(t){e.type_select=t},expression:"type_select"}},e._l(e.types,(function(e){return i("el-option",{key:e.value,attrs:{label:e.label,value:e.value}})})),1):e._e(),e.modifyVisible&&"tags"==e.type?i("el-checkbox-group",{model:{value:e.tags_select,callback:function(t){e.tags_select=t},expression:"tags_select"}},e._l(e.tags,(function(t){return i("el-checkbox",{attrs:{label:t.value}},[e._v(e._s(t.label))])})),1):e._e(),e.modifyVisible&&"time"!=e.type&&"tags"!=e.type&&"type"!=e.type?i("el-input",{attrs:{placeholder:"请输入要修改的内容",type:"textarea",autosize:"",clearable:""},model:{value:e.content,callback:function(t){e.content=t},expression:"content"}}):e._e(),i("span",{attrs:{slot:"footer"},slot:"footer"},[0==e.modifyVisible?i("el-button",{on:{click:function(t){e.modifyVisible=!0}}},[e._v("修 改")]):e._e(),e.modifyVisible?i("el-button",{on:{click:function(t){e.modifyVisible=!1}}},[e._v("取 消")]):e._e(),e.modifyVisible?i("el-button",{attrs:{type:"primary"},on:{click:function(t){return e.handleModify()}}},[e._v("确 定")]):e._e()],1)],1),i("el-dialog",{attrs:{visible:e.newImageVisible},on:{"update:visible":function(t){e.newImageVisible=t}}},[i("div",{staticStyle:{display:"flex","justify-content":"center"}},[i("div",{staticStyle:{display:"flex","justify-content":"center","align-items":"center","flex-direction":"column",width:"178px"}},[i("el-upload",{ref:"upload",attrs:{drag:"",action:e.APP_API+"user/img",data:e.data,name:"img","on-success":e.handleSuccess,"on-preview":e.handlePictureCardPreview,"on-exceed":e.handleOnExceed,"auto-upload":!1,accept:".jpg,.jpeg,.png,.JPG,.JPEG,.PNG",limit:1}},[i("i",{staticClass:"el-icon-upload"}),i("div",{staticClass:"el-upload__text"},[e._v("将图片拖到此处，或"),i("em",[e._v("点击上传")])]),i("div",{staticClass:"el-upload__tip",attrs:{slot:"tip"},slot:"tip"},[e._v("只能上传jpg/jpeg/png文件")])]),i("el-button",{staticStyle:{width:"178px","margin-top":"10px"},attrs:{size:"small",type:"success"},on:{click:e.submitUpload}},[e._v("上传到服务器")])],1)])])],1)},l=[],n=(i("d81d"),i("d3b7"),i("3ca3"),i("ddb0"),i("2b3d"),i("ade3")),a=i("9c5c"),s=i("d2d3"),c={props:{tableData:{default:function(){return[]}},loading:{default:!1}},data:function(){return{APP_API:"https://gathering.cooltian.cn/v1/",currentTableData:[],rowId:-1,imageVisible:!1,imageUrl:"",contentVisible:!1,content:"",type:"",time:"",type_select:"",types:[{value:0,label:"线上游戏"},{value:1,label:"经验分享"},{value:2,label:"影视鉴赏"},{value:3,label:"美食探店"}],tags_select:[],modifyVisible:!1,newImageVisible:!1,data:{type:"image"},tags:[]}},watch:{tableData:{handler:function(e){this.currentTableData=e},immediate:!0}},mounted:function(){var e=this;Object(a["i"])().then((function(t){console.log(t.data),200==t.data.code&&(e.tags=t.data.data.tags.map((function(e,t){return{value:t,label:e}})))})).catch((function(t){e.$notify.error("获取标签失败，请刷新页面重试"),console.log("err",t)}))},methods:{submitUpload:function(){var e=this;this.$confirm("确定上传吗").then((function(t){e.$refs.upload.submit()}))},handleSuccess:function(e,t){var i=this;console.log(e.data),Object(a["k"])({id:this.rowId,image:e.data.url}).then((function(e){console.log(e.data),200==e.data.code&&(i.$notify.success("上传成功"),i.$refs.upload.clearFiles(),i.newImageVisible=!1,i.$emit("submit"))})).catch((function(e){i.$notify.error("未知错误，请刷新页面重试"),console.log("err",e)}))},handlePictureCardPreview:function(e){this.imageUrl=URL.createObjectURL(e.raw),this.imageVisible=!0},handleOnExceed:function(){this.$notify.warning("一次只能上传一个文件")},handleSelectionChange:function(e){this.$emit("select",e)},handleDelete:function(e){var t=this;this.$confirm("确定删除吗").then((function(i){Object(a["d"])({id:e}).then((function(e){console.log(e.data),200==e.data.code&&(t.$notify.success("删除成功"),t.$emit("submit"))})).catch((function(e){t.loading=!1,t.$notify.error("未知错误，请刷新页面重试"),console.log("err",e)}))}))},handleModify:function(){var e=this;if(this.contentVisible=!1,this.modifyVisible=!1,"tags"!=this.type){if("time"==this.type){if(!this.time)return void this.$notify.error("时间不能为空");this.time instanceof Date==1?this.content=s.formatTime(this.time):this.content=this.time}else"type"==this.type&&(this.content=this.type_select);Object(a["k"])(Object(n["a"])({id:this.rowId},this.type,this.content)).then((function(t){console.log(t.data),200==t.data.code&&(e.$notify.success("修改内容成功"),e.type_select="",e.$emit("submit"))})).catch((function(t){e.loading=!1,e.$notify.error("未知错误，请刷新页面重试"),console.log("err",t)}))}else Object(a["b"])({id:this.rowId,tags:this.tags_select}).then((function(t){console.log(t.data),200==t.data.code&&(e.$notify.success("修改标签成功"),e.tags_select=[],e.$emit("submit"))})).catch((function(t){e.loading=!1,e.$notify.error("未知错误，请刷新页面重试"),console.log("err",t)}))},seeDetail:function(e,t,i){this.type=t,this.rowId=i,"time"==t&&(this.time=e),this.content=e,this.contentVisible=!0},imagePreview:function(e){this.imageUrl=this.APP_API+"user/img?url="+e,this.imageVisible=!0}}},r=c,u=i("2877"),d=Object(u["a"])(r,o,l,!1,null,null,null);t["default"]=d.exports},d2d3:function(e,t,i){i("a15b"),i("d81d"),i("d3b7"),i("25f0");var o=function(e){var t=e.getFullYear(),i=e.getMonth()+1,o=e.getDate(),n=e.getHours(),a=e.getMinutes(),s=e.getSeconds();return[t,i,o].map(l).join("-")+" "+[n,a,s].map(l).join(":")},l=function(e){return e=e.toString(),e[1]?e:"0"+e};e.exports={formatTime:o}}}]);