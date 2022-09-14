from PIL.Image import Resampling
import RPi.GPIO as GPIO, time as t, os, sys
GPIO.setmode(GPIO.BOARD)
sys.path.append(os.getcwd())
from dependencies import internalGPIO, internalClock
GPIO.setwarnings(False)
from datetime import datetime as dtime
from datetime import timedelta as tdelta
time_folder = os.path.join(os.getcwd(), 'funciones/', 'clocktime/')
hour_file = os.path.join(time_folder, 'hour.txt')
min_file = os.path.join(time_folder, 'minute.txt')

timefile = os.path.join(os.getcwd(), 'funciones/', 'clocktime/', 'time.txt')


GPIO.setup(internalGPIO.add, GPIO.OUT)
GPIO.setup(internalGPIO.lights, GPIO.OUT)

#Funcion para contar el tiempo de la funcion validacion de tiempo
def contar_tiempo_main(correr_funcion, *tiempo):
    st = t.time()
    hora_erronea, minuto_erroneo = tiempo
    correr_funcion(hora_erronea, minuto_erroneo)
    et = t.time()
    tiempo_ejecutado = round(et-st, 2)
    print(f"Tiempo de ejecucion: {tiempo_ejecutado}s | Main")
    return tiempo_ejecutado

#Funcion para contar el tiempo de la funcion retraso y adelanto
def contar_tiempo_minor(correr_funcion, retraso_adelanto):
    st = t.time()
    correr_funcion(retraso_adelanto)
    et = t.time()
    
    tiempo_ejecutado = round(et-st, 2)
    print(f"Tiempo de ejecucion: {tiempo_ejecutado}s | Minor")
    return tiempo_ejecutado


def tiempo_actual():
    now = dtime.now()
    hora_real = int(now.strftime('%I'))
    minuto_real = int(now.strftime('%M'))
    segundo_real = int(now.strftime('%S'))
    return hora_real, minuto_real, segundo_real

class Ahora:
    def info():
        hora_real, minuto_real, segundo_real = tiempo_actual()
        print(F'HORA REAL:{hora_real}:{minuto_real}:{segundo_real}')
        
    def hora():
        return tiempo_actual()[0]
    def minuto():
        return tiempo_actual()[1]
    def segundo():
        return tiempo_actual()[2]
    

def read_timefile():
    with open(min_file, 'r') as m:
        m.flush()
        minuto = int(m.read())
    m.close()
    with open(hour_file, 'r') as h:
        h.flush()
        hora = int(h.read())
    h.close()
    return hora, minuto


def add_minute(hora, minuto):
    minuto=minuto+1
    if minuto>=60:
        hora=hora+1
        minuto=0
    if hora >= 13:
        hora=1
        minuto=0
        
    hora_ = f'0{hora}' if hora<=9 else f'{hora}' 
    minuto_ = f'0{minuto}' if minuto<=9 else f'{minuto}'

    with open(hour_file, 'w') as h:
        h.flush()
        h.write(hora_)
    h.close()
    
    with open(min_file, 'w') as m:
        m.flush()
        m.write(minuto_)
    m.close()
    



#NumeroDeAdelantosEnMinutos indica la cantidad de veces que se debe adelantar o retrasar
def adelanto(adelantos_minutos):
    try:
        for n in range(adelantos_minutos):
            hora, minuto = read_timefile()
            GPIO.output(internalGPIO.add, True)
            t.sleep(internalClock.high_state)
            GPIO.output(internalGPIO.add, False)
            t.sleep(internalClock.low_state)
            add_minute(hora, minuto)
        print(f"\nADELANTADOS: {adelantos_minutos}min")
    except Exception:
        with open(hour_file, 'w') as h:
            h.flush()
            h.write(hora)
        h.close()
        
        with open(min_file, 'w') as m:
            m.flush()
            m.write(minuto)
        m.close()
    


## Convierte cualquiere numero en formato de 12 horas y 60 minutos
class convertir:
    def hora(x):
        hora = x - ((int(x/12))*(12))
        hora = 12 if hora == 0 else hora
        return int(hora)
    
    def minuto(x):
        minuto = x - ((int(x/60))*(60))
        return int(minuto)



