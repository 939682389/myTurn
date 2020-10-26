from werkzeug.datastructures import FileStorage

from main import basedir

from flask import request, make_response
import os
from main.code import *
from main.utils import InterfaceHelper, RequestHelper, FileHelper, snowflake, ImageHelper
from main.v1.dbs.user import *
from main.v1.dbs.common import *
from flask_restplus import Resource, fields
from . import api, check_cookie, set_session, check_sig, set_whiteIp, del_whiteIp
from main.miniConfig import HOST

NAMESPACE = "user"
API = HOST + "/v1/" + NAMESPACE

# 定义命名空间
ns = api.namespace(NAMESPACE, description='User api')

user_model = api.model('UserModel', {
    'id': fields.Integer(readOnly=True, description='用户id'),
    'openid': fields.String(description='获取的微信openid'),
    'username': fields.String(description='姓名'),
    'password': fields.String(description='姓名'),
    'nick': fields.String(description='昵称'),
    'avatar': fields.String(description='头像地址'),
    'identity': fields.Integer(description='身份'),
    'location': fields.String(),
    "tags": fields.String(description='[]形式'),
    'private_status': fields.Integer(description='是否允许私信'),
    'exhibition_status': fields.Integer(description='是否展示活动'),
    'access_right': fields.Boolean(description='访问权限'),
    'status': fields.Integer(description='状态'),
    # 'create_time': fields.DateTime(description='时间')
})


@ns.route('/login/<string:code>')
class WxUserLogin(Resource):
    '''用户登陆接口'''

    @ns.doc('user_login')
    def post(self, code):
        """微信用户登录"""
        info = InterfaceHelper.get_openid(code)
        openid = info['openid']
        user = query_user_by_openid(openid)
        if not user:
            user = User(openid=openid)
            insert(user)
            user = query_user_by_openid(openid)
        set_session(user.id)
        return success(user.id, "用户登录成功")


@ns.route('/login')
class UserLoginApi(Resource):
    """用户登陆接口"""

    @ns.doc('user_login')
    @ns.param('user_id')
    def post(self):
        """用户登录（测试）"""
        parameters = RequestHelper.formToDict(request)
        check_sig(method="POST", url=API + "/login", params=parameters)
        set_session(int(parameters['user_id']))
        return success(int(parameters['user_id']))


@ns.route('')
class UserInfoApi(Resource):

    @ns.doc('get_user_info')
    @ns.param('user_id')
    def get(self):
        '''获取用户信息'''
        # user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="GET", url=API + "", params=parameters)
        user = query_user_by_id(parameters['user_id'])
        if user is None:
            return fail('无该用户')
        return success(data=user.to_json(), message='获取用户用户信息成功')

    @ns.doc('put_user_info')
    @ns.expect(user_model)
    def put(self):
        '''用户信息修改'''
        user_id = check_cookie()
        user = query_user_by_id(user_id)
        parameters = RequestHelper.formToDict(request)
        check_sig(method="PUT", url=API + "", params=parameters)

        user = JSONHelper.modifyDictToObj(parameters, user)
        if update(user):
            return success(message='修改成功')
        else:
            return fail(message='修改失败')

    @ns.param('username')
    @ns.param('password')
    @ns.param('identity')
    def post(self):
        '''用户注册'''
        user_id = check_cookie()
        parameters = RequestHelper.formToDict(request)
        check_sig(method="POST", url=API + "", params=parameters)

        if query_user_by_username(username=parameters['username']):
            return fail('用户存在')
        user = query_user_by_id(user_id)
        user.username = parameters['username']
        user.password = parameters['password']
        user.identity = parameters['identity']
        if update(user):
            return success()
        return fail()


@ns.route('/img')
class Img(Resource):
    '''图片'''
    parser = api.parser()
    parser.add_argument('img', type=FileStorage, location='files')

    @ns.doc('post_img')
    @ns.param('type', 'image or video')
    @ns.expect(parser)
    def post(self):
        '''图片上传'''
        filename = None
        parameters = RequestHelper.formToDict(request)
        if not 'type' in parameters:
            get_param_invalid()
        if not parameters['type'] in ['image', 'video']:
            get_type_invalid()
        file = request.files['img']
        if file and FileHelper.allowed_file(file.filename):  # 判断是否是允许上传的文件类型
            ext = file.filename.rsplit('.', 1)[1]  # 获取文件后缀
            # unix_time = int(time.time())
            new_filename = str(snowflake.MySnow(dataID="").get_code()) + '.' + ext
            if not os.path.exists(os.path.join(basedir, "static", parameters['type'])):
                os.makedirs(os.path.join(basedir, "static", parameters['type']))
            filename = os.path.join(parameters['type'], new_filename)
            file_dir = os.path.join(basedir, "static", parameters['type'], new_filename)
            file.save(file_dir)  # 保存文件到upload目录
            if parameters['type'] == 'image':
                ImageHelper.gen_thumbnail(file_dir, new_filename)
        if filename:
            return success({"url": filename}, "图片上传成功")
        return fail('图片上传失败')

    @ns.doc('get_img')
    @ns.param('url')
    @ns.param('watermark', '1-image with watermark')
    @ns.param('quality', '压缩率 1-9')
    def get(self):
        """获取图片"""
        parameters = RequestHelper.formToDict(request)
        # if 'quality' not in parameters:
        #     parameters['quality'] = 10
        image_path = os.path.join(basedir, 'static', parameters['url'])
        if 'url' not in parameters:
            get_param_invalid()
        try:
            image_data = open(image_path, "rb").read()
        except Exception as e:
            print(e)
            return False
        if 'quality' in parameters:
            if 'image' in parameters['url']:
                thumb_path = os.path.join(basedir, 'static', 'thumb')
                image_filename, ext = os.path.basename(parameters['url']).split('.')
                image_filename += '_%s.' % parameters['quality'] + ext
                thumb_image_path = os.path.join(thumb_path, image_filename)
                if not os.path.exists(thumb_image_path):
                    ImageHelper.gen_image_by_ration(image_path, int(parameters['quality']))
                image_data = open(thumb_image_path, "rb").read()

        response = make_response(image_data)
        if 'image' in parameters['url']:
            response.headers['Content-Type'] = 'image/png'
        elif 'thumb' in parameters['url']:
            response.headers['Content-Type'] = 'image/png'
        elif 'video' in parameters['url']:
            response.headers['Content-Type'] = 'video/mp4'
        return response


@ns.route('/ip/white')
class IpWhiteApi(Resource):

    @ns.param('')
    def post(self):
        """设置白名单"""
        set_whiteIp(request.remote_addr)
        return success(request.remote_addr)

    @ns.param('')
    def delete(self):
        """取消白名单"""
        del_whiteIp()
        return success(request.remote_addr)
