import time as t
from utilities.appfunctions import play, C, D, E, F, G, A, B, C_, utilidad, finalizar
import utilities.appfunctions as appfunctions
appfunctions.tempo = 120

### Ingresar el tempo de la canción, recomendamos [40-80]
appfunctions.tempo = 180

### Dentro de las comillas ingresa el título de la canción
title="Seppette of the Dead Princess - ZUN"
def appsong():
    try:
        start_time = t.time()
        utilidad()

        ### Ingresa las notas a reproducir después de este comentario
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


        
        ### Aquí termina el espacio para escribir canciones
    except ValueError as ex:
        print(ex)

    except KeyboardInterrupt:
        print("Interrupción abrupta por teclado")

    finally:
        finalizar(t.time(), start_time)

if __name__ == '__main__':
    appsong()

