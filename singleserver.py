import threading, os, sys, time, socket, importlib.util

from campanario.media import songs

## DJANGO SERVER
serverpath = os.path.join(os.getcwd(), 'campanario/', 'manage.py')

## EVENTS
media = os.path.join(os.getcwd(), 'campanario/', 'media/')
sys.path.append(media)

### Songs folder
songspath = os.path.join(media, 'songs/')
sys.path.append(songspath)
utilities = os.path.join(songspath, 'utilities/')
sys.path.append(utilities)
from appfunctions import play, C, D, E, F, G, A, B, C_, utilidad, finalizar
import appfunctions

funcionesfolder= os.path.join(os.getcwd(), 'campanario/', 'funcionesd/')
sys.path.append(funcionesfolder)
from getapps import now, singleday, singleweek, singleweekdays, singleweekendays, getsong 
playsongs = os.path.join(funcionesfolder, 'playsongs.py')

### Backups folder
backupspath = os.path.join(media, 'backups/')
sys.path.append(songspath)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]


def events():
    with open(playsongs, 'r') as f:
        contenido = f.read()
    objectexec = compile(contenido, 'playsongs', 'exec')
    exec(objectexec)
eventsfunction = threading.Thread(target=events)


def webpage():
    os.system(f'python3 {serverpath} runserver {ip}:8080')
server = threading.Thread(target=webpage)

class Server:
    class djangoServer:
        def run():
            server.start()
    class Events:
        def run():    
            eventsfunction.start()
# Server.djangoServer.run()
Server.Events.run()

# Server.djangoServer.run()

# Server.djangoServer.run()

