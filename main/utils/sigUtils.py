# sigUtils 爱码仕签名算法 v0.1.1.200609
# by SalzFischKatze 2020年6月9日
# 仅限于学习研究使用
# QQ523301264
import json
import time
from urllib import parse
import urllib
import base64
import hmac
from hashlib import sha1
import hashlib

key = '723a80b7adf38fc8'  # HmacSHA1密钥
# url编码替换的特殊字符
# %20 - py会将空格编码，js不会; %5C - py会将unicode编码为%5Cuxxxx，js为%uxxxx
oldSym = ['*', '/', '-', '_', '.', ':', '%20', '%22', '+', '%5C']
newSym = ['%2A', '%2F', '%2D', '%5F', '%2E', '%3A', '', '', '%2B', '%']


def genSig(method, url, params):
    # 拷贝params
    origin_params = params
    # 生成当前时间戳
    ts = round(time.time() * 1000)
    # 对url及params进行url编码，替换部分特殊字符
    url = parse.quote(url.replace('\n', '').replace('\r', '').replace('\\', ''))
    params = parse.quote(json.dumps(params).replace('\n', '').replace('\r', '').replace('\\', ''))
    for i, sym in enumerate(oldSym):
        url = url.replace(sym, newSym[i])
        params = params.replace(sym, newSym[i])
    # 将method、url、params、ts用&拼接
    comb = method + '&' + url + '&' + params + '&' + str(ts)
    # 使用key对拼接后的字符串进行散列值计算
    hmac_result = hmac.new(key.encode(), comb.encode(), sha1).digest()
    # base64编码
    sig = base64.b64encode(hmac_result).decode()
    # 添加ts、sig字段
    origin_params['ts'] = ts
    origin_params['sig'] = sig
    # 返回原始参数加上ts、sig字段
    return origin_params


def chkSig(method, url, params):
    try:
        # 提取ts、sig字段
        ts = params['ts']
        sig = parse.unquote(params['sig'])
    except KeyError as e:
        # 无ts、sig字段处理
        print('无' + str(e) + '字段')
        return 40001
    # 删除ts、sig字段后计算散列值
    del params['ts']
    del params['sig']
    # 对url及params进行url编码，替换部分特殊字符
    url = parse.quote(url.replace('\n', '').replace('\r', '').replace('\\', ''))
    params = parse.quote(json.dumps(params).replace('\n', '').replace('\r', '').replace('\\', ''))
    for i, sym in enumerate(oldSym):
        url = url.replace(sym, newSym[i])
        params = params.replace(sym, newSym[i])
    # 将method、url、params、ts用&拼接
    comb = method + '&' + url + '&' + params + '&' + str(ts)
    # 使用key对拼接后的字符串进行散列值计算
    hmac_result = hmac.new(key.encode(), comb.encode(), sha1).digest()
    # base64编码
    chk = base64.b64encode(hmac_result).decode()
    # 验证通过返回1，不通过返回0
    if chk == sig:
        return 1
    else:
        return 0
