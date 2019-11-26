# encoding=utf-8

# 控制蜂鸣器发声,使用pwd方波输出
import gpiozero
import time
from signal import pause

buzzer = gpiozero.PWMOutputDevice(21)
buzzer.blink(on_time=0.1, off_time=0.1)
pause()
