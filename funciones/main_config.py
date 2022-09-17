import os, sys, datetime, RPi.GPIO as GPIO, psutil
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

time_folder = os.path.join(os.getcwd(), 'funciones/', 'clocktime/')
hour_file = os.path.join(time_folder, 'hour.txt')
min_file = os.path.join(time_folder, 'minute.txt')


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


def guardar_tiempo(hora:int, minuto:int):
    hora_ = f'0{hora}' if hora <= 9 else f'{hora}'
    minuto_ = f'0{minuto}' if minuto <= 9 else f'{minuto}'
    
    with open(hour_file, 'w') as h:
        h.flush()
        h.write(hora_)
    h.close()
    
    with open(min_file, 'w') as m:
        m.flush()
        m.write(minuto_)
    m.close()
    


def last_reboot():
    last_shutoff=datetime.fromtimestamp(psutil.boot_time())
    
    hora_ = f'0{last_shutoff.hour}' if last_shutoff.hour <= 9 else f'{last_shutoff.hour}'
    minuto_ = f'0{last_shutoff.minute}' if last_shutoff.minute <= 9 else f'{last_shutoff.minute}' 
    
    return hora_, minuto_

update_clock_state(False)

check_time = last_reboot()
    
if f'{check_time[0]}{check_time[1]}' != f"{Now.hour}{Now.minute}":
    
    h_cambiar, m_cambiar = int(check_time[0]), int(check_time[1])
    while True:
        if clock_state() is False:
            update_clock_state(True)
            
            cambiarhora(h_cambiar, m_cambiar)
            
            update_clock_state(False)
            break
    sleep(1)


while True:
    today = datetime.now()
    Now.hour, Now.minute, Now.second=today.strftime('%I'), today.strftime('%M'), today.strftime('%S')
    
    try:    
        if int(Now.second) <= 2 and clock_state() is False:
            sleep(1)
            GPIO.output(internalGPIO.add, True)
            sleep(1)
            GPIO.output(internalGPIO.add, False)
            sleep(1)
            guardar_tiempo(int(Now.hour), int(Now.minute))

    except Exception as ex:
        guardar_tiempo(Now.hour, Now.minute)
        print(f"{os.path.basename(__file__)}\nEX: {ex}")
