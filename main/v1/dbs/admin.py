"""
@Author: Jenkin
@Date: 2020/6/6 10:57 下午
@Description
"""
from main.v1.models import Admin
from sqlalchemy import or_, and_


def query_admin_by_username_password(usernmae, password):
    return Admin.query.filter(and_(Admin.username == usernmae, Admin.password == password)).first()


def query_admin_by_username(username):
    return Admin.query.filter(Admin.username == username).first()
