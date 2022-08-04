import RPi.GPIO as GPIO
import time 
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BOARD)
GPIO.setup (11,GPIO.OUT)
while True:
    GPIO.output(11,True)
    time.sleep(2)
    print("Encendido!")
    GPIO.output(11,False)
    time.sleep(2) 
    print("Apagado!")