def validar_tiempo(hora_ingresada, minuto_ingresado):
    ahora_ = dtime.now()
    dt = dtime(ahora_.year, ahora_.month, ahora_.day, int(hora_ingresada), int(minuto_ingresado), 0)
    conversion_hora=convertir.hora(hora_ingresada)
    conversion_minuto=convertir.minuto(minuto_ingresado) 
    
    horas_calculadas = Ahora.hora() - conversion_hora
    minutos_calculados = Ahora.minuto() - conversion_minuto
    
    horas_minutos = horas_calculadas * 60 
    tiempo_calculado = horas_minutos + minutos_calculados

    if tiempo_calculado <= -1:
        tiempo_calculado=abs(tiempo_calculado)
        retraso_en_adelantos=(12*60) - (tiempo_calculado)
        time_to_fix = dt + tdelta(minutes=retraso_en_adelantos)
        time_to_fix=time_to_fix.strftime('%I:%M:%S')
        print(f"ARREGLAR {time_to_fix}")
        print(f'RETRASO DE {tiempo_calculado}min')
        print(f'HORA REAL: {Ahora.hora()}:{Ahora.minuto()}')
        print(f'HORA FALSA: {conversion_hora}:{conversion_minuto}')
        
        adelanto(retraso_en_adelantos)
        print("Tiempo de retroceso reestablecido")
    
        
        
    elif tiempo_calculado >= 1:
        tiempo_calculado=abs(tiempo_calculado)
        time_to_fix = dt + tdelta(minutes=tiempo_calculado)
        time_to_fix=time_to_fix.strftime('%I:%M:%S')
        print(f"ARREGLAR {time_to_fix}")
        print(f'ADELANTO DE {tiempo_calculado}min')
        print(f'HORA REAL: {Ahora.hora()}:{Ahora.minuto()}')
        print(f'HORA FALSA: {conversion_hora}:{conversion_minuto}')
        
        adelanto(tiempo_calculado)
        
    elif tiempo_calculado == 0:
        print("La hora está sincronizada")


def cambiarhora(hora_erronea, minuto_erroneo):
    print(f"\n[PROCESO] Iniciando método de configuración de hora.")

    conversion_hora=convertir.hora(hora_erronea)
    conversion_minuto=convertir.minuto(minuto_erroneo) 
    
    hora_ = f'0{conversion_hora}' if conversion_hora <= 9 else f'{conversion_hora}'
    minuto_ = f'0{conversion_minuto}' if conversion_minuto <= 9 else f'{conversion_minuto}'
    
    with open(hour_file, 'w') as h:
        h.flush()
        h.write(hora_)
    h.close()
    
    with open(min_file, 'w') as m:
        m.flush()
        m.write(minuto_)
    m.close()
    
    tiempoRetrasado = True
    minutos_a_segundos = 60

    tiempoContado = contar_tiempo_main(validar_tiempo, hora_erronea, minuto_erroneo)
    segundos_a_minutos = tiempoContado / minutos_a_segundos #convertir los segundos de retraso a minutos
    print(f"\n[PROCESO] Iniciando método de restablecimiento de hora retrasada.")

    #loop para adelantar el tiempo retrasado durante el proceso de adelanto
    while(tiempoRetrasado):
        # Si el tiempo del proceso es mayor a un minuto(segundos_a_minutos), adelantar a ese tiempo perdido 
        if (segundos_a_minutos>= 1): 
            segundos_a_minutos = round(segundos_a_minutos)
            print(f"segundos a minutos: {segundos_a_minutos}")

            validacion = contar_tiempo_minor(adelanto, segundos_a_minutos)
            segundos_a_minutos = round(validacion / minutos_a_segundos)
            if (segundos_a_minutos == 0):
                tiempoRetrasado = False
                
        elif (segundos_a_minutos < 1):
            print(f"Hora real: {Ahora.hora()}:{Ahora.minuto()}")
            print(f"¡Cambios realizados! ¡Campanario en hora actual!")
            tiempoRetrasado = False


print(f"[DONE] {os.path.basename(__file__)} cargado.")


