"""
@Author: Jenkin
@Date: 2020/5/23 10:28 下午
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

NAMESPACE = "group"
API = HOST + "/v1/" + NAMESPACE
# 定义命名空间
ns = api.namespace(NAMESPACE, description='Group api')

group_model = api.model('GroupModel', {
    'id': fields.Integer(readOnly=True, description='id'),
    # 'user_id': fields.Integer(description="用户id"),
    "announcement": fields.String(description="公告"),
    'name': fields.String(),
    'introduction': fields.String(),
    'number': fields.Integer(description="人数"),
    'question': fields.String(),
    'image': fields.String(),
    # 'status': fields.Integer(description='状态'),
    # 'create_time': fields.DateTime(description='时间')
})
activity_model = api.model('ActivityModel', {
    'id': fields.Integer(readOnly=True, description='id'),
    'type': fields.Integer(description="0-线上游戏 1-经验分享 2-影视鉴赏 3-美食探店"),
    'group_id': fields.Integer(),
    'user_id':fields.Integer(),
    'title': fields.String(),
    'time': fields.DateTime(),
    'location': fields.String(),
    'summarize': fields.String(),
    'notice_status': fields.Integer(description='是否需要提醒 0-否 1-是'),
    'number': fields.Integer(description="人数"),
    'image': fields.String(),
    'tags': fields.String(description="['xx','xx']"),
    # 'status': fields.Integer(description='状态'),
    # 'create_time': fields.DateTime(description='时间')
})

group_topic_model = api.model('GroupTopicModel', {
    'id': fields.Integer(readOnly=True, description='id'),
    'content': fields.String(description='内容'),
    'group_id': fields.Integer(),
    'topic_id': fields.Integer(description="回复需要填写，否则不填"),
    'user_id': fields.Integer(),
})


@ns.route('')
class GroupApi(Resource):

    # @ns.doc(params={'usernameOrEmail': 'An account'})
    @ns.expect(group_model)
    def post(self):
        """添加小组"""
        user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="POST", url=API + "", params=parameters)
        group = JSONHelper.dictToObj(parameters, Group)
        group.user_id = user_id
        if insert(group):
            return success(group.id)
        return fail()

    @ns.expect(group_model)
    def put(self):
        """修改小组"""
        # user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="PUT", url=API + "", params=parameters)
        if 'id' not in parameters:
            get_param_invalid()
        group = query_group_by_id(parameters['id'])
        group = JSONHelper.modifyDictToObj(parameters, group)
        if update(group):
            if 'announcement' in parameters:
                for i in query_userList_by_groupId(group.id):
                    addInform(type=3, user_id=i.id, image=group.image, group_id=group.id)
            return success()
        return fail()

    @ns.param('id', '小组id')
    def delete(self):
        """删除小组"""
        # user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="DELETE", url=API + "", params=parameters)
        if 'id' not in parameters:
            get_param_invalid()
        group = query_group_by_id(parameters['id'])
        group.status = False
        if update(group):
            return success()
        return fail()

    @ns.param('id')
    def get(self):
        """获取小组详情"""
        # user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="GET", url=API + "", params=parameters)
        if 'id' not in parameters:
            get_param_invalid()
        group = query_group_by_id(parameters['id'])
        group.user = query_user_by_id(group.user_id).to_json()
        return success(group.to_json())


@ns.route('/list')
class GroupListApi(Resource):

    @ns.param("isHot", '1-人气小组 否则不传')
    @ns.param('user_id', '某人创建的小组')
    @ns.param('keyword', '关键词')
    @ns.param('page', '页码 从1开始')
    @ns.param('limit', '数量')
    def get(self):
        """获取小组列表"""
        parameters = RequestHelper.formToDict(request)
        check_sig(method="GET", url=API + "/list", params=parameters)
        if 'page' not in parameters or 'limit' not in parameters:
            get_param_invalid()
        data = []
        for i in query_groupList_by_condition(int(parameters['page']), int(parameters['limit']), parameters):
            i.applicantNum = count_groupJoin_by_groupId(i.id)  # 活动参与人数
            data.append(i.to_json())
        return success(data)


@ns.route('/activity')
class ActivityApi(Resource):

    @ns.expect(activity_model)
    def post(self):
        """添加活动"""
        # user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="POST", url=API + "/activity", params=parameters)
        activity = JSONHelper.dictToObj(parameters, Activity)
        if insert(activity):
            return success(activity.id)
        return fail()

    @ns.expect(activity_model)
    def put(self):
        """修改活动"""
        # user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="PUT", url=API + "/activity", params=parameters)
        if 'id' not in parameters:
            get_param_invalid()
        activity = query_activity_by_id(parameters['id'])
        if not activity:
            return get_data_fail()
        activity = JSONHelper.modifyDictToObj(parameters, activity)
        if update(activity):
            return success()
        return fail()

    @ns.param('id')
    def delete(self):
        """删除活动"""
        # user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="DELETE", url=API + "/activity", params=parameters)

        if 'id' not in parameters:
            get_param_invalid()
        activity = query_activity_by_id(parameters['id'])
        activity.status = False
        if update(activity):
            return success()
        return fail()

    @ns.param('id')
    def get(self):
        """获取活动详情"""
        parameters = RequestHelper.formToDict(request)
        check_sig(method="GET", url=API + "/activity", params=parameters)

        if 'id' not in parameters:
            get_param_invalid()
        activity = query_activity_by_id(parameters['id'])
        activity.group = query_group_by_id(activity.group_id).to_json()
        activity.user = query_user_by_id(activity.group['user_id']).to_json()
        return success(activity.to_json())


@ns.route('/activity/join')
class ActivityJoinApi(Resource):

    @ns.param('activity_id')
    def post(self):
        """加入活动"""
        user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="POST", url=API + "/activity/join", params=parameters)
        join = query_activityJoin_by_activityId_userId(parameters['activity_id'], user_id)
        if join:
            join.status = True
            if update(join):
                return success(join.id)
        join = ActivityJoin(user_id=user_id, activity_id=parameters['activity_id'])
        if insert(join):
            return success(join.id)
        return fail()

    @ns.param('id', 'activity id')
    def delete(self):
        """用户退出活动"""
        user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="DELETE", url=API + "/activity/join", params=parameters)

        if 'id' not in parameters:
            get_param_invalid()
        join = query_activityJoin_by_activityId_userId(parameters['id'], user_id)
        if not join:
            get_data_fail()
        join.status = False
        if update(join):
            return success()
        return fail()

    @ns.param('activity_id')
    def get(self):
        user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="GET", url=API + "/activity/join", params=parameters)

        if 'activity_id' not in parameters:
            get_param_invalid()
        join = query_activityJoin_by_activityId_userId(parameters['activity_id'], user_id)
        if join:
            return success(join.status)
        return success(False)


@ns.route('/activity/join/user/list')
class ActivityJoinUserListApi(Resource):

    @ns.param('user_id')
    @ns.param('activity_id')
    @ns.param('page')
    @ns.param('limit')
    def get(self):
        """获取加入活动用户列表"""
        parameters = RequestHelper.formToDict(request)
        check_sig(method="GET", url=API + "/activity/join/user/list", params=parameters)

        if 'page' not in parameters or 'limit' not in parameters:
            get_param_invalid()
        date = []
        for i in query_activityJoinList_by_condition(int(parameters['page']), int(parameters['limit']), parameters):
            i.user = query_user_by_id(i.user_id).to_json()
            date.append(i.to_json())
        return success(date)


@ns.route('/activity/join/list')
class ActivityJoinListApi(Resource):

    @ns.param('page')
    @ns.param('limit')
    @ns.param('user_id')
    def get(self):
        """获取参加活动列表"""
        parameters = RequestHelper.formToDict(request)
        check_sig(method="GET", url=API + "/activity/join/list", params=parameters)
        if 'page' not in parameters or 'limit' not in parameters:
            get_param_invalid()
        date = []
        for i in query_activityJoinList_by_condition(int(parameters['page']), int(parameters['limit']), parameters):
            i.activity = query_activity_by_id(i.activity_id).to_json()
            date.append(i.to_json())
        return success(date)


@ns.route('/activity/list')
class ActivityListApi(Resource):

    @ns.param('page')
    @ns.param('limit')
    @ns.param('type', '0-线上游戏 1-经验分享 2-影视鉴赏 3-美食探店')
    @ns.param('keyword', '搜索关键词')
    @ns.param('group_id')
    @ns.param('isHot', '1-hot')
    @ns.param('order', '0-参与人数 1-最新发布')
    @ns.param('isComing', '是否即将到来 1-即将到来')
    @ns.param('isExpired', '是否过期 0-未过期 1-过期')
    @ns.param('user_id', '创建者id')
    def get(self):
        """获取活动列表"""
        parameters = RequestHelper.formToDict(request)
        check_sig(method="GET", url=API + "/activity/list", params=parameters)

        if 'page' not in parameters or 'limit' not in parameters:
            get_param_invalid()
        data = []
        for i in query_activityList_by_condition(int(parameters['page']), int(parameters['limit']), parameters):
            i.applicantNum = count_activityJoin_by_activityId(i.id)
            data.append(i.to_json())
        return success(data)


@ns.route('/topic')
class GroupTopicApi(Resource):

    @ns.expect(group_topic_model)
    def post(self):
        """添加小组讨论"""
        user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="POST", url=API + "/topic", params=parameters)
        groupTopic = JSONHelper.dictToObj(parameters, GroupTopic)
        groupTopic.user_id = user_id
        if 'topic_id' in parameters:
            tpl = query_groupTopic_by_id(parameters['topic_id'])
            addInform(type=5, user_id=tpl.user_id, group_id=tpl.group_id)
        if insert(groupTopic):
            return success(groupTopic.id)
        return fail()

    @ns.param('topic_id')
    def delete(self):
        """删除用户讨论"""
        # user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="DELETE", url=API + "/topic", params=parameters)
        topic = query_groupTopic_by_id(parameters['topic_id'])
        if topic:
            topic.status = False
            if update(topic):
                return success()
        return fail()


@ns.route('/topic/list')
class GroupTopicListApi(Resource):

    @ns.param('page')
    @ns.param('limit')
    @ns.param('group_id')
    def get(self):
        """获取用户小组讨论列表"""
        user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="GET", url=API + "/topic/list", params=parameters)
        if 'page' not in parameters or 'limit' not in parameters:
            get_param_invalid()
        data = []
        parameters['isReply'] = None
        for i in query_groupTopicList_by_condition(int(parameters['page']), int(parameters['limit']), parameters):
            i.user = query_user_by_id(i.user_id).to_json()
            gtp = query_groupTopicPraise_by_userId_groupTopicPraiseId(user_id, i.id)
            i.praise = gtp.status if gtp else False
            i.praiseNum = count_groupTopicPraise_by_groupTopicPraiseId(i.id)
            i.reply = findReply(user_id, i.id)
            data.append(i.to_json())
        return success(data)


def findReply(userId, topicId):
    """
    查找评论
    :param userId:
    :param topicId:
    :return:
    """
    replys = []
    for j in query_groupTopicReplyList(topicId):
        j.user = query_user_by_id(j.user_id).to_json()
        gtp = query_groupTopicPraise_by_userId_groupTopicPraiseId(userId, j.id)
        j.praise = gtp.status if gtp else False
        j.praiseNum = count_groupTopicPraise_by_groupTopicPraiseId(j.id)
        j.replys = findReply(userId, j.id)
        replys.append(j.to_json())
    return replys


@ns.route('/topic/praise')
class GroupTopicPraiseApi(Resource):

    @ns.param('id', "group_topic_id")
    def post(self):
        """话题点赞"""
        user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="POST", url=API + "/topic/praise", params=parameters)
        if 'id' not in parameters:
            get_param_invalid()
        praise = query_groupTopicPraise_by_userId_groupTopicPraiseId(user_id, parameters['id'])
        gt = query_groupTopic_by_id(parameters['id'])
        addInform(type=6, user_id=gt.user_id, group_id=gt.group_id, from_user_id=user_id)
        if praise:
            if not praise.status:
                praise.status = True
                update(praise)
            return success()
        prise = GroupTopicPrise(group_topic_id=parameters['id'], user_id=user_id)
        if insert(prise):
            return success(prise.id)
        return fail()

    @ns.param('id', "group_topic_id")
    def get(self):
        """查询点赞状态"""
        user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="GET", url=API + "/topic/praise", params=parameters)
        if 'id' not in parameters:
            get_param_invalid()
        praise = query_groupTopicPraise_by_userId_groupTopicPraiseId(user_id, parameters['id'])
        if praise:
            if praise.status:
                return success(True, "用户点赞")
        return fail("用户没点赞")

    @ns.param('id', "group_topic_id")
    def delete(self):
        """取消点赞状态"""
        user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="DELETE", url=API + "/topic/praise", params=parameters)
        if 'id' not in parameters:
            get_param_invalid()
        praise = query_groupTopicPraise_by_userId_groupTopicPraiseId(user_id, parameters['id'])
        if praise:
            if praise.status:
                praise.status = False
                update(praise)
                return success(True)
        return fail()


@ns.route('/join')
class GroupJoinApi(Resource):

    @ns.param('group_id')
    @ns.param('answer', '问题回答')
    def post(self):
        """用户加入小组"""
        user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="POST", url=API + "/join", params=parameters)

        if 'answer' not in parameters:
            get_param_invalid()
        join = query_groupJoin_by_groupId_userId(parameters['group_id'], user_id)
        if join:
            if not join.status:
                join.status = True
                update(join)
            return success(join.id)
        join = GroupJoin(user_id=user_id, group_id=parameters['group_id'])
        # 发送消息
        if insert(join):
            group = query_group_by_id(parameters['group_id'])
            addInform(type=0, user_id=group.user_id, content=parameters['answer'], group_id=group.id,
                      from_user_id=user_id)
            return success(join.id)
        return fail()

    @ns.param('id', 'group id')
    def delete(self):
        """用户退出小组"""
        user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="DELETE", url=API + "/join", params=parameters)
        join = query_groupJoin_by_groupId_userId(parameters['id'], user_id)
        if not join:
            get_data_fail()
        join.status = False
        if update(join):
            return success()
        return fail()

    @ns.param('audit_status', '审核状态 0-未审核 1-通过 2-拒绝')
    @ns.param('user_id')
    @ns.param('group_id')
    def put(self):
        """修改审核状态"""
        # user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="PUT", url=API + "/join", params=parameters)

        join = query_groupJoin_by_groupId_userId(parameters['group_id'], parameters['user_id'])
        if 'audit_status' not in parameters:
            get_param_invalid()
        if not join:
            get_data_fail()
        join.audit_status = parameters['audit_status']
        if update(join):
            return success()
        return fail()

    @ns.param('user_id')
    @ns.param('group_id')
    def get(self):
        """获取小组加入状态"""
        # user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="GET", url=API + "/join", params=parameters)
        join = query_groupJoin_by_groupId_userId(parameters['group_id'], parameters['user_id'])
        if not join:
            get_data_fail()
        return success(join.to_json())



@ns.route('/join/list')
class GroupJoinListApi(Resource):

    @ns.param('user_id')
    @ns.param('page')
    @ns.param('limit')
    @ns.param('audit_status', '审核状态 0-未审核 1-通过 2-拒绝')
    def get(self):
        """获取参加小组"""
        parameters = RequestHelper.formToDict(request)
        check_sig(method="GET", url=API + "/join/list", params=parameters)

        if 'page' not in parameters or 'limit' not in parameters:
            get_param_invalid()
        date = []
        for i in query_groupJoinList_by_condition(int(parameters['page']), int(parameters['limit']), parameters):
            i.user = query_user_by_id(i.user_id).to_json()
            i.group = query_group_by_id(i.group_id).to_json()
            i.applicantNum = count_groupJoin_by_groupId(i.group_id)  # 活动参与人数
            date.append(i.to_json())
        return success(date)


@ns.route('/join/user/list')
class JoinUserListApi(Resource):

    @ns.param('group_id')
    @ns.param('order_by', '1-活跃度 2-最新添加 3-按字母')
    @ns.param('keyword', '搜索关键词')
    def get(self):
        """获取加入小组用户列表"""
        parameters = RequestHelper.formToDict(request)
        check_sig(method="GET", url=API + "/join/user/list", params=parameters)

        if 'group_id' not in parameters:
            get_param_invalid()
        data = []
        for i in query_userList_by_groupId(parameters['group_id'],
                                           order_by=parameters['order_by'] if 'order_by' in parameters else None):
            data.append(i.to_json())
        return success(data)


@ns.route('/collection')
class CollectionApi(Resource):

    @ns.param('activity_id')
    def post(self):
        """添加收藏"""
        user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="POST", url=API + "/collection", params=parameters)

        if 'activity_id' not in parameters:
            get_param_invalid()
        collection = Collection(activity_id=parameters['activity_id'], user_id=user_id)
        if insert(collection):
            return success(collection.id)
        return fail()

    @ns.param('id', 'activity id')
    def delete(self):
        """删除收藏"""
        user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="DELETE", url=API + "/collection", params=parameters)

        if 'id' not in parameters:
            get_param_invalid()
        collection = query_collection_by_activityId_userId(parameters['id'], user_id)
        if not collection:
            get_data_fail()
        collection.status = False
        if update(collection):
            return success()
        return fail()

    @ns.param('activity_id')
    def get(self):
        """获取用户收藏状态"""
        user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="GET", url=API + "/collection", params=parameters)

        if 'activity_id' not in parameters:
            get_param_invalid()
        collection = query_collection_by_activityId_userId(parameters['activity_id'], user_id)
        if collection:
            return success(collection.status)
        return success(False)


@ns.route('/collection/list')
class CollectionListApi(Resource):

    @ns.param('page')
    @ns.param('limit')
    def get(self):
        """获取收藏列表"""
        user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="GET", url=API + "/collection/list", params=parameters)

        if 'page' not in parameters or 'limit' not in parameters:
            get_param_invalid()
        parameters['user_id'] = user_id
        data = []
        for i in query_collectionList_by_condition(int(parameters['page']), int(parameters['limit']), parameters):
            i.activity = query_activity_by_id(i.activity_id).to_json()
            data.append(i.to_json())
        return success(data)
