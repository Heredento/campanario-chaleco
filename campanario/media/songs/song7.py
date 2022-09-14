import time as t
from utilities.appfunctions import play, C, D, E, F, G, A, B, C_, utilidad, finalizar
import utilities.appfunctions as appfunctions
appfunctions.tempo = 100
title="Salve Don Bosco Santo"


def appsong():

    try:
        utilidad()
        start_time = t.time()
        #compas0
        play(1, 3, A)
        play(1, 3, E)
        play(1, 4, E)
        play(1, 4, C)
        play(1, 4, E)
        play(1, 4, A)
        #compas1
        play(1, 1, B)
        play(1, 2, A)
        play(0, 3)
        #compas2
        play(1, 3, C_)
        play(1, 4, B)
        play(1, 4, A)
        play(1, 4, B)
        play(1, 3, A)
        play(0, 4)
        #compas4
        play(1, 2, G)
        play(0, 2)
        #compas5
        play(1, 3, A)
        play(1, 3, E)
        play(1, 4, E)
        play(1, 4, C)
        play(1, 4, E)
        play(1, 4, A)
        #compas6
        play(1, 3, B)
        play(1, 2, A)
        play(0, 3)
        #compas7
        play(1, 3, C_)
        play(1, 4, B)
        play(1, 4, A)
        play(1, 4, B)
        play(1, 3, A)
        play(0, 4)
        #compas8
        play(1, 2, D, G, C_)
        play(0, 2)



    except ValueError as ex:
        print(ex)
            
    except KeyboardInterrupt:
        print("Interrupción abrupta por teclado")

    finally:
        finalizar(t.time(), start_time)
        
if __name__ == '__main__':
    appsong()
