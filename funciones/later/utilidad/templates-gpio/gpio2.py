#import GPIO library
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#set GPIO numbering mode and define inputs
wp = 18 #working pin
rp = 16 #reading pin

#GPIO.setmode(GPIO.BOARD)
GPIO.setup(wp, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(rp, GPIO.IN)

for i in range(5):
    GPIO.output(18, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(18, GPIO.LOW)
    time.sleep(1)
    print(f"Secuencia: {int(i)+1}")

# try:
#
#     while (GPIO.input(rp)==1):
#         if GPIO.input(wp)==0:
#             print("Circuito abierto!")
#         else:
#             print("Circuito Cerrado")
#
# finally: #Presionando CTRL + C reproduce esta acción
#     GPIO.cleanup()

