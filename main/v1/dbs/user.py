from main import db
from main.v1.models import User, Group, GroupJoin
from sqlalchemy import and_


# user

def query_user_by_id(id):
    return User.query.filter(User.id == id).first()


def query_user_by_phone(phone):
    return User.query.filter(User.phone == phone).first()


def query_user_by_username(username):
    return User.query.filter(User.username == username).first()


def query_user_by_openid(openid):
    return db.session.query(User).filter(User.openid == openid).first()


def query_userList_by_groupId(groupId, order_by=None, keyword=None):
    qs = User.query.join(GroupJoin).filter(and_(GroupJoin.user_id == User.id,
                                                      GroupJoin.group_id == groupId))
    if order_by:
        if order_by == '2':
            qs = qs.order_by(db.desc(GroupJoin.create_time))
        elif order_by == '3':
            qs = qs.order_by(db.desc(User.nick))
    if keyword != None:
        qs = qs.filter(User.nick.like('%' + keyword + '%'))
    return qs.filter(and_(GroupJoin.status == True, GroupJoin.audit_status == 1)).all()


def query_userList_by_condition(page, limit, condition=None):
    qs = User.query.filter(User.status == True)
    return qs.paginate(page, limit, False).items


if __name__ == '__main__':
    print(query_userList_by_groupId(8, '3'))
