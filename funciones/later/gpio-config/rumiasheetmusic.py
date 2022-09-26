import time
import RPi.GPIO as GPIO
from gpiofunc import play, C, D, E, F, G, A, B, C_, utilidad, interrupcion, tempo
# from gpiofunc import tempo
import gpiofunc
# gpiofunc.tempo = 80
tempo = 120

def rumiasheetmusic():
    try:
        utilidad()    
        print("Reproduciendo: 'Aparitions Stalk in the night' de ZUN")
        time.sleep(3)
        #compas intro
        play(1, 4, E)
        play(1, 4, G)
        # compas 1
        play(1, 4, A)
        play(1, 4, C_)
        play(1, 5, B)
        play(1, 5, A)
        play(1, 4, G)
        play(1, 3, A)
        play(1, 4, E)
        play(1, 4, G)
        #compas2
        play(1, 4, A)
        play(1, 4, C_)
        play(1, 5, B)
        play(1, 5, A)
        play(1, 4, G)
        play(1, 3, A)
        play(1, 5, D)
        play(1, 4, E)
        play(1, 5, G)
        #compas3
        play(1, 2, A, C)
        play(0, 5) # revisar
        play(1, 5, C_)
        play(1, 5, B)
        play(1, 5, F)
        #compas4
        play(1, 4, G)
        play(1, 4, D)
        play(1, 4, F)
        play(1, 4, C)
        play(1, 4, A)
        play(1, 4, E)
        play(1, 5, F)
        play(1, 4, E)
        play(1, 5, C)
        #compas5
        play(1, 4, A)
        play(1, 4, C_)
        play(1, 5, B)
        play(1, 5, A)
        play(1, 3, G)
        play(1, 3, A)
        play(1, 4, E)
        play(1, 4, G)
        #compas6
        play(1, 4, A)
        play(1, 4, C_)
        play(1, 5, B)
        play(1, 5, A)
        play(1, 4, G)
        play(1, 3, A)
        play(1, 5, D)
        play(1, 4, E)
        play(1, 5, G)
        #compas7
        play(1, 2, A, C_)
        play(0, 5, A) # revisar
        play(1, 5, B)
        play(1, 5, A)
        play(1, 5, E)
        #compas8
        play(1, 3, A)
        play(1, 3, C)
        play(1, 3, F)
        play(1, 3, D)
        play(1, 3, G)
        play(1, 3, C)
        play(1, 5, E)
        play(1, 5, D)
        play(1, 5, E)
        play(1, 5, F)
        #compas9
        play(1, 3, A)
        play(1, 3, C_)
        play(1, 5, B)
        play(1, 5, A)
        play(1, 4, G)
        play(1, 3, A)
        play(1, 4, F)
        play(1, 4, A)
        #compas10
        play(1, 4, G)
        play(1, 4, B)
        play(1, 5, A)
        play(1, 5, G)
        play(1, 4, F)
        play(1, 3, G)
        play(1, 5, F)
        play(1, 4, G)
        play(1, 5, B)
        #compas11
        play(1, 2, C_, C)
        play(0, 5)
        play(1, 5, C_)
        play(1, 5, B)
        play(1, 5, F)
        #compas12
        play(1, 4, C_)
        play(1, 4, G)
        play(1, 4, B)
        play(1, 4, F)
        play(1, 4, A)
        play(1, 4, F)
        play(1, 5, G)
        play(1, 4, E)
        play(1, 5, C)
        #compas13
        play(1, 4, A)
        play(1, 4, C_)
        play(1, 5, B)
        play(1, 5, A)
        play(1, 4, G)
        play(1, 3, A)
        play(1, 4, E)
        play(1, 4, G)
        #compas14
        play(1, 4, A)
        play(1, 4, C_)
        play(1, 5, B)
        play(1, 5, A)
        play(1, 4, G)
        play(1, 3, A)
        play(1, 5, D)
        play(1, 4, E)
        play(1, 5, G)
        #compas15
        play(1, 2, E, A)
        play(0, 5)
        play(1, 5, A)
        play(1, 5, G)
        play(1, 5, D)
        #compas16
        play(1, 1, E, C_)


        time.sleep(0.1)
        for y in range(3,0,-1):
            print(f"Terminando en {y}")
            time.sleep(1)

        GPIO.cleanup()

    except KeyboardInterrupt:
        interrupcion()

rumiasheetmusic()