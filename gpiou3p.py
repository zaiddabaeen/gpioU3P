import os

if os.getuid() != 0:
    print "Must have superuser privileges for gpiou3p"
    exit(1)
    
# --------------------------------------------------------------------------------

def setup(pin, direction):
    export_file = open("/sys/class/gpio/export", "w")
    export_file.write(pin)
    export_file.close()
    direction_file = open("/sys/class/gpio/" + pin + "/direction", "w")
    direction_file.write(direction)
    direction_file.close()

def write(data, pin):
    pin_file = open("/sys/class/gpio/" + pin + "/value", "w")
    pin_file.write(data)
    pin_file.close()

class PIN:
    GPIO199 = "gpio199"
    GPIO200 = "gpio200"
    GPIO204 = "gpio204"

class DIRECTION:
    OUT = "out"
    IN = "in"