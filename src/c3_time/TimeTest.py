# coding=utf-8
import time
import datetime

print("当前时间戳:{}秒".format(time.time()))
print("格式化日期:{}".format(time.strftime("%Y-%m-%d %H:%M:%S")))

now = datetime.datetime.today()
print("完整日期与时间:{}".format(now.strftime("%Y-%m-%d %H:%M:%S")))
print("只有日期:{}".format(now.date()))
print("只有时间:{}".format(now.time()))
print("当前时间戳:{}秒".format(now.timestamp()))
