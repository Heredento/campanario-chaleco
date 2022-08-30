import os, sys, datetime, RPi.GPIO as GPIO
from datetime import date, datetime
from time import sleep
sys.path.append(os.getcwd())
from dependencies import internalGPIO, internalClock
from validation import update_clock_state

GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False)

GPIO.setup(internalGPIO.add, GPIO.OUT)
GPIO.setup(internalGPIO.delete, GPIO.OUT)

sys.path.append(os.getcwd())
from fix_hour import cambiarhora
hora, minuto = int, int
timefile = os.path.join(os.getcwd(), 'funciones/', 'clocktime', 'time.txt')

db = os.path.join(os.path.expanduser('~'), '.campanario')
sys.path.append(db)
from connection import cur

print(f"[DONE] {os.path.basename(__file__)} cargado.")
    
today = datetime.now()
class Now:
    hour, minute, second=today.strftime('%I'), today.strftime('%M'), today.strftime('%S')

def clock_state():
    clock_query = f"select is_active from paginaweb_ClockInformation where name='change_hour';"
    cur.execute(clock_query)
    clock_state = cur.fetchall()[0][0]
    return clock_state

def music_state():
    clock_query = f"select is_active from paginaweb_ClockInformation where name='play_songs';"
    cur.execute(clock_query)
    music_state = cur.fetchall()[0][0]
    return music_state


def guardar_tiempo(hora, minuto):
    with open(timefile, "wt") as ft:
        ft.write(f"{hora}{minuto}")
    ts.close()
    
update_clock_state(False)
with open(timefile, 'r') as ts:
    filetime = str(ts.read()).strip() 
ts.close()

if len(filetime) <= 3:
    print(f"[STARTUP] ARCHIVO DE TIEMPO NO ESTÁ COMPLETO: {filetime}")
    guardar_tiempo(Now.hour, Now.minute)

    sleep(1)
    with open(timefile, 'r') as ts:
        filetime = str(ts.read()).strip() 
    ts.close()

if len(filetime)  >= 5:
    print(f"[STARTUP] ARCHIVO DE TIEMPO ESTA MÁL FORMATEADO: {filetime}")
    guardar_tiempo(Now.hour, Now.minute)

    sleep(1)
    with open(timefile, 'r') as ts:
        filetime = str(ts.read()).strip() 
    ts.close()


if filetime!=f"{Now.hour}{Now.minute}":
    hcambiar, mcambiar = int(filetime[:-2]), int(filetime[2:])
    while True:
        if clock_state() is False:
            update_clock_state(True)
            cambiarhora(hcambiar, mcambiar)
            update_clock_state(False)
            break
    sleep(1)


while True:
    today = datetime.now()
    Now.hour, Now.minute, Now.second=today.strftime('%I'), today.strftime('%M'), today.strftime('%S')
    validation = [hora != Now.hour or minuto != Now.minute]
    # and clock_state is False
    if int(Now.second) <= 2 :
        sleep(1)
        GPIO.output(internalGPIO.add, True)
        sleep(1)
        GPIO.output(internalGPIO.add, False)
        sleep(1)

        print(f'PIN: {internalGPIO.add}')

    with open(timefile, 'r') as ts:
        filetime = ts.read()
    ts.close()

    hora, minuto=filetime[:-2], filetime[2:]
    
    if len(filetime) <= 3 and clock_state() is False:
        print("[RUNTIME] ARCHIVO DE TIEMPO NO ESTÁ COMPLETO...")
        guardar_tiempo(Now.hour, Now.minute)
        sleep(1)
        
    if filetime == "" and clock_state() is False:
        print(f"[RUNTIME] Tiempo vacío: --:-- | {Now.hour}:{Now.minute}")
        guardar_tiempo(Now.hour, Now.minute)
        sleep(1)
    

    ## Update time
    if all(validation) and clock_state() is False:
        horaleida, minutoleido=filetime[:-2], filetime[2:] 
        print(f"SAVED: {horaleida}:{minutoleido} | NOW: {Now.hour}:{Now.minute}")
        hora, minuto = horaleida, minutoleido

        with open(timefile, "wt") as ft:
            ft.write(f"{Now.hour}{Now.minute}")
        ts.close()
        sleep(1)
            
