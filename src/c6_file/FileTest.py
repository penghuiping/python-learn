# coding=utf-8
import io
import shutil
import os

# 文件写入 with...as 类似于java7中 try...with resources
with io.open("./tmp.txt", mode='x+') as f:
    f.writelines("hello world1\n")
    f.writelines("hello world2\n")
    f.writelines("hello world3\n")

# 文件读取
f = ""
try:
    f = io.open("./tmp.txt", mode='r+')
    for line in f.readlines():
        print(line)
finally:
    f.close()

# 文件copy
shutil.copy('./tmp.txt', './tmp1.txt')

# 获取文件属性
print("======获取文件属性======")
print(os.stat("./tmp1.txt"))
print(os.getcwd())

# 删除文件
os.remove("./tmp.txt")
os.remove("./tmp1.txt")
