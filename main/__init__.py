# coding=utf-8
from datetime import datetime, timedelta
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from main import dbConfig
import os
from flask_cors import *

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    # flask
    app = Flask(__name__, template_folder='./templates', static_folder="./templates", static_url_path="")

    # 解决跨域问题
    CORS(app, supports_credentials=True)

    # 配置数据库
    app.config.from_object(dbConfig)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
    # gunicorn多进程禁用
    # app.config['SECRET_KEY'] = os.urandom(24)  # 设置为24位的字符,每次运行服务器都是不同的，所以服务器启动一次上次的session就清除。
    app.config['SECRET_KEY'] = 'yuepai'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  # 设置session的保存时间。

    # register blueprint
    from main.v1.apis import api_blueprint
    # from .apis.chat import chat_blueprint
    app.register_blueprint(api_blueprint)
    # app.register_blueprint(chat_blueprint)
    return app


def register_api():
    from main.v1.apis import api
    from main.v1.apis.user import ns as user_api
    from main.v1.apis.group import ns as group_api
    from main.v1.apis.admin import ns as admin_api
    from main.v1.apis.inform import ns as inform_api

    api.add_namespace(user_api)
    api.add_namespace(group_api)
    api.add_namespace(admin_api)
    api.add_namespace(inform_api)


app = create_app()
db = SQLAlchemy(app)

# register api namespace
register_api()


@app.route('/index')
def cms():
    return render_template('index.html')


import main.utils.checkKeyUtil as ck
import time


@app.route('/key', methods=['GET'])
def getCheckMd5():
    ip = request.remote_addr
    return jsonify({'key': ck.getCheckKey(), 'ip': ip})


@app.route('/login', methods=['GET'])
def login():
    ip = request.remote_addr
    return render_template('login.html', key=ck.getCheckKey(),
                           time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


@app.route('/success', methods=['GET'])
def success():
    ip = request.remote_addr
    name = request.args.get("name")

    return render_template('success.html', name=name,
                           date=(datetime.now()).strftime("%Y-%m-%d"),
                           sx="下午(13:30--20:00)" if int(datetime.now().strftime("%H")) >= 13 else "上午(06:30--13:00)",
                           time1=(datetime.now() + timedelta(days=-1) + timedelta(seconds=-9)).strftime(
                               "%Y-%m-%d %H:%M:%S"),
                           time2=(datetime.now() + timedelta(hours=-1) + timedelta(minutes=-3) + timedelta(
                               seconds=-1)).strftime(
                               "%Y-%m-%d %H:%M:%S"),
                           time3=(datetime.now()).strftime("%Y-%m-%d %H:%M:%S"))


@app.route('/out', methods=['GET'])
def out():
    key = request.args.get("key")
    if not ck.checkKey(key):
        return jsonify({'msg': 'check fail'})
    name = request.args.get("name")
    id = request.args.get("id")
    if checkName(name) or str(datetime.today()).split(' ')[0] == '2020-07-11':
        return render_template('out.html', name=name, id=id,
                               time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    return render_template('400.html')


@app.route('/in', methods=['GET'])
def inx():
    key = request.args.get("key")
    if not ck.checkKey(key):
        return jsonify({'msg': 'check fail'})
    name = request.args.get("name")
    id = request.args.get("id")
    if checkName(name) or str(datetime.today()).split(' ')[0] == '2020-07-11':
        return render_template('in.html', name=name, id=id,
                               time=(datetime.now() + timedelta(hours=-1)).strftime("%Y-%m-%d %H:%M:%S"))
    return render_template('400.html')


def checkName(name):
    names = ["章金凯", '范健良', "袁浩", "张智敏", "徐豪郡", "王荣伟", "王荣伟", "孔启超", "陈浩然", "程宇航", "潘智裔",
             "厉晌煦", "林珊珊", "袁玲玲", "娄方莹", "陈凡", "王唯", "林姜毅", "康梦玲", "姜丽雯", "戎炫霖", "严晓"]
    return name in names
