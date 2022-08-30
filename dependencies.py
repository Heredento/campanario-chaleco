import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)


class internalGPIO:
    add, delete= 36, 38
    reload, lights = 40, 38
    music = [8, 10, 12, 16, 18, 22, 24, 26]
    clock = [add, lights]

class internalClock:
    tiempo_rotacion = 1.5
    estado_activo = round(tiempo_rotacion * 0.8, 3)
    estado_apagado = round(tiempo_rotacion *  0.2, 3)
    high_state = round(7/8, 3)
    low_state = round(1/8, 3)



