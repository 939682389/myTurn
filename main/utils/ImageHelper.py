from PIL import Image
import os
from main import basedir


def gen_thumbnail(file, filename, width=160):
    '''生成缩略图，缩略图长边为256'''
    img = Image.open(file)
    ration = max(img.size)/width
    print(ration)
    size = (int(img.size[0]/ration), int(img.size[1]/ration))
    img.thumbnail(size)
    thumb_dir = os.path.join(basedir, "static", 'thumb')
    if not os.path.exists(thumb_dir):
        os.makedirs(thumb_dir)
    img.save(os.path.join(thumb_dir, filename))


def gen_image_by_ration(filePath, ration):
    """
    生成不同质量图片
    :param filePath:
    :param ration: 1-9 代表图片质量
    :return:
    """
    img = Image.open(filePath)
    filename, ext = os.path.basename(filePath).split('.')
    filename += '_%s.' % ration + ext
    size = (int(img.size[0] / (7 - ration * .5)), int(img.size[1] / (7 - ration * .5)))
    img.thumbnail(size)
    thumb_dir = os.path.join(basedir, "static", 'thumb')
    if not os.path.exists(thumb_dir):
        os.makedirs(thumb_dir)
    img.save(os.path.join(thumb_dir, filename))


