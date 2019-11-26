# coding=utf-8
# 简单的控制led灯开关
# led小灯 有2个引脚 一个长一个段，长的引脚接正电，短的引脚接地
import gpiozero
import time

led = gpiozero.LED(21)

for i in range(10):
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
