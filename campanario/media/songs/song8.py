import time as t
from utilities.appfunctions import play, C, D, E, F, G, A, B, C_, utilidad, finalizar
import utilities.appfunctions as appfunctions
appfunctions.tempo = 120
title="Wesminster Chimes - Campanario clásico"


def appsong():

    try:
        utilidad()
        start_time = t.time()
        #compas0
        play(1, 3, B)
        play(1, 3, G)
        play(1, 3, A)
        #compas1
        play(1, 2, E)
        play(0, 3)
        #compas3
        play(1, 3, F)
        play(1, 3, G)
        play(1, 3, B)
        #compas4
        play(1, 2, E)
        play(0, 3)
        #compas5
        play(1, 3, A)
        play(1, 3, F)
        play(1, 3, G)
        #compas6
        play(1, 2, E)
        play(0, 3)
        #compas7
        play(1, 3, E)
        play(1, 3, F)
        play(1, 3, A)
        #compas8
        play(1, 2, E)
        play(0, 3)
        #compas9
        play(1, 3, F)
        play(1, 3, G)
        play(1, 2, C_) # transición compas10
        #compas10
        play(0, 3)
        play(1, 2, E, A) # transición compas11
        #compas11
        play(0, 3)
        play(1, 2, E) # transición compas12
        #compas12
        play(1, 2, E, C)
        play(0, 3)
        #compas13
        play(1, 1, E, C)
        play(0, 3)


    except ValueError as ex:
        print(ex)
            
    except KeyboardInterrupt:
        print("Interrupción abrupta por teclado")

    finally:
        finalizar(t.time(), start_time)
        
if __name__ == '__main__':
    appsong()
