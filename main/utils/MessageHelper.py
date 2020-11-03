#!/usr/bin/env python
#coding=utf-8
import json
import random
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest


def get_code(phone, code):
    client = AcsClient('', '', 'cn-hangzhou')

    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https') # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('SignName', "微搬砖")
    request.add_query_param('TemplateCode', "SMS_187560620")
    request.add_query_param('TemplateParam', '{"code":"%s"}'% code)
    request.add_query_param('PhoneNumbers', "%s" % phone)

    response = client.do_action(request)
    # python2:  print(response)
    responses = json.loads(str(response, encoding='utf-8'))
    # print(responses)
    return responses['Message'] == 'OK'


def generate_verification_code(len=6):
    ''' 随机生成6位的验证码 '''
    code_str = ""
    for i in range(len):
        code_str += str(random.randint(0, 9)) # 随机生成0-9的数字
    return code_str


if __name__ == '__main__':
    print(get_code(17376566698, 1233))