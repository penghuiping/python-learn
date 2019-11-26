# coding=utf-8

import concurrent.futures.thread as cft
import threading


class CountDown:
    i = 0
    xLock = threading.Lock()
    zeroCondition = threading.Condition(lock=xLock)

    def __init__(self, counts):
        self.i = counts

    def count_down(self):
        try:
            self.xLock.acquire()
            self.i = self.i - 1
            if self.i <= 0:
                # 减一以后到达0
                self.zeroCondition.notifyAll()
        finally:
            self.xLock.release()
        pass

    def wait(self):
        while True:
            try:
                self.xLock.acquire()
                if self.i > 0:
                    self.zeroCondition.wait()
                else:
                    break
            finally:
                self.xLock.release()
        pass


cd = CountDown(10000)


class Counter:
    i = 0


lock = threading.Lock()


def add():
    try:
        lock.acquire()
        Counter.i = Counter.i + 1
    finally:
        lock.release()
        cd.count_down()


pool = cft.ThreadPoolExecutor(max_workers=20, thread_name_prefix='test-executor')

for f in range(10000):
    pool.submit(add)

cd.wait()

print(Counter.i)
