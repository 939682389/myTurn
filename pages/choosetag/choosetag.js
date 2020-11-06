const app = getApp();
var util = require("../../script/utils.js");
Page({

  /**
   * 页面的初始数据
   */
  data: {
    taglist: ['#xxxx', '#xxxx', '#xxxx', '#xxxx', '#xxxx', '#xxxx', '#xxxx', '#xxxx', '#xxxx', '#xxxx', ],
    tags: []
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this
    let url = app.globalData.URL + '/admin/tag';
    util.get(url, {}).then(function (res) {
      console.log(res.data)
      that.setData({
        tags: res.data.data.tags
      })
    })
  },
  choosetag(e) {
    // console.log(e.currentTarget.dataset.id)
    this.setData({
      tagindex: e.currentTarget.dataset.id
    })
  },
  tosearch() {
    wx.setStorageSync('searchTag', this.data.tagindex)
    wx.navigateBack({
      delta: 1
    })
  },
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})