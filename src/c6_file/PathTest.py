# coding=utf-8
import os
import io
import pathlib

pathlib.Path.open()

# 创建文件夹
print("======创建文件夹======")
rootPath = "./path"
if not os.path.exists(rootPath):
    os.mkdir(rootPath, mode=0o777)

if not os.path.exists(rootPath + "/folder1"):
    os.mkdir(rootPath + "/folder1", mode=0o777)

if not os.path.exists(rootPath + "/folder2"):
    os.mkdir(rootPath + "/folder2", mode=0o777)

if not os.path.exists(rootPath + "/folder2"):
    os.mkdir(rootPath + "/folder2", mode=0o777)

# 创建文件
print("======创建文件======")
if not os.path.exists(rootPath + "/1.txt"):
    f = io.open(rootPath + "/1.txt", mode="x+")
    f.close()

if not os.path.exists(rootPath + "/1.txt"):
    f = io.open(rootPath + "/1.txt", "x+")
    f.close()


# 打印目录结构
print("======打印目录结构======")
list = os.listdir(rootPath)
for i in list:
    print(i)

# 删除文件夹
print("======删除所有创建的文件与文件夹======")
list = os.listdir(rootPath)
for x in list:
    path = rootPath + "/" + x
    if os.path.isfile(path):
        os.remove(path)
    else:
        for y in os.listdir(path):
            if os.path.isfile(path + "/" + y):
                os.remove(path + "/" + y)
        os.rmdir(path)
os.rmdir(rootPath)
