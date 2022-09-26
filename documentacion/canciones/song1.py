import time as t
from utilities.appfunctions import play, C, D, E, F, G, A, B, C_, utilidad, finalizar
import utilities.appfunctions as appfunctions
appfunctions.tempo = 120

title="Aparitions Stalk in the night - ZUN"
def appsong():
    try:
        utilidad()
        start_time = t.time()
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

        

    except ValueError as ex:
        print(ex)
            
    except KeyboardInterrupt:
        print("Interrupción abrupta por teclado")

    finally:
        finalizar(t.time(), start_time)

if __name__ == '__main__':
    appsong()
