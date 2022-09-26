import time as t
from utilities.appfunctions import play, C, D, E, F, G, A, B, C_, utilidad, finalizar
import utilities.appfunctions as appfunctions
appfunctions.tempo = 120
title="We Wish You a Merry Christmas"


def appsong():

    try:
        utilidad()
        start_time = t.time()
        #compas0
        play(1, 3, D)
        play(1, 3, G)
        play(1, 4, G)
        play(1, 4, A)
        play(1, 4, G)
        play(1, 4, F)
        #compas1
        play(1, 3, E)
        play(1, 3, E)
        play(1, 3, E)
        play(1, 3, A)
        #compas2
        play(1, 4, A)
        play(1, 4, B)
        play(1, 4, A)
        play(1, 4, G)
        play(1, 3, F)
        play(1, 3, D)
        #compas3
        play(1, 3, D)
        play(1, 3, G)
        play(1, 4, B)
        play(1, 4, C_)
        play(1, 4, B)
        play(1, 4, A)
        #compas4
        play(1, 3, G)
        play(1, 3, E)
        play(1, 3, D)
        play(1, 3, E)
        #compas5
        play(1, 3, A)
        play(1, 3, F)
        play(1, 2, G)
        #compas6
        play(1, 3, D)
        play(1, 3, G)
        play(1, 4, G)
        play(1, 4, A)
        play(1, 4, G)
        play(1, 4, F)
        #compas7
        play(1, 3, E)
        play(1, 3, E)
        play(1, 3, E)
        play(1, 3, A)
        #compas8
        play(1, 4, A)
        play(1, 4, B)
        play(1, 4, A)
        play(1, 4, G)
        play(1, 3, F)
        play(1, 3, D)
        #compas9
        play(1, 3, D)
        play(1, 3, B)
        play(1, 4, B)
        play(1, 4, C_)
        play(1, 4, B)
        play(1, 4, A)
        #compas10
        play(1, 3, G)
        play(1, 3, E)
        play(1, 3, D)
        play(1, 3, E)
        #compas11
        play(1, 3, A)
        play(1, 3, F)
        play(1, 2, G)
        #compas12
        play(1, 3, D)
        play(1, 3, G)
        play(1, 4, G)
        play(1, 4, A)
        play(1, 4, G)
        play(1, 4, F)
        #compas13
        play(1, 4, A)
        play(1, 4, B)
        play(1, 4, A)
        play(1, 4, G)
        play(1, 3, F)
        play(1, 3, D)
        #compas14
        play(1, 3, D)
        play(1, 3, B)
        play(1, 4, B)
        play(1, 4, C_)
        play(1, 4, B)
        play(1, 4, A)
        #compas15
        play(1, 3, G)
        play(1, 3, E)
        play(1, 3, D)
        play(1, 3, E)
        #compas16
        play(1, 3, A)
        play(1, 3, F)
        play(1, 3, E)
        play(0, 3)
        
        
        
    except ValueError as ex:
        print(ex)
            
    except KeyboardInterrupt:
        print("Interrupción abrupta por teclado")

    finally:
        finalizar(t.time(), start_time)
        
if __name__ == '__main__':
    appsong()
