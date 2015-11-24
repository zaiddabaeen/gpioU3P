import os

if os.getuid() != 0:
    print "Must have superuser privileges for gpiou3p"
    exit(1)

# --------------------------------------------------------------------------------

def setup(pin, direction):
    os.system("echo " + pin + " > /sys/class/gpio/export")
    os.system("echo " + direction + " > /sys/class/gpio/gpio" + pin + "/direction")

def write(data, pin):
    os.system("echo " + str(data) + " > /sys/class/gpio/gpio" + pin + "/value")

class PIN:
    GPIO199 = "199"
    GPIO200 = "200"
    GPIO204 = "204"

class DIRECTION:
    OUT = "out"
    IN = "in"