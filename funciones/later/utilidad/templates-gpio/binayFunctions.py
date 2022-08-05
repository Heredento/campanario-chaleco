
#import GPIO library
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
A = 16
B = 18
C = 22
D = 24

binaryPins = [D, C, B, A]
bP = binaryPins


class t:
    def bpm(x):
        bps = x / 60
        return bps

        def redonda():
            time.sleep(bps)

        def blanca():
            time.sleep(bps/2)

        def negra():
            time.sleep(bps/4)

        def corchea():
            time.sleep(bps/16)

        def semicorchea():
            time.sleep(bps/32)

        def fusa():
            time.sleep(bps/64)

        def semifusa():
            time.sleep(bps/128)



def all_low():
    for i in binaryPins:
        GPIO.output(bP[i], GPIO.HIGH)
        print("Pines apagados")

def C(): #Nota Do
    GPIO.output(bP[0], GPIO.HIGH)

def D(): #Nota Re
    GPIO.output(bP[1], GPIO.HIGH)

def E():  #Nota Mi
    GPIO.output(bP[0], GPIO.HIGH)
    GPIO.output(bP[1], GPIO.HIGH)

def F():  #Nota Fa
    GPIO.output(bP[2], GPIO.HIGH)

def G():  #Nota Sol
    GPIO.output(bP[2], GPIO.HIGH)
    GPIO.output(bP[0], GPIO.HIGH)

def A():  #Nota La
    GPIO.output(bP[2], GPIO.HIGH)
    GPIO.output(bP[1], GPIO.HIGH)

def B():  #Nota Si
    GPIO.output(bP[2], GPIO.HIGH)
    GPIO.output(bP[1], GPIO.HIGH)
    GPIO.output(bP[0], GPIO.HIGH)

def C2():  #Nota Do de segunda escala
    GPIO.output(bP[3], GPIO.HIGH)





