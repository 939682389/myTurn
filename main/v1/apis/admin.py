"""
@Author: Jenkin
@Date: 2020/5/31 10:06 下午
@Description
"""
import json

from main import basedir

from flask import request, make_response
import os
from main.code import *
from main.utils import InterfaceHelper, RequestHelper, FileHelper, snowflake, ImageHelper, pwdUtils
from main.v1.dbs.group import *
from main.v1.dbs.common import *
from main.v1.dbs.user import *
from main.v1.dbs.admin import *

from flask_restplus import Resource, fields
from . import api, check_cookie, set_session, set_admin_session, check_admin_cookie, check_sig
from main.miniConfig import HOST

NAMESPACE = "admin"
API = HOST + "/v1/" + NAMESPACE
# 定义命名空间
ns = api.namespace(NAMESPACE, description='Admin api')


@ns.route('/tag')
class TagApi(Resource):

    @ns.param('tag')
    def post(self):
        """添加标签"""
        parameters = RequestHelper.formToDict(request)
        check_sig(method="POST", url=API + "/tag", params=parameters)

        if 'tags' in parameters:
            get_data_fail()
        try:
            with open("tags.json", 'r') as load_f:
                data = json.load(load_f)
        except:
            data = {
                'tags': []
            }
        data['tags'].append(parameters['tag'])
        with open("tags.json", "w") as f:
            json.dump(data, f)
        return success()

    def get(self):
        """获取标签"""
        try:
            with open("tags.json", 'r') as load_f:
                data = json.load(load_f)
        except:
            data = {
                'tags': []
            }
        return success(data)

    @ns.param('index', '索引')
    @ns.param('tag')
    def put(self):
        parameters = RequestHelper.formToDict(request)
        check_sig(method="PUT", url=API + "/tag", params=parameters)
        try:
            with open("tags.json", 'r') as load_f:
                data = json.load(load_f)
        except:
            data = {
                'tags': []
            }
        try:
            index = int(parameters['index'])
            data['tags'][index] = parameters['tag']
            with open("tags.json", "w") as f:
                json.dump(data, f)
        except Exception as e:
            return fail(e)
        return success()

    @ns.param('index', '索引')
    def delete(self):
        """删除标签"""
        parameters = RequestHelper.formToDict(request)
        check_sig(method="DELETE", url=API + "/tag", params=parameters)
        try:
            with open("tags.json", 'r') as load_f:
                data = json.load(load_f)
        except:
            data = {
                'tags': []
            }
        try:
            index = int(parameters['index'])
            data['tags'].pop(index)
            with open("tags.json", "w") as f:
                json.dump(data, f)
        except Exception as e:
            return fail(e)
        return success()


@ns.route('/login')
class LoginApi(Resource):

    @ns.param('username')
    @ns.param('password')
    def post(self):
        """登陆"""
        parameters = RequestHelper.formToDict(request)
        check_sig(method="POST", url=API + "/login", params=parameters)
        admin = query_admin_by_username(parameters['username'])
        if not admin:
            get_data_fail()
        pwdUtils.chkPwd(parameters['password'], admin.password)
        if admin:
            set_admin_session(admin.id)
            return success(admin.id)
        return fail()


@ns.route('/register')
class LoginApi(Resource):

    @ns.param('username')
    @ns.param('password')
    def post(self):
        """注册"""
        parameters = RequestHelper.formToDict(request)
        check_sig(method="POST", url=API + "/register", params=parameters)
        admin = Admin(username=parameters['username'], password=pwdUtils.newPwd(parameters['password']))
        if insert(admin):
            return success(admin.id)
        return fail()


@ns.route('/activity/tags')
class GroupTags(Resource):

    @ns.param('tags', '[] list格式')
    @ns.param('id')
    def put(self):
        """修改活动标签"""
        parameters = RequestHelper.formToDict(request)
        check_sig(method="PUT", url=API + "/activity/tags", params=parameters)

        activity = query_activity_by_id(parameters['id'])
        activity.tags = parameters['tags']
        if update(activity):
            return success()
        return fail()


@ns.route('/user/list')
class UserListApi(Resource):

    @ns.param('page')
    @ns.param('limit')
    def get(self):
        """获取用户列表"""
        parameters = RequestHelper.formToDict(request)
        check_sig(method="GET", url=API + "/user/list", params=parameters)

        data = []
        for i in query_userList_by_condition(int(parameters['page']), int(parameters['limit'])):
            data.append(i.to_json())
        return success(data)
