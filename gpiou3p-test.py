import gpiou3p as gpio
import time

def blink():
    while(True):
        gpio.write(1, gpio.PIN.GPIO199)
        time.sleep(1)
        gpio.write(0, gpio.PIN.GPIO199)
        time.sleep(1)

gpio.setup(gpio.PIN.GPIO199, gpio.DIRECTION.OUT)
blink()
