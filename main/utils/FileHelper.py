from bs4 import BeautifulSoup
import json, time, os
from main import basedir

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF', 'mp4', 'MP4', 'jpeg', 'JPEG'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def resolve_html(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)  # 可以看到网页的内容
        model = {}  # 数据
        data = []
        for p in soup.select('p'):
            # print(p)
            if p.select('img'):
                print(p.select('img')[0].get('src'))
                img = p.select('img')[0].get('src')
                if 'http' not in img:
                    img = 'https://apis.bangstuhelp.com/' + img
                data.append({'img': img, 'type': 'img'})

            else:
                print(p.text)
                data.append({'text': p.text, 'type': 'text'})
        model['data'] = data
        model['html'] = html
        now = int(time.time())
        with open(os.path.join(basedir, "templates", "news", "%s.json" % now), 'w', encoding='utf-8') as json_file:
            json.dump(model, json_file, ensure_ascii=False)
    except Exception as e:
        print(e)
        return False
    return "%s.json" % now

#
# from PIL import Image
#
#
# def add_mark(path, dst_path):
#     # 打开装饰
#     hnu_image = Image.open(r"D:\zjk\项目\xiaoxin\mark.png")
#     # 打开头像
#     nike_image = Image.open(path)
#     # 创建底图
#     target = Image.new('RGBA', nike_image.size, (0, 0, 0, 0))
#     width, height = nike_image.size
#     m = min(width, height) * .2
#     m = int(m)
#     hnu_image = hnu_image.resize((m, m))
#     # 分离透明通道
#     r, g, b, a = hnu_image.split()
#     # 将头像贴到底图
#     nike_image.convert("RGBA")
#
#     target.paste(nike_image, (0, 0))
#     # 将装饰贴到底图
#     hnu_image.convert("RGBA")
#     target.paste(hnu_image, (width - m, height - m), mask=a)
#     # 保存图片
#     target.save(dst_path)
