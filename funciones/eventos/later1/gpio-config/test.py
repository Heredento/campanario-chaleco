import time
import RPi.GPIO as GPIO
from gpiofunc import play, C, D, E, F, G, A, B, C_, utilidad, interrupcion
import gpiofunc
gpiofunc.tempo=60
rango=20


try:
     utilidad()
     print("Reproduciendo: 'Aparitions Stalk in the night' de ZUN")
     time.sleep(3)
     #compas intro
     play(1, 4, C)

