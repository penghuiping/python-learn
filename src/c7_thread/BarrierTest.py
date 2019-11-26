# encoding=utf8

import threading

i = 0

barrier = threading.Barrier(parties=2, action=lambda: (
    print(i)
))


def add():
    global i
    i = i + 1
    barrier.wait()


for i in range(2):
    t = threading.Thread(target=add)
    t.start()
