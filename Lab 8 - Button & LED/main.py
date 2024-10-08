from machine import Pin
from time import sleep

LED = Pin("LED", Pin.OUT)

Button = Pin(16, Pin.IN, Pin.PULL_UP)

while True:
    sleep(0.5)
    if Button.value() == 0:
        LED.value(1)
    else:
        LED.value(0)
        