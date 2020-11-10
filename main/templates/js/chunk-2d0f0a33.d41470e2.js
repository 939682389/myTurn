(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d0f0a33"],{"9ce8":function(n,t,a){"use strict";a.r(t),t["default"]="<template>\n  <div>\n    <d2-crud\n      :columns=\"columns\"\n      :data=\"data\"\n      :loading=\"loading\"\n      :pagination=\"pagination\"\n      @pagination-current-change=\"paginationCurrentChange\"/>\n  </div>\n</template>\n\n<script>\nexport default {\n  data () {\n    return {\n      columns: [\n        {\n          title: '卡密',\n          key: 'key',\n          width: 320\n        },\n        {\n          title: '面值',\n          key: 'value'\n        },\n        {\n          title: '管理员',\n          key: 'admin'\n        },\n        {\n          title: '创建时间',\n          key: 'dateTimeCreat'\n        },\n        {\n          title: '使用时间',\n          key: 'dateTimeUse'\n        }\n      ],\n      data: [],\n      loading: false,\n      pagination: {\n        currentPage: 1,\n        pageSize: 5,\n        total: 0\n      }\n    }\n  },\n  mounted () {\n    this.fetchData()\n  },\n  methods: {\n    paginationCurrentChange (currentPage) {\n      this.pagination.currentPage = currentPage\n      this.fetchData()\n    },\n    fetchData () {\n      this.loading = true\n      this.$api.DEMO_BUSINESS_TABLE_1_LIST({\n        ...this.pagination\n      }).then(res => {\n        this.data = res.list\n        this.pagination.total = res.page.total\n        this.loading = false\n      }).catch(err => {\n        console.log('err', err)\n        this.loading = false\n      })\n    }\n  }\n}\n<\/script>"}}]);