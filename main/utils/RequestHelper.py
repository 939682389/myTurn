import json, requests, re


# 获取的form转dict
def formToDict(request):
    try:
        # print(request.data)
        if request.form:
            print('form')
            dict = json.dumps(request.form)
            dict = json.loads(dict)
        elif request.args:
            print('args')
            dict = json.dumps(request.args)
            dict = json.loads(dict)
        elif request.json:
            print('json')
            dict = json.dumps(request.json, ensure_ascii=False)
            dict = json.loads(dict)
        elif request.data:
            print('data')
            dict = json.dumps(request.data, ensure_ascii=False)
            dict = json.loads(dict)
        else:
            dict = {}
    except Exception as e:
        print('error', e)
        return {}
    return dict


def get_wx_article_title(url):
    try:
        res = requests.get(url)
        dict = {}
        dict['title'] = re.findall('msg_title = "([\S\s]+?)";', res.text)[0]
        dict['content'] = re.findall('msg_desc = "([\S\s]+?)";', res.text)[0].replace('\\x0a', '\n')
    except Exception as e:
        print(e)
    return dict


if __name__ == '__main__':
    url = "https://mp.weixin.qq.com/s/r5sz9VukLwA0VO06KrVJJg"
    print(get_wx_article_title(url))
