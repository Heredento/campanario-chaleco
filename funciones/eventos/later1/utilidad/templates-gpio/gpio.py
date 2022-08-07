#import GPIO library
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#set GPIO numbering mode and define inputs
wp = 18 #working pin
rp = 16 #reading pin

GPIO.setmode(GPIO.BOARD)
GPIO.setup(wp, IN)
GPIO.setup(rp, IN)


try:
    while (GPIO.input(rp)==1):
        if GPIO.input(wp)==0:
            print("Circuito abierto!")
        else:
            print("Circuito Cerrado")

finally: #Presionando CTRL + C reproduce esta acción
    GPIO.cleanup()

