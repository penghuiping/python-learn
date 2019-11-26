# coding=utf-8

import threading

i = 0


def run():
    global i  # 定义成全局变量
    i = i + 1


for i in range(3):
    t = threading.Thread(target=run)
    t.start()
    t.join()

print(i)
