import json
import requests
import urllib.request

appId = "wx4b9edd12cab20a6d"
secret = "219c8a3cb759dcf722d8220c04815d87"
grant_type = "authorization_code"


def get_openid(code):
    url = "https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code" \
          % (appId, secret, code)
    res = requests.get(url)
    print(res.text)
    return json.loads(res.text)


def get_ACCESS_TOKEN():
    '''
    获取access token
    :return:
    '''
    access_token = ''
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (appId, secret)
    res = requests.get(url)
    j = json.loads(res.text)
    # print(j['access_token'])
    try:
        access_token = j['access_token']
    except Exception as e:
        print(e)
    return access_token


def subscribeMessageSend(ACCESS_TOKEN, openid, template_id, page, data):
    URL = 'https://api.weixin.qq.com/cgi-bin/message/subscribe/send?access_token=%s' % ACCESS_TOKEN
    data = {
        "touser": openid,
        "template_id": template_id,
        "data": data,
    }
    res = requests.post(url=URL, data=data)
    print(res.text)


def get_QrCode(path):
    '''获取小程序二维码'''
    url = "https://api.weixin.qq.com/wxa/getwxacode?access_token=" + get_ACCESS_TOKEN()
    data = {"path": path}
    res = requests.post(url, json=data)
    return res.content
    # with open('picture.jpg', 'wb') as file:
    #     file.write(res.content)
    # print(res.text)

if __name__ == '__main__':
    get_QrCode("pages/home/home")
    # access_token = get_ACCESS_TOKEN()
    # subscribeMessageSend(access_token,
    #                      "osp325cIk6HwCRS4uvUd2aDoKlQk",
    #                      "Zn2DBcLoLzmUm-HAThphRH7CtUJ7gMwkK5oplJx13vA",
    #                      "",
    #                      {
    #                          "name06": { "value": "测试" },
    #                          "date03": { "value": "2019年10月1日 15:01" },
    #                          "thing02": { "value": "测试"}})

    from main.utils.WXBizDataCrypt import WXBizDataCrypt
    sessionKey = 'yFA\/u12F1z8103ccWD+btA=='
    iv = '1JNSqB9Ahe5P59y7fjwebQ=='
    encryptedData = 'SV2ZOV3c0zwFGBcCi7Km3d2h14Nd1NZpU880I6COQzcm8Z9cijFoAVag6NmrODc2Wzq1Ih9epZBTJX4qn3HUd4xOEXwn0z6FrNd2y/4/GIsq8MhMdNvsaCdoSESSjVLhdyI6DcGKHBTExWjvsTrvLpnYb0uKZj6D8AOQRk72xKhdKsOwGz/Q5aPyEzHclbpqo5sGh6brLSd2JjTTvEww2g=='
    # def get_phone(sessionKey, encryptedData, iv):
    pc = WXBizDataCrypt(appId, sessionKey)
    print(pc.decrypt(encryptedData, iv))

