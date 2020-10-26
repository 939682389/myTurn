"""
@Author: Jenkin
@Date: 2020/6/2 8:19 下午
@Description
"""

from main import db
from main.v1.models import User, Group, GroupJoin, Inform, Message
from sqlalchemy import and_, or_


def query_InformList_by_condition(page, limit, condition):
    qs = Inform.query.filter(Inform.status == True)
    if 'user_id' in condition:
        qs = qs.filter(Inform.user_id == condition['user_id'])
    return qs.paginate(page, limit, False).items


# message
def query_MessageList_by_condition(page, limit, condition):
    qs = Message.query.filter(Message.status == True)
    if 'id' in condition and 'user_id' in condition:
        qs = qs.filter(
            or_(
                and_(Message.from_id == condition['id'], Message.to_id == condition['user_id']),
                and_(Message.from_id == condition['user_id'], Message.to_id == condition['id'])
            )
        )
    return qs.order_by(Message.create_time.desc()).paginate(page, limit, False).items
