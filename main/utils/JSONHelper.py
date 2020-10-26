
def jsonBQlist(bqlist):
    result=[]
    for item in bqlist:
        jsondata={}
        for i in range(item.__len__()):

            tdic={item._fields[i]:item[i]}
            jsondata.update(tdic)
        result.append(jsondata)
    return result
def dictToObj(results, to_class):
    """将字典list或者字典转化为指定类的对象list或指定类的对象
    python 支持动态给对象添加属性，所以字典中存在而该类不存在的会直接添加到对应对象
    """
    if isinstance(results, list):
        objL = []
        for result in results:
            obj = to_class()
            for r in result.keys():
                obj.__setattr__(r, result[r])
            objL.append(obj)
        return objL
    elif isinstance(results, dict):
        obj = to_class()
        for r in results.keys():
            obj.__setattr__(r, results[r])
        return obj
    else:
        print("传入对象非字典或者list")
        return None


def copyObj(src_class, dst_class):
    """将字典list或者字典转化为指定类的对象list或指定类的对象
    python 支持动态给对象添加属性，所以字典中存在而该类不存在的会直接添加到对应对象
    """
    for key, value in src_class.__dict__.items():

        if isinstance(value, str):
            print(value)
            setattr(dst_class, key, value)
    return dst_class


def modifyObj(src_class, dst_class):
    """将字典list或者字典转化为指定类的对象list或指定类的对象
    python 支持动态给对象添加属性，所以字典中存在而该类不存在的会直接添加到对应对象
    """
    for key, value in src_class.__dict__.items():
        if key == "_sa_instance_state":
            continue
        if (key, value) not in dst_class.__dict__.items():
            print(dst_class)
            setattr(dst_class, key, value)
    return dst_class


def modifyDictToObj(src_dict, dst_class):
    """将字典复制到对象
    """
    for key, value in dst_class.__dict__.items():
        if key == "_sa_instance_state":
            continue
        if key in src_dict:
            setattr(dst_class, key, src_dict[key])
    return dst_class