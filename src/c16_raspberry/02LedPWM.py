# coding=utf-8
# 使用PWM (pulse-width-modulation)控制led灯的亮度
import gpiozero
import time

led = gpiozero.PWMLED(21)

while True:
    led.value = 0
    for i in range(99):
        led.value = led.value + 0.01
        time.sleep(0.1)
