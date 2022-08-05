# Configuración
import RPi.GPIO as GPIO
import time 
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BOARD)


pines = [8, 10, 12, 16, 18, 22, 24, 26]

tempo = 90
tps = tempo/60

C = pines[0]
D = pines[1]
E = pines[2]
F = pines[3]
G = pines[4]
A = pines[5]
B = pines[6]
C_ = pines[7]

sc = tps*(1/4)
redon = tps*4
conteo=range(len(pines))

#constantes y funciones extra

for i in conteo:
        GPIO.setup(pines[i], GPIO.OUT)

def allLow(x):
    for i in conteo:
        GPIO.output(pines[i], False)
    time.sleep(x)
    

def t(x): # Modo de nota
    time.sleep((6/7)*x)
    allLow((1/7)*x)

def s(x): # Modo de silencio
    print(f"Silencio: {x}")
    time.sleep(x)

## "Partitura en código"
try:
    for y in range(3):
        allLow(1)
        print("Iniciando")

        GPIO.output(A,True)
        print("LA")
        t(sc)
        GPIO.output(G,True)
        print("SOL")
        t(sc)
        GPIO.output(D,True)
        print("RE")
        t(sc)
        GPIO.output(E,True)
        print("MI")
        GPIO.output(C,True)
        print("DO+")
        t(redon)

    time.sleep(3)
    GPIO.cleanup()



finally:
    GPIO.cleanup()
