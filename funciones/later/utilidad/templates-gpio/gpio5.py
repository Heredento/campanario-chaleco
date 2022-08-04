import RPi.GPIO as GPIO
import time 
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BOARD)
GPIO.setup (11,GPIO.OUT)

def loop(t):
    GPIO.output(11,True)
    print(f"Encendido! t: {t}")
    time.sleep(t)
    
    GPIO.output(11,False)
    print(f"Apagado! t: {t}")
    time.sleep(t) 
    

def mHzClock(bpm, seleccion):
    bcs=60/bpm
    if (seleccion==1):
        t=bcs*4
        loop(t)

    elif (seleccion==2):
        t=bcs*2
        loop(t)

    elif (seleccion==3):
        t=bcs*1
        loop(t)

    elif (seleccion==4):
        t=bcs*(1/2)
        loop(t)

    elif (seleccion==5):
        t=bcs*(1/4)
        loop(t)

    elif (seleccion==0):
        print("Seleccion: 0")

    
try:
    while(True):
        mHzClock(120, 5)

except:
    mHzClock(60, 2)

finally:
    GPIO.cleanup()

# while True:
#     GPIO.output(11,True)
#     time.sleep(2)
#     print("Encendido!")
#     GPIO.output(11,False)
#     time.sleep(2) 
#     print("Apagado!")
