
from random import randint
from machine import Pin
from utime import sleep
led = Pin(25, Pin.OUT)

def throw_dice(num_dice=2):
    total = 0
    for x in range(1, num_dice+1):
        total += randint(1, 6)
        print ("TOTAL",total)
    return total

def blink(times,delay):
    for x in range(1,times+1):
        led.on()
        sleep(delay)
        led.off()
        sleep(delay)
while True:
    input("Press enter")    #Wait for input before pressing enter
    dice_throw = throw_dice()
    print(dice_throw)
    blink(dice_throw, 0.2)
    sleep(3)
          