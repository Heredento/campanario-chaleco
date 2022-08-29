import time as t
from utilities.appfunctions import play, C, D, E, F, G, A, B, C_, utilidad, finalizar
import utilities.appfunctions as appfunctions

### Ingresar el tempo de la canción, recomendamos entre 40-80
appfunctions.tempo = 120

### DENTRO de las comillas ingresa el título de la canción
title="Ingresa el título de la canción acá"
def appsong():
    try:
        start_time = t.time()
        utilidad()

        ### Ingresa las notas a reproducir después de este comentario

        ## Las siguientes cuatro líneas son ejemplos
        play(1, 3, C, G, A)
        play(1, 4, D)
        play(1, 4, F)
        play(1, 4, G)
        ### Borra las cautro lineas anteriores cuando ya escribas tus canciones


        ### Aquí termina el espacio para escribir canciones
    except ValueError as ex:
        print(ex)

    except KeyboardInterrupt:
        print("Interrupción abrupta por teclado")

    finally:
        finalizar(t.time(), start_time)

    
