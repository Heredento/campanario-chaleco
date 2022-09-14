import time as t
from utilities.appfunctions import play, C, D, E, F, G, A, B, C_, utilidad, finalizar
import utilities.appfunctions as appfunctions
appfunctions.tempo = 100
title="Shanghai Alice of Meiji - ZUN"


def appsong():

    try:
        utilidad()
        start_time = t.time()
        #compas0
        play(1, 3, C, A)
        play(0, 4)
        play(1, 4, G)
        play(1, 3, E)
        play(0, 4)
        play(1, 4, A)
        play(0, 5)
        play(1, 4, G)
        #compas1
        play(1, 4, E)
        play(1, 4, C)
        play(1, 4, E)
        play(0, 5)
        play(1, 2, C, C_)
        play(0, 5)
        #compas2
        play(1, 3, C, A)
        play(0, 5)
        play(1, 4, F)
        play(1, 4, E)
        play(0, 5)
        play(1, 4, F)
        play(0, 5)
        play(1, 4, G)
        #compas3
        play(1, 1, C, E)
        #compas4
        play(1, 3, C)
        play(0, 4)
        play(1, 4, F)
        play(1, 4, E)
        play(0, 5)
        play(1, 4, F)
        play(0, 5)
        play(1, 4, G)
        #compas5
        play(1, 3, A)
        play(1, 3, G)
        play(1, 3, A)
        play(1, 3, A)
        #compas6
        play(1, 4, E, A)
        play(1, 3, F)
        play(1, 5, G)
        play(1, 5, A)
        play(1, 4, G)
        play(0, 5)
        play(1, 4, E)
        play(0, 5)
        play(1, 4, C)
        #compas7
        play(1, 4, E)
        play(1, 4, C)
        play(1, 4, E)
        play(0, 5)
        play(1, 3, F, C_)
        play(0, 5)
        play(0, 3)
        
    except ValueError as ex:
        print(ex)
            
    except KeyboardInterrupt:
        print("Interrupción abrupta por teclado")

    finally:
        finalizar(t.time(), start_time)
        
if __name__ == '__main__':
    appsong()
