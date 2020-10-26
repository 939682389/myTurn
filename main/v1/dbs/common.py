from main import db
from sqlalchemy.exc import InvalidRequestError
from main.utils import JSONHelper
from datetime import datetime
from main.v1.models import Inform
from sqlalchemy import or_, and_, func


def insert(object):
    try:
        if type(object) == list:
            for i in object:
                i.create_time = datetime.now()
                db.session.add(i)
        else:
            object.create_time = datetime.now()
            db.session.add(object)
        db.session.commit()
        return True
    # except InvalidRequestError as e:
    #     print(e)
    #     db.session.rollback()
    except Exception as e:
        print(e)
        return False


def update(object):
    try:
        # object.create_time = datetime.now()
        db.session.commit()
        return True
    except InvalidRequestError:
        db.session.rollback()
    except Exception as e:
        print(e)
        return False


def addInform(user_id, type, content=None, image=None, group_id=None, activity_id=None, from_user_id=None):
    """
    添加通知
    :param content:
    :param image:
    :param type:     通知类型0-小组审核 1-站内好友私信 2-提醒：即将参加的活动 3-参加小组的公告和活动提醒 4-已参加/已过期 5-讨论被回复 6-讨论被点赞
    :param user_id:
    :param group_id:
    :return:
    """
    titles = ["你有待审核信息",
              "你有好友私信",
              "你有即将参加的活动",
              "你参加的小组有新的公告",
              "你的活动已过期",
              "你的讨论被回复",
              "你的讨论被点赞"]
    inform = Inform(title=titles[type], type=type, user_id=user_id)
    if image:
        inform.image = image
    if group_id:
        inform.group_id = group_id
    if content:
        inform.content = content
    if activity_id:
        inform.activity_id = activity_id
    if from_user_id:
        inform.from_user_id = from_user_id
    if insert(inform):
        return True
    return False
