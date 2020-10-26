"""
@Author: Jenkin
@Date: 2020/5/23 10:28 下午
@Description
"""

from main import db
from main.v1.models import Group, GroupJoin, GroupTopic, GroupTopicPrise, Activity, Collection, ActivityJoin
from sqlalchemy import or_, and_, func, desc
from datetime import datetime


# group
def query_groupList_by_condition(page, limit, condition={}):
    """
    查询小组列表
    :param page:
    :param limit:
    :param condition:
    :return:
    """
    qs = Group.query.filter(Group.status == True)
    if 'isHot' in condition:
        qs = qs.order_by(Group.number.desc())
    if 'user_id' in condition:
        qs = qs.filter(Group.user_id == condition['user_id'])
    if 'keyword' in condition:
        qs = qs.filter(Group.name.like('%' + condition['keyword'] + '%'))
    return qs.order_by(Group.create_time.desc()).paginate(page, limit, False).items


def query_group_by_id(id):
    return Group.query.filter(Group.id == id).first()


# activity
def query_activityList_by_condition(page, limit, condition={}):
    """

    :param page:
    :param limit:
    :param condition:
    :return:
    """
    qs = None
    if 'isHot' in condition:
        condition['order'] = '0'
    if 'order' in condition:
        if condition['order'] == '0':
            qs = db.session.query(Activity, func.count(ActivityJoin.activity_id).label('total')).outerjoin(
                ActivityJoin).group_by(Activity). \
                filter(Activity.status == True)
    if not qs:
        qs = db.session.query(Activity).filter(Activity.status == True)
    if 'type' in condition:
        qs = qs.filter(Activity.type == condition['type'])

    if 'keyword' in condition:
        qs = qs.filter(or_(
            Activity.title.like('%' + condition['keyword'] + '%'),
            Activity.summarize.like('%' + condition['keyword'] + '%')
        ))
    if 'group_id' in condition:
        qs = qs.filter(Activity.group_id == condition['group_id'])
    if 'user_id' in condition:
        qs = qs.filter(Activity.user_id == condition['user_id'])
    if 'order' in condition:
        if condition['order'] == '0':
            # qs = qs.order_by(Activity.number.desc())
            qs = qs.order_by(desc('total'))
        elif condition['order'] == '1':
            qs = qs.order_by(Activity.time.desc())
    if 'isExpired' in condition:
        if condition['isExpired'] == '0':
            qs = qs.filter(Activity.time >= datetime.now())
        elif condition['isExpired'] == '1':
            qs = qs.filter(Activity.time < datetime.now())
    if 'isComing' in condition:
        qs = qs.filter(Activity.time >= datetime.now())
    if 'order' in condition:
        if condition['order'] == '0':
            return [i[0] for i in qs.paginate(page, limit, False).items]

    return qs.order_by(Activity.time.desc()).paginate(page, limit, False).items


def query_activity_by_id(id):
    return Activity.query.filter(Activity.id == id).first()


def query_activityList_by_groupId(groupId):
    return Activity.query.filter(and_(Activity.status == True,
                                      Activity.group_id == groupId)).all()


# join
def query_groupJoin_by_id(id):
    return GroupJoin.query.filter(GroupJoin.id == id).first()


def query_groupJoin_by_groupId_userId(groupId, userId):
    return GroupJoin.query.filter(and_(GroupJoin.group_id == groupId,
                                       GroupJoin.user_id == userId)).first()


def count_groupJoin_by_groupId(groupId):
    return GroupJoin.query.filter(and_(GroupJoin.group_id == groupId,
                                       GroupJoin.status == True)).count()


def query_groupJoinList_by_condition(page, limit, condition={}):
    """
    :param page:
    :param limit:
    :param condition:
    :return:
    """
    qs = GroupJoin.query.filter(GroupJoin.status == True)
    if 'user_id' in condition:
        qs = qs.filter(GroupJoin.user_id == condition['user_id'])
    if 'audit_status' in condition:
        qs = qs.filter(GroupJoin.audit_status == condition['audit_status'])
    return qs.paginate(page, limit, False).items


# group topic
def query_groupTopic_by_id(id):
    return GroupTopic.query.filter(GroupTopic.id == id).first()


def query_groupTopicList_by_condition(page, limit, condition={}):
    """
    :param page:
    :param limit:
    :param condition:
    :return:
    """
    qs = GroupTopic.query.filter(GroupTopic.status == True)
    if 'group_id' in condition:
        qs = qs.filter(GroupTopic.group_id == condition['group_id'])
    if 'topic_id' in condition:
        qs = qs.filter(GroupTopic.group_id == condition['topic_id'])
    if 'isReply' in condition:
        qs = qs.filter(GroupTopic.topic_id == condition['isReply'])
    return qs.paginate(page, limit, False).items


def query_groupTopicReplyList(topic_id):
    return GroupTopic.query.filter(GroupTopic.status == True).filter(GroupTopic.topic_id == topic_id).all()


# topic praise
def query_groupTopicPraise_by_id(id):
    return GroupTopicPrise.query.filter(id == id).first()


def query_groupTopicPraise_by_userId_groupTopicPraiseId(userId, groupTopicId):
    return GroupTopicPrise.query.filter(and_(
        GroupTopicPrise.user_id == userId,
        GroupTopicPrise.group_topic_id == groupTopicId
    )).first()


def count_groupTopicPraise_by_groupTopicPraiseId(groupTopicId):
    return GroupTopicPrise.query.filter(GroupTopicPrise.group_topic_id == groupTopicId).count()


# collection
def query_collection_by_id(id):
    return Collection.query.filter(Collection.id == id).first()


def query_collection_by_activityId_userId(activityId, userId):
    return Collection.query.filter(and_(Collection.activity_id == activityId,
                                        Collection.user_id == userId)).first()


def query_collectionList_by_condition(page, limit, condition={}):
    """
    查询小组列表
    :param page:
    :param limit:
    :param condition:
    :return:
    """
    qs = Collection.query.filter(Collection.status == True)
    if 'user_id' in condition:
        qs = qs.filter(Collection.user_id == condition['user_id'])
    return qs.paginate(page, limit, False).items


# activity join
def query_activityJoin_by_id(id):
    return ActivityJoin.query.filter(ActivityJoin.id == id).first()


def query_activityJoin_by_activityId_userId(activityId, userId):
    return ActivityJoin.query.filter(and_(ActivityJoin.activity_id == activityId,
                                          ActivityJoin.user_id == userId)).first()


def count_activityJoin_by_activityId(activityId):
    return ActivityJoin.query.filter(and_(ActivityJoin.activity_id == activityId,
                                          ActivityJoin.status == True)).count()


def query_activityJoinList_by_condition(page, limit, condition={}):
    """
    :param page:
    :param limit:
    :param condition:
    :return:
    """
    qs = ActivityJoin.query.filter(ActivityJoin.status == True)
    if 'user_id' in condition:
        qs = qs.filter(ActivityJoin.user_id == condition['user_id'])
    if 'activity_id' in condition:
        qs = qs.filter(ActivityJoin.activity_id == condition['activity_id'])
    return qs.paginate(page, limit, False).items


if __name__ == '__main__':
    print(query_activityList_by_condition(1, 10, {'order': '0'}))
