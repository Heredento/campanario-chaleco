#import GPIO library
import RPi.GPIO as GPIO
#import time

GPIO.setwarnings(False)

#set GPIO numbering mode and define inputs
rp = 10 #reading pin
wp = 12 #working pin


GPIO.setmode(GPIO.BOARD)
GPIO.setup(wp, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(rp, GPIO.IN)

try:

    while (True):
        if GPIO.input(rp)==0:
            print("Circuito abierto!")
        else:
            print("Circuito Cerrado")
            GPIO.output(wp)

finally: #Presionando CTRL + C reproduce esta acción
    GPIO.cleanup()