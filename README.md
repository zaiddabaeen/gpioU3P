###GPIO U3+
####Developed by: Zaid Daba'een

A simple python library to control the three GPIO pins on the Odroid U3+.

Clone the library using:
```
git clone https://github.com/zaiddabaeeen/gpiou3p
```

###Usage

1. Simply import the library

   ```python
   import gpiou3p as gpio
   ```

2. Setup the pin directions

   ```python
   gpio.setup(gpio.PIN.GPIO199, gpio.DIRECTION.OUT)
   ```

3. Write to the pin

   ```python
   gpio.write(1, gpio.PIN.GPIO199)
   ```

Check `gpiou3p-test.py` file for a test case that blinks an LED.

>You need sudo previliges to be able to edit the GPIO pins on the Odroid U3+