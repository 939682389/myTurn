# pwdUtils 爱码仕密码算法 v0.1.0.200611
# by SalzFischKatze 2020年6月11日
# 仅限于学习研究使用
# QQ523301264
from hashlib import sha256
import hashlib
import random


def genRanStr(length):
    ranStr = ''
    base = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    baseLen = len(base) - 1
    for i in range(length):
        ranStr += base[random.randint(0, baseLen)]
    return ranStr


def newPwd(orig):
    # 生成16位随机字符串
    random = genRanStr(16)
    # 原始口令进行一次SHA256计算
    pwd = hashlib.sha256(orig.encode()).hexdigest() + random
    # 拼接随机字符串后进行一次SHA256计算
    pwd = hashlib.sha256(pwd.encode()).hexdigest()
    # 拼接结果
    pwd = '$SHA256$' + random + '$' + pwd
    return pwd


def chkPwd(orig, dbPwd):
    # 分离数据库中的密码
    splitResult = dbPwd.split('$')
    # 原始口令进行一次SHA256计算
    pwd = hashlib.sha256(orig.encode()).hexdigest() + splitResult[2]
    # 拼接随机字符串后进行一次SHA256计算
    pwd = hashlib.sha256(pwd.encode()).hexdigest()
    # 比较结果
    if pwd == splitResult[3]:
        return 1
    else:
        return 0
