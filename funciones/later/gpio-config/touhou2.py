import time
import RPi.GPIO as GPIO
from funciones import play, C, D, E, F, G, A, B, C_, utilidad, interrupcion, limpieza, finalizar
import funciones
# funciones.tempo = 120
funciones.tempo = 80
title="Seppette of the Dead Princess - ZUN"
# print(f"tempo: {funciones.tempo} ")
try:
    limpieza()
    #compas0
    play(0, 4)
    play(1, 4, D)
    play(1, 4, F)
    play(1, 4, G)
    #compas1
    play(1, 3, A)
    play(0, 4)
    play(1, 4, B)
    play(1, 3, G)
    play(0, 4)
    play(1, 4, A)
    #compas2
    play(1, 2, F)
    play(0, 4)
    play(1, 4, C)
    play(1, 4, F)
    play(1, 4, G)
    #compas3
    play(1, 3, A)
    play(0, 4)
    play(1, 4, B)
    play(1, 3, G)
    play(0, 4)
    play(1, 4, C_)
    #compas4
    play(1, 2, A)
    play(0, 4)
    play(1, 4, E)
    play(1, 4, G)
    play(1, 4, B)
    #compas5
    play(1, 3, D)
    play(1, 3, D)
    play(0, 4)
    play(1, 4, G)
    play(1, 4, B)
    play(1, 4, C_)
    #compas6
    play(1, 3, D)
    play(1, 3, D)
    play(0, 4)
    play(1, 4, A)
    play(1, 4, A)
    play(1, 4, B)
    #compas7
    play(1, 3, A)
    play(0, 4)
    play(1, 4, C_)
    play(1, 3, A)
    play(0, 4)
    play(1, 4, G)
    #compas8 tercera línea


    finalizar()

except KeyboardInterrupt:
    interrupcion()