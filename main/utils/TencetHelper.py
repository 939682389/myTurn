import requests
import hmac
import hashlib
import base64
import time
import random
import re
import os

def OCR(dir):
    appid = "1256381563"
    bucket = "" #参考本文开头提供的链接
    secret_id = "AKIDlMioobGVdWBbnviSr21lKflbCXcX9hww"  #参考官方文档
    secret_key = "tXw74mGVWIq9HBqHWVEpAF4dx2rQltlO"  #同上
    expired = time.time() + 2592000
    onceExpired = 0
    current = time.time()
    rdm = ''.join(random.choice("0123456789") for i in range(10))
    userid = "0"
    fileid = "tencentyunSignTest"
    info = "a=" + appid + "&b=" + bucket + "&k=" + secret_id + "&e=" + str(expired) + "&t=" + str(current) + "&r=" + str(
        rdm) + "&u=0&f="
    signindex = hmac.new(bytes(secret_key,'utf-8'),bytes(info,'utf-8'), hashlib.sha1).digest()  # HMAC-SHA1加密
    sign = base64.b64encode(signindex + bytes(info,'utf-8'))  # base64转码，也可以用下面那行转码
    #sign=base64.b64encode(signindex+info.encode('utf-8'))

    url = "http://recognition.image.myqcloud.com/ocr/general"
    headers = {'Host': 'recognition.image.myqcloud.com',
               "Authorization": sign,
               }
    files = {'appid': (None,appid),
        'bucket': (None,bucket),
        'image': ('1.jpg', open(os.path.join("../templates/image", dir), 'rb'), 'image/jpeg')
        }
    r = requests.post(url, files=files,headers=headers)
    responseinfo = r.content
    data = responseinfo.decode('utf-8')
    name_index = r'itemstring":"姓名:(.*?)"'  # 做一个正则匹配
    card_index = r'itemstring":"学号:(.*?)"'  # 做一个正则匹配
    name = re.findall(name_index, data)
    if name:
        name = name[0].replace(" ", "")
    card = re.findall(card_index, data)
    if card:
        card = card[0].replace(" ", "")
    return {'name': name, 'student_id': card}


if __name__ == '__main__':
    print(OCR(r"C:\Users\zjk\Desktop\730AC9094F52512D0DA2A181B94171C1.png"))