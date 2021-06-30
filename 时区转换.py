from datetime import datetime, timezone
from pytz import timezone

def utc_2_pk(utctime_str: str) -> datetime:
    '''UTC时间字符串转化为北京时间的datetime对象
    :参数 utctime_str:UTC时间字符串，格式为y-m-d H:M:S
    '''
    # 构造出没有时区的datetime对象
    naive_time = datetime.strptime(utctime_str, '%Y-%m-%d %H:%M:%S')
    # 取出上述对象的年月日小时构造一个时区为utc的datetime对象
    utctime = datetime(naive_time.year, naive_time.month, naive_time.day, naive_time.hour, naive_time.minute,
                       naive_time.second, tzinfo=timezone('UTC'))
    # 把时区为utc的对象转化为时区为Asia/Shanghai的datetime对象
    pktime = utctime.astimezone(timezone('Asia/Shanghai'))
    return pktime


def pk_2_utc(pktime_str: str) -> datetime:
    '''北京时间字符串转化为UTC时间的datetime对象
    :参数 pktime_str:北京时间字符串，格式为y-m-d H:M:S
    '''
    # 构造出没有时区的datetime对象
    naive_time = datetime.strptime(pktime_str, '%Y-%m-%d %H:%M:%S')
    # 将上述对象转化为时区为Asia/Shanghai的datetime对象
    pktime = naive_time.astimezone(timezone('Asia/Shanghai'))
    # 将时区为上海的datetime对象转化为时区为utc的时间对象
    utctime = pktime.astimezone(timezone('UTC'))
    return utctime

now_time = datetime.now()

utc_time = pk_2_utc(now_time.strftime("%Y-%m-%d %H:%M:%S"))
print('utc_time', utc_time.strftime("%Y-%m-%d %H:%M:%S"))

now_time = utc_2_pk(utc_time.strftime(("%Y-%m-%d %H:%M:%S")))
print('now_time', now_time.strftime("%Y-%m-%d %H:%M:%S"))

