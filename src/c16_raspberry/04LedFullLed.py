# encoding=utf-8

# 全彩led有4个引脚，1个长，三个短，长的那个引脚接高电平，短的引脚接负电平
import gpiozero
import time
from signal import pause

led12 = gpiozero.PWMLED(12)
led16 = gpiozero.PWMLED(16)  # red
led20 = gpiozero.PWMLED(20)  # green
led21 = gpiozero.PWMLED(21)  # blue


def RGB(red, green, blue):
    global led12, led16, led20, led21
    # red
    led12.value = 1
    led16.value = 1 - red
    led20.value = 1 - green
    led21.value = 1 - blue


while True:
    RGB(1, 0, 0)
    time.sleep(1)

    RGB(0, 1, 0)
    time.sleep(1)

    RGB(0, 0, 1)
    time.sleep(1)

    RGB(1, 1, 0)
    time.sleep(1)

    RGB(1, 0, 1)
    time.sleep(1)

    RGB(0, 1, 1)
    time.sleep(1)

    RGB(0.5, 0.5, 0.5)
    time.sleep(1)

# pause()
