"""
@Author: Jenkin
@Date: 2020/6/4 8:49 下午
@Description
"""
from main import basedir

from flask import request, make_response
import os
from main.code import *
from main.utils import InterfaceHelper, RequestHelper, FileHelper, snowflake, ImageHelper
from main.v1.dbs.group import *
from main.v1.dbs.common import *
from main.v1.dbs.user import *
from main.v1.dbs.inform import *
from flask_restplus import Resource, fields
from . import api, check_cookie, set_session, check_sig
from main.miniConfig import HOST

NAMESPACE = "inform"
API = HOST + "/v1/" + NAMESPACE

# 定义命名空间
ns = api.namespace(NAMESPACE, description='Inform api')


@ns.route('/message')
class MessageApi(Resource):

    @ns.param('from_id', '发送者id')
    @ns.param('to_id', '接受者id')
    @ns.param('content', '内容')
    def post(self):
        """发送私信"""
        user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="POST", url=API + "/message", params=parameters)
        message = Message(from_id=parameters['from_id'], to_id=parameters['to_id'], content=parameters['content'])
        if insert(message):
            addInform(type=1, user_id=parameters['to_id'], content=parameters['content'], from_user_id=user_id)
            return success()
        return fail()


@ns.route('/message/list')
class MessageListApi(Resource):

    @ns.param('id', '私信对象')
    @ns.param('page')
    @ns.param('limit')
    def get(self):
        """获得私信列表"""
        user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="GET", url=API + "/message/list", params=parameters)

        parameters['user_id'] = user_id
        data = []
        for i in query_MessageList_by_condition(int(parameters['page']), int(parameters['limit']), parameters):
            data.append(i.to_json())
        return success(data)


@ns.route("/list")
class InformApi(Resource):

    @ns.param('page')
    @ns.param('limit')
    def get(self):
        """获取通知列表"""
        user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="GET", url=API + "/list", params=parameters)

        parameters['user_id'] = user_id
        data = []
        for i in query_InformList_by_condition(int(parameters['page']), int(parameters['limit']), parameters):
            if i.user_id:
                i.user = query_user_by_id(i.user_id).to_json()
            if i.from_user_id:
                i.from_user = query_user_by_id(i.from_user_id).to_json()
            data.append(i.to_json())
        return success(data)


# def addInform(type, user_id=None, group_id=None):
#     """
#
#     :param type: 通知类型0-小组审核 1-站内好友私信 2-提醒：即将参加的活动 3-参加小组的公告和活动提醒 4-已参加/已过期 5-讨论被回复点赞
#     :param user_id:
#     :param group_id:
#     :return:
#     """
#     inform = Inform(type=type, user_id=user_id, group_id=group_id)
#     if insert(inform):
#         return True
#     return False
