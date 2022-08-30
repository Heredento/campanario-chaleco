import threading, os, sys, time, socket, importlib.util, RPi.GPIO as GPIO
from django.db.models import Expression
from campanario.media import songs
import funciones.drivers as drivers
db = os.path.join(os.path.expanduser('~'), '.campanario')
sys.path.append(db)
from connection import cur
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
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

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]


def events():
    playsongs = os.path.join(funcionesfolder, 'playsongs.py')
    os.system(f'python3 {playsongs}')
eventsfunction = threading.Thread(target=events)

def webpage():
    serverpath = os.path.join(os.getcwd(), 'campanario/', 'manage.py')
    os.system(f'python3 {serverpath} runserver {ip}:8080')
server = threading.Thread(target=webpage)

def lcdscreens():
    lcdfolder = os.path.join(funciones, 'lcd_time.py')
    os.system(f'python3 {lcdfolder}')
lcdscreen = threading.Thread(target=lcdscreens)

def time_config():
    hourfix = os.path.join(funciones, 'main_config.py')
    os.system(f'python3 {hourfix}')
clock_function = threading.Thread(target=time_config)

class Server:
    class djangoServer:
        def run():
            server.start()
    class Events:
        def run():    
            eventsfunction.start()

    class ScreenLCD:
        def run():
            lcdscreen.start()

    class clockTime:
        def run():
            clock_function.start()


try: 
    ## Estados de condición
    update_server_state(True)
    update_clock_state(False)
    update_clock_state(False)

    time.sleep(1)

    Server.djangoServer.run()
    Server.ScreenLCD.run()
    Server.Events.run()
    Server.clockTime.run()

except KeyboardInterrupt:
    print("Interrupción de teclado")
    update_server_state(False)
    GPIO.cleanup()

except Exception:
    update_server_state(False)
    GPIO.cleanup()
