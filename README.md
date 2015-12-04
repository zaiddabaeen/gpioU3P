###GPIO U3+
####Developed by: Zaid Daba'een

A simple python library to control the three GPIO pins on the Odroid U3+.

Clone the library using:
```
git clone https://github.com/zaiddabaeeen/gpiou3p
```

###Usage

Simply import the library

    import gpiou3p as gpio


####Writing to the pin

1. Setup the pin directions

        gpio.setup(gpio.PIN.GPIO199, gpio.DIRECTION.OUT)
   

2. Write to the pin
 
        gpio.write(1, gpio.PIN.GPIO199)

####Reading the pin

1. Setup the pin directions

        gpio.setup(gpio.PIN.GPIO199, gpio.DIRECTION.IN)
   
2. Read the pin

        gpio.read(gpio.PIN.GPIO199)


Check `example.py` file for an example case that blinks an LED.

>You need sudo privileges to be able to edit the GPIO pins on the Odroid U3+

###More Information
Check out the blog post http://nasa.z-proj.com/accessing-gpio-pins-on-the-odroid-u3/ for more information on the GPIO pins and schematics.