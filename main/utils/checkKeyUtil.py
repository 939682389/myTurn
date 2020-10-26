"""
@Author: Jenkin
@Date: 2020/6/8 3:31 下午
@Description
"""
import hashlib
import time


def getCheckKey():
    sha1 = hashlib.sha1()
    sha1.update(time.strftime("%Y-%m-%d %H", time.localtime()).encode('utf-8'))
    return sha1.hexdigest()


def checkKey(key):
    return key == getCheckKey()


if __name__ == '__main__':
    print(getCheckKey())
    print(checkKey('57074354802fd0ed760b80435e0b41930147410'))
