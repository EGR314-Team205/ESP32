from machine import Pin   
from time import sleep    
led = Pin(2, Pin.OUT)     
while True:               
    led.value(led.value()^1) 
    sleep(0.25)