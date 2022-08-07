import RPi.GPIO as GPIO
import time 
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BOARD)
GPIO.setup (11,GPIO.OUT)

def tiempo_musical(t):
    # Duración de nota pulsada para evitar silencios inexistentes
    GPIO.output(11, True)
    time.sleep((7/4)*t)
    GPIO.output(11, False)
    time.sleep((1/4)*t)



class nm: #notas musicales
    def C(seleccion):

    
        


    



    
try:
    while(True):
        

finally:
    GPIO.cleanup()

# while True:
#     GPIO.output(11,True)
#     time.sleep(2)
#     print("Encendido!")
#     GPIO.output(11,False)
#     time.sleep(2) 
#     print("Apagado!")
