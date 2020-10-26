from main import db
from main import app
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DateTime, Date, JSON
from datetime import datetime
from main.utils import TimeHelper


class User(db.Model):
    """用户"""
    __tablename__ = "user"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer(), primary_key=True)
    openid = Column(String(31))
    username = Column(String(31))
    password = Column(String(31))
    nick = Column(String(31))
    avatar = Column(String(255))
    identity = Column(Integer)  # user identity 0-user 1-admin 2-checker
    location = Column(String(255))
    introduction = Column(String(255))
    private_status = Column(Integer)
    exhibition_status = Column(Integer)
    tags = Column(JSON)
    status = Column(Boolean, default=True)
    create_time = Column(DateTime, default=datetime.now())

    def to_json(self):
        dict = self.__dict__
        if "create_time" in dict:
            if dict["create_time"]:
                dict["create_time"] = TimeHelper.datetime_toString_short(dict["create_time"])
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


class Group(db.Model):
    __tablename__ = "group"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    name = Column(String(31))
    introduction = Column(String(255))  # 简介
    announcement = Column(String(255))  # 公告
    number = Column(Integer)
    question = Column(String(255))
    image = Column(String(255))
    status = Column(Boolean, default=True)
    create_time = Column(DateTime, default=datetime.now())

    def to_json(self):
        dict = self.__dict__
        if "create_time" in dict:
            if dict["create_time"]:
                dict["create_time"] = TimeHelper.datetime_toString_short(dict["create_time"])
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


class Activity(db.Model):
    __tablename__ = "activity"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('group.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    type = Column(Integer)  # 0-线上游戏 1-经验分享 2-影视鉴赏 3-美食探店
    title = Column(String(31))
    time = Column(DateTime, default=datetime.now())
    location = Column(String(255))
    summarize = Column(String(255))
    number = Column(Integer)
    image = Column(String(255))
    tags = Column(JSON)
    notice_status = Column(Integer)
    status = Column(Boolean, default=True)
    create_time = Column(DateTime, default=datetime.now())

    def to_json(self):
        dict = self.__dict__
        for i in dict.keys():
            if type(dict[i]) == datetime:
                dict[i] = TimeHelper.datetime_toString_short(dict[i])
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


class GroupJoin(db.Model):
    __tablename__ = "group_join"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('group.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    audit_status = Column(Integer, default=0)  # 0-未审核 1-通过 2-拒绝
    status = Column(Boolean, default=True)
    create_time = Column(DateTime, default=datetime.now())

    def to_json(self):
        dict = self.__dict__
        if "create_time" in dict:
            if dict["create_time"]:
                dict["create_time"] = TimeHelper.datetime_toString_short(dict["create_time"])
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


class ActivityJoin(db.Model):
    __tablename__ = "activity_join"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    activity_id = Column(Integer, ForeignKey('activity.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    status = Column(Boolean, default=True)
    create_time = Column(DateTime, default=datetime.now())

    def to_json(self):
        dict = self.__dict__
        if "create_time" in dict:
            if dict["create_time"]:
                dict["create_time"] = TimeHelper.datetime_toString_short(dict["create_time"])
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


class GroupTopic(db.Model):
    __tablename__ = "group_topic"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    content = Column(String(255))
    group_id = Column(Integer, ForeignKey('group.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    topic_id = Column(Integer)
    status = Column(Boolean, default=True)
    create_time = Column(DateTime, default=datetime.now())

    def to_json(self):
        dict = self.__dict__
        if "create_time" in dict:
            if dict["create_time"]:
                dict["create_time"] = TimeHelper.datetime_toString_short(dict["create_time"])
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


class GroupTopicPrise(db.Model):
    __tablename__ = "group_topic_prise"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    content = Column(String(255))
    group_topic_id = Column(Integer, ForeignKey('group_topic.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

    status = Column(Boolean, default=True)
    create_time = Column(DateTime, default=datetime.now())

    def to_json(self):
        dict = self.__dict__
        if "create_time" in dict:
            if dict["create_time"]:
                dict["create_time"] = TimeHelper.datetime_toString_short(dict["create_time"])
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


class Inform(db.Model):
    __tablename__ = "inform"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    content = Column(String(255))
    image = Column(String(255))
    title = Column(String(255))
    type = Column(Integer)  # 通知类型0-小组审核 1-站内好友私信 2-提醒：即将参加的活动 3-参加小组的公告和活动提醒 4-已参加/已过期 5-讨论被回复点赞
    user_id = Column(Integer, ForeignKey('user.id'))
    group_id = Column(Integer, ForeignKey('group.id'))
    activity_id = Column(Integer, ForeignKey('activity.id'))
    from_user_id = Column(Integer, ForeignKey('user.id'))
    status = Column(Boolean, default=True)
    create_time = Column(DateTime, default=datetime.now())

    def to_json(self):
        dict = self.__dict__
        if "create_time" in dict:
            if dict["create_time"]:
                dict["create_time"] = TimeHelper.datetime_toString_short(dict["create_time"])
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


class Collection(db.Model):
    __tablename__ = "collection"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    activity_id = Column(Integer, ForeignKey('activity.id'))
    status = Column(Boolean, default=True)
    create_time = Column(DateTime, default=datetime.now())

    def to_json(self):
        dict = self.__dict__
        if "create_time" in dict:
            if dict["create_time"]:
                dict["create_time"] = TimeHelper.datetime_toString_short(dict["create_time"])
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


class Message(db.Model):
    __tablename__ = "message"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    from_id = Column(Integer, ForeignKey('user.id'))
    to_id = Column(Integer, ForeignKey('user.id'))
    content = Column(String(255))
    status = Column(Boolean, default=True)
    create_time = Column(DateTime, default=datetime.now())

    def to_json(self):
        dict = self.__dict__
        if "create_time" in dict:
            if dict["create_time"]:
                dict["create_time"] = TimeHelper.datetime_toString_short(dict["create_time"])
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


class Admin(db.Model):
    __tablename__ = "admin"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    username = Column(String(31))
    password = Column(String(31))
    status = Column(Boolean, default=True)
    create_time = Column(DateTime, default=datetime.now())

    def to_json(self):
        dict = self.__dict__
        if "create_time" in dict:
            if dict["create_time"]:
                dict["create_time"] = TimeHelper.datetime_toString_short(dict["create_time"])
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


# create tables
db.create_all()

if __name__ == '__main__':
    # create tables
    # db.create_all()
    app.run(debug=True)
