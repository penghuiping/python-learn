# coding=utf-8
# 使用按钮控制led小灯的亮与灭
# 按钮有4个引脚
from gpiozero import Button
from gpiozero import LED
from signal import pause

led = LED(21)
button = Button(2)

button.when_pressed = led.on
button.when_released = led.off

pause()
