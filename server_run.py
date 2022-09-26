import threading, os, sys, time, socket, importlib.util, RPi.GPIO as GPIO, requests
from datetime import date, datetime, time as t
from campanario.media import songs
import funciones.drivers as drivers
db = os.path.join(os.path.expanduser('~'), '.campanario')
sys.path.append(db)
from connection import cur
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

global connection_state
connection_state: bool
global active_server
active_server: bool
## DJANGO SERVER

sys.path.append(os.getcwd())
from dependencies import internalGPIO, internalClock
for num, music_pin in enumerate(internalGPIO.music):
    GPIO.setup(music_pin, GPIO.OUT)
    GPIO.output(music_pin, True)

for num, clock_pin in enumerate(internalGPIO.clock):
    GPIO.setup(clock_pin, GPIO.OUT)
    GPIO.output(clock_pin, False)
    

from validation import update_clock_state, update_server_state, update_music_state


## EVENTS
media = os.path.join(os.getcwd(), 'campanario/', 'media/')
sys.path.append(media)

## LCD SCRIPT
funciones = os.path.join(os.getcwd(), 'funciones/')
sys.path.append(funciones)

### Songs folder
songspath = os.path.join(media, 'songs/')
sys.path.append(songspath)

### Utilities folder (from songs folder)
utilities = os.path.join(songspath, 'utilities/')
sys.path.append(utilities)
from appfunctions import play, C, D, E, F, G, A, B, C_, utilidad, finalizar, pines
import appfunctions


for pin_num, pin in enumerate(pines):  
    GPIO.setup(pin, GPIO.OUT)

## Folder funcionesdjango
funcionesfolder= os.path.join(os.getcwd(), 'funciones/', 'built-in/')
sys.path.append(funcionesfolder)
from getapps import now, singleday, singleweek, singleweekdays, singleweekendays, getsong 


### Backups folder
backupspath = os.path.join(media, 'backups/')
sys.path.append(songspath)

import requests

def check_connection():
    try:
        requests.head('https://www.google.com/', timeout=20)
        return True
    except Exception: 
        return False
    


def events():
    playsongs = os.path.join(funcionesfolder, 'playsongs.py')
    os.system(f'python3 {playsongs}')
eventsfunction = threading.Thread(target=events)

def webpage_local():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip = s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    serverpath = os.path.join(os.getcwd(), 'campanario/', 'manage.py')
    os.system(f'python3 {serverpath} runserver {ip}:8080 --insecure')


def webpage_localmachine():
    serverpath = os.path.join(os.getcwd(), 'campanario/', 'manage.py')
    os.system(f'python3 {serverpath} runserver 127.0.0.1:8080 --insecure')


def lcdscreens():
    lcdfolder = os.path.join(funciones, 'lcd_time.py')
    os.system(f'python3 {lcdfolder}')
lcdscreen = threading.Thread(target=lcdscreens)

def time_config():
    hourfix = os.path.join(funciones, 'main_config.py')
    os.system(f'python3 {hourfix}')
clock_function = threading.Thread(target=time_config)

def display_lights():
    # ## check display lights
    # create_query=f"select start_time, finish_time from paginaweb_ScheduledTasks where name='scheduled_lights';"
    # cur.execute(create_query)
    # object_ = cur.fetchall()
    # print(object_)
    # start_time, finish_time = datetime()
    # if len(object_) == 0:
    #     query_ = f"insert into paginaweb_ScheduledTasks (name, start_time, finish_time) VALUES ('scheduled_lights', None, None)"
    #     cur.execute(query_)
    #     cur.commit()
    while True:
        query=f"select start_time, finish_time from paginaweb_ScheduledTasks where name='scheduled_lights';"
        cur.execute(query)
        object = cur.fetchall()[0]
        start_time, finish_time = object[0], object[1]
        
        n = datetime.now()
        time_now = t(n.hour, n.minute)
        if (start_time < time_now < finish_time):
            # print("aye")
            GPIO.output(internalGPIO.lights, True)
            time.sleep(1)
        else:
            # print("nay")
            GPIO.output(internalGPIO.lights, False)
            time.sleep(1)

lights_system = threading.Thread(target=display_lights)

def provisional_connection(connection_function, runserver_local, runserver_localhost):
        server_running = False
        while True:
            connected_state = connection_function()
            if (connected_state is True):
                print(server_running)
                if server_running is False:
                    
                    server_running = True
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    ip = s.connect(("8.8.8.8", 80))
                    ip = s.getsockname()[0]
                    
                    os.system('pkill -f runserver')
                    runserver_local()
                    
                    print(f"Corriendo en {ip}:8080")
                elif server_running == True:
                    while True:
                        sub_connected_state = connection_function()
                        if sub_connected_state is True:
                            pass
                        elif sub_connected_state is False:
                            server_running = False
                            break
                    
            elif (connected_state is False):
                print(server_running)
                if server_running is False:
                    server_running = True
                    os.system('pkill -f runserver')
                    runserver_localhost()
                    
                    print(f"Corriendo en 127.0.0.1:8080 ")
                    
                elif server_running == True:
                    while True:
                        sub_connected_state = connection_function()
                        if sub_connected_state is False:
                            pass
                        elif sub_connected_state is True:
                            server_running = False
                            break
            time.sleep(1)


class Server:
    class djangoLocal:
        def run():
            server_local = threading.Thread(target=webpage_local, name=datetime.now())
            server_local.start()

    class djangoLocalhost:
        def run():
            server_localhost = threading.Thread(target=webpage_localmachine, name=datetime.now())
            server_localhost.start()
    class Events:
        def run():    
            eventsfunction.start()

    class ScreenLCD:
        def run():
            lcdscreen.start()

    class clockTime:
        def run():
            clock_function.start()
    class lightState:
        def run():
            lights_system.start()

connection_fix = threading.Thread(
    target=provisional_connection,
    args=(
        check_connection, 
        Server.djangoLocal.run, 
        Server.djangoLocalhost.run
    )
)

class ProvisionalServer:
    def run():
        connection_fix.start()

try: 
    update_server_state(True)
    update_clock_state(False)
    time.sleep(1)
    ProvisionalServer.run()
    Server.ScreenLCD.run()
    Server.Events.run()
    Server.clockTime.run()
    Server.lightState.run()

except Exception as ex:
    GPIO.cleanup()
    update_server_state(False)

