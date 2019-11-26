# coding=utf-8

import re

# 字符串拼接
a = "hello" + "," + "world"

print("字符串拼接:", a)
print("字符串大写", a.upper())
print("字符串小写", a.lower())
print("字符串截取", a[0:5])
print("判断字符串是以特定格式开始", a.startswith("hello"))
print("判断字符串是否包含特定字符串", "hello" in a)

# trim
a = " hello "
print(a.strip())

# 使用正则表达式抓取固定电话
b = "我家的固定电话为021-12345678，不是18812345678，这个是手机号。我姐家固定电话为021-33333333"
print(re.findall("[0-9]+-[0-9]+", b, re.M))

# str转成int
print(int('12'))

# int转成str
print(str(12))

# str format
a = "这个错误是:{}".format("空指针错误")
print(a)

# 字符串转bytes
a = "hello world"
bytess = bytes(a, encoding="utf-8")
print("字节数组为:{}".format(bytess))

# bytes转字符串
str = str(bytess, encoding="utf-8")
print("字符串为:{}".format(str))
