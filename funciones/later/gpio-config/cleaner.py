import RPi.GPIO as GPIO
import time 
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BOARD)

pines = [8, 10, 12, 16, 18, 22, 24, 26]
conteo=range(len(pines))
for i in conteo: # funcion confifura como salida los pines en la lista 
        GPIO.setup(pines[i], GPIO.OUT)

def allLow(x): # 0 Logico en todos los pines de salida de notas
    for i in conteo:
        GPIO.output(pines[i], False)
    time.sleep(x)

def cleaner():
    try:
        for y in range(5, 0, -1):
            print(f"Limpiando en {y}")
            time.sleep(1)
        allLow(1)
        GPIO.cleanup()

    except KeyboardInterrupt:
        print("Sesión interrumpida")
    # finally:
    #     print("test")
    #     GPIO.cleanup()

cleaner()