# coding=utf-8

import concurrent.futures.thread as cft
import concurrent.futures


class Counter:
    value = 0

    def incr(self):
        self.value = self.value + 1


pool = cft.ThreadPoolExecutor(max_workers=20)

counter = Counter()


futures = []

for i in range(1000000):
    tmp = pool.submit(fn=lambda: (
        counter.incr(),
    ))
    futures.append(tmp)


concurrent.futures.wait(futures)

print(counter.value)