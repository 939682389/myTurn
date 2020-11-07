const app = getApp();
var util = require("../../script/utils.js");
var time = require("../../script/time.js");
Page({
  // 通知类型
  // 0-小组审核 
  // 1-站内好友私信
  // 2-提醒：即将参加的活动
  // 3-参加小组的公告和活动提醒
  // 4-已参加/已过期
  // 5-讨论被回复点赞

  /**
   * 页面的初始数据
   */
  data: {
    currentpage: 1, //当前页数
    fleshlimit: '7', //每次刷新页数
    imgurl: app.globalData.imgurl,
    needflesh: true
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    let that = this
    wx.showLoading({
      title: '加载中...',
      mask: true //显示触摸蒙层  防止事件穿透触发
    });
    //获取通知列表
    let url = app.globalData.URL + '/inform/list';
    var data = {
      limit: that.data.fleshlimit,
      page: that.data.currentpage
    }
    util.get(url, data).then(function (res) {
      let tmp = res.data.data
      for (let i of tmp) {
        i.lasttime = time.formatMsgTime(i.create_time)
        if (i.content != null) {
          if (i.content.length > 10)
            i.content = i.content.substring(0, 10) + '...'
        } else {
          i.content = '暂无'
        }
        if (i.image == null) {
          if (i.user.avatar.length > 40)
            i.image = i.user.avatar
          else
            i.image = 'https://gathering.cooltian.cn/v1/user/img?url=' + i.user.avatar
        } else {
          if (i.image.length < 40)
            i.image = 'https://gathering.cooltian.cn/v1/user/img?url=' + i.image
        }
      }
      that.setData({
        message: tmp
      })
      wx.hideLoading()
    })
  },
  //小组通过审核
  verify(e) {
    var that = this
    console.log(e.currentTarget.dataset.group)
    console.log(e.currentTarget.dataset.user)
    let url = app.globalData.URL + '/group';
    var data = {
      id: e.currentTarget.dataset.group
    }
    util.get(url, data).then(function (res) {
      console.log(res.data.data)
      var groupinfo = res.data.data
      wx.showModal({
        title: '小组名：' + groupinfo.name,
        content: '通过该申请',
        cancelText: '不通过',
        confirmText: '通过',
        success: res => {
          if (res.confirm) {
            console.log('pass')
            let url = app.globalData.URL + '/group/join';
            var data = {
              group_id: e.currentTarget.dataset.group,
              user_id: e.currentTarget.dataset.user,
              audit_status: '1'
            }
            util.other(url, data, 'PUT').then(function (res) {
              console.log(res.data)
              if (res.data.code == 200) {
                wx.showToast({
                  title: '审核成功',
                  duration: 2000,
                  success: function () {
                    console.log('verify success')
                  }
                })
              } else {
                wx.showToast({
                  title: res.data.msg,
                  image: '/img/fail.png',
                  icon: 'success',
                  duration: 2000
                })
              }
            })
          } else {
            console.log('not pass')
            let url = app.globalData.URL + '/group/join';
            var data = {
              group_id: e.currentTarget.dataset.group,
              user_id: e.currentTarget.dataset.user,
              audit_status: '2'
            }
            util.other(url, data, 'PUT').then(function (res) {
              console.log(res.data)
              if (res.data.code == 200) {
                wx.showToast({
                  title: '审核成功',
                  duration: 2000,
                  success: function () {
                    console.log('verify success')
                  }
                })
              } else {
                wx.showToast({
                  title: res.data.msg,
                  image: '/img/fail.png',
                  icon: 'success',
                  duration: 2000
                })
              }
            })
          }
        }
      })
    })
  },
  toUserInfo(e) {
    console.log(e.currentTarget.dataset.id)
    wx.navigateTo({
      url: '/pages/viewUserInfo/viewUserInfo?id=' + e.currentTarget.dataset.id,
    })
  },
  //去详细私信
  totalkdetail(e) {
    console.log('id', e.currentTarget.dataset.id)
    wx.navigateTo({
      url: '/pages/userTalk2/userTalk2?id=' + e.currentTarget.dataset.id,
    })
  },
  togroupdetail(e) {
    console.log(e.currentTarget.dataset.id)
    wx.navigateTo({
      url: '/pages/groupdetail2/groupdetail2?id=' + e.currentTarget.dataset.id,
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
    this.setData({
      currentpage: 1,
      needflesh: true
    })
    console.log('onshow')
    this.onLoad()
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
    // this.onLoad()
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
    var that = this
    if (that.data.needflesh) {
      console.log("上拉刷新")
      wx.showLoading({
        title: '加载中...',
        mask: true //显示触摸蒙层  防止事件穿透触发
      });
      //获取通知列表
      let url = app.globalData.URL + '/inform/list';
      var data = {
        limit: that.data.fleshlimit,
        page: that.data.currentpage + 1
      }
      util.get(url, data).then(function (res) {
        let tmp = that.data.message
        if (res.data.data.length == 0) {
          console.log('no other message')
          that.setData({
            needflesh: false
          })
        }
        for (let i of res.data.data) {
          i.lasttime = time.formatMsgTime(i.create_time)
          if (i.image == null) {
            if (i.user.avatar.length > 40)
              i.image = i.user.avatar
            else
              i.image = 'https://gathering.cooltian.cn/v1/user/img?url=' + i.user.avatar
          } else {
            if (i.image.length < 40)
              i.image = 'https://gathering.cooltian.cn/v1/user/img?url=' + i.image
          }
          tmp.push(i)
        }
        that.setData({
          message: tmp,
          currentpage: that.data.currentpage + 1
        })
        wx.hideLoading()
      })
    }
  },
  todetail(e) {
    console.log(e.currentTarget.dataset.group_id)
    console.log(e.currentTarget.dataset.activity_id)
    wx.navigateTo({
      url: '/pages/groupdDiscuss/groupdDiscuss?id=' + e.currentTarget.dataset.group_id,
    })

  },
  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})