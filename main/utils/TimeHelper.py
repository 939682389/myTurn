import time
def datetime_toString_long(dt):
    return dt.strftime("%Y-%m-%d")


def datetime_toString_short(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def datetime_toString_time(dt):
    return dt.strftime("%H:%M:%S")


def is_same_day(dt1, dt2):
    return dt1.strftime("%Y-%m-%d") == dt2.strftime("%Y-%m-%d")


def timestamp_to_str(timestamp=None, format=None):
    if timestamp:
        time_tuple = time.localtime(timestamp)  # 把时间戳转换成时间元祖
        result = time.strftime(format, time_tuple)  # 把时间元祖转换成格式化好的时间
        return result
    else:
        return int(time.mktime(time.strptime(format, '%Y-%m-%d %H:%M:%S')))