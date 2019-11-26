# encoding=utf-8

# 单个数码管 从数字0显示到数字9 每个1秒加1
import gpiozero
import time
from signal import pause

h = gpiozero.LEDBoard(5, 6, 13, 19, 26, 16, 20, 21)


def printToDevice(value):
    table = {
        0: (0, 0, 0, 0, 0, 0, 1, 1),
        1: (1, 0, 0, 1, 1, 1, 1, 1),
        2: (0, 0, 1, 0, 0, 1, 0, 1),
        3: (0, 0, 0, 0, 1, 1, 0, 1),
        4: (1, 0, 0, 1, 1, 0, 0, 1),
        5: (0, 1, 0, 0, 1, 0, 0, 1),
        6: (0, 1, 0, 0, 0, 0, 0, 1),
        7: (0, 0, 0, 1, 1, 1, 1, 1),
        8: (0, 0, 0, 0, 0, 0, 0, 1),
        9: (0, 0, 0, 0, 1, 0, 0, 1)
    }
    h.value = table[value]


for i in range(10):
    printToDevice(i)
    time.sleep(1)
