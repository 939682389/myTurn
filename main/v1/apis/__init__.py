from flask_restplus import Resource, Api
from flask import Blueprint, request, session
from main.code import user_not_login, admin_not_login, check_signature_fail, get_signature_param_fail
from main.utils import sigUtils

api_blueprint = Blueprint("open_api", __name__, url_prefix="/v1")
api = Api(api_blueprint, version='1.0', title='聚玩 API',
          description='gathering API v1.0',
          )


def check_cookie():
    c = session.get("userId")
    if not c:
        user_not_login()
    else:
        return int(c)


def check_admin_cookie():
    c = session.get("adminId")
    print(c)
    if not c:
        admin_not_login()
    else:
        return int(c)


def set_session(user_id):
    session['userId'] = user_id


def set_admin_session(user_id):
    session['adminId'] = user_id


def set_whiteIp(ip):
    session['white'] = ip


def del_whiteIp():
    session.pop('white')


def check_sig(method, url, params):
    """

    :param method:
    :param url:
    :param params:
    :return:
    """
    if session.get('white') == request.remote_addr:
        return True
    code = sigUtils.chkSig(method=method, url=url, params=params)
    if code == 0:
        check_signature_fail()
    elif code == 40001:
        get_signature_param_fail()
