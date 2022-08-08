Pinouts
https://pinout.xyz/

# Instrucciones para crear una partitura
1. Crear un archivo nombredepartitura.py en el directorio ../gpio-config
2. Antes de empezar pegar las siguientes líneas de código

        import time
        import RPi.GPIO as GPIO
        from gpiofunc import play, C, D, E, F, G, A, B, C_, utilidad, interrupcion
        import gpiofunc
        gpiofunc.tempo=90


En la línea de código ``gpiofunc.tempo=90`` podemos remplazar 90 por el tempo(BPM) de la partitura real que deseamos crear.

Notas aclaratorias:
- El campanario sólo puede tocar una octava musical sin notas intermedias, es decir las notas, ``DO, RE, MI, FA, SOL, LA, SI y DO`` de segunda escala.

[IMPORTANTE] 
No se pueden usar notas medias, es decir sostenidas o bemoles, sólo las naturales. (Escala de DO Mayor)
No se pueden tocar notas consecutivas en tiempos diferentes.
Sólo se pueden tocar múltiples notas si tienen el mismo tiempo.

Ejemplo:
<img src="https://github.com/Heredento/sys-de-campanario/blob/main/static/img/ejemplo-partitura.png?raw=true" width="500">
  


# Sistema de campanario automatizado
El objetivo principal:
    Desarrollar un sistema que permita automatizar el sistema horario del reloj cuando sucedan incovenientes que vuelven los cambios de horas inevitables; El reloj se retrasa o adelanta tiempo y deseamos que vuelva a la hora normal sin tener que hacerlo manualmente.

El objetivo secundario es desarrollar una página web que permita agendar eventos y seleccionar partituras-scripts reproducibles en el campanario.

Metas:
    1. Reproducir melodías personalizadas en el campanario en horas agendadas.
    2. Desarrollar un control manual mediante la página web sin necesidad de tocar el hardware.
    3. Crear una librería para el desarrollo de partituras implementables al campanario mediante scripts.

## Instalación
Instalar los paquetes requeridos dentro consola:

1. RPi.GPIO: exclusivo para el control de pines en Raspberry. NO INSTALAR EN OTROS DISPOSITIVOS EXCEPTO RASPBERRY      

        pip install RPi.GPIO

2. Flask: paquete para desarrollo web   

        pip install Flask

3. schedule: facilita agendar eventos 

        pip install schedule 
    
4. psycopg2: base de datos PostgreSQL implementada localmente para guardar events agendados

        pip install psycopg2
        sudo apt install postgresql-13


## Disclaimer

    El codigo se mantiene en producción y muchas plantillas de apoyo pueden ser encontradas.
    Actuamente en desarrollo.
    Usuario en aprendizaje!
    No sé cómo usar Github apropiadamente.