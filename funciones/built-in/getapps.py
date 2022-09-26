import os, sys, time as t, importlib.util, RPi.GPIO as GPIO, pytz
import threading
from threading import Thread
from datetime import datetime, timedelta
connection = os.path.join(os.path.expanduser('~'), '.campanario')
sys.path.append(connection)
GPIO.setmode(GPIO.BOARD)
mediapath = os.path.join(os.getcwd(), 'campanario/', 'media/')
songspath = os.path.join(mediapath, 'songs/')
songspathutils = os.path.join(songspath, 'utilities/')
backuppath = os.path.join(mediapath, 'backups/')
sys.path.append(songspathutils)

from appfunctions import play, C, D, E, F, G, A, B, C_, utilidad, finalizar, pines
import appfunctions
sys.path.append(songspath)
sys.path.append(backuppath)

print(f"[DONE] {os.path.basename(__file__)} cargado.")

for pin_num, pin in enumerate(pines): #Confifura como OUTPUT los pines en la lista 
    GPIO.setup(pin, GPIO.OUT)
from connection import cur


def now():
    # dd/mm/YY H:M:S
    now= datetime.now()
    año= int(now.strftime("%Y"))
    mes= int(now.strftime("%m"))
    dia= int(now.strftime("%d"))
    hora= int(now.strftime("%H"))
    minuto= int(now.strftime("%M"))
    segundo = int(now.strftime("%S"))
    return año, mes, dia, hora, minuto, segundo

def singleday():
    query=f'select id, date, time, currentyear, song from paginaweb_events_list where selection=4;'
    cur.execute(query)
    special=cur.fetchall()
    
    idlist, timelist, datelist, thisyear, songidlist = ([] for i in range(5))

    for idlist_, timelist_, datelist_, thisyear_, songidlist_ in special:
        idlist.append(idlist_)
        datelist.append(timelist_)
        timelist.append(datelist_)
        thisyear.append(thisyear_)
        songidlist.append(songidlist_)
    return idlist, timelist, datelist, thisyear, songidlist

def singleweek():
    query=f'select id, week, time, currentyear, song from paginaweb_events_list where selection=5;'
    cur.execute(query)
    items=cur.fetchall()

    idlist, timelist, weeklist, thisyear, songidlist = ([] for i in range (5))


    
    for idlist_, timelist_, weeklist_, thisyear_, songidlist_ in items:
        idlist.append(idlist_)
        weeklist.append(timelist_)
        timelist.append(weeklist_)
        thisyear.append(thisyear_)
        songidlist.append(songidlist_)

    list1, weekdays=[], []
    for week in weeklist:
        dates = datetime.strptime(week + '-1', "%Y-W%W-%w")
        list1.append(dates)
        
    for day in list1:
        dayweeklist=[]
        for i in range(7):

            tomorrow = str(day + timedelta(days = i))
            dayweeklist.append(tomorrow[:-9])
        weekdays.append(dayweeklist)
    
    
    return idlist, timelist, weekdays, thisyear, songidlist

def singleweekdays():
    query = f'select id, time, currentyear, song from paginaweb_events_list where selection=2;'
    cur.execute(query)
    special=cur.fetchall()
    
    idlist, timelist, currentyear, songidlist = ([] for i in range(4))

    for idlist_, timelist_, currentyear_, songidlist_ in special:
        idlist.append(idlist_)
        timelist.append(timelist_)
        currentyear.append(currentyear_)
        songidlist.append(songidlist_)
        
    return idlist, timelist, currentyear, songidlist

def singleweekendays():
    query = f'select id, time, currentyear, song from paginaweb_events_list where selection=3;'
    cur.execute(query)
    special=cur.fetchall()
    
    idlist, timelist, currentyear, songidlist = ([] for i in range(4))

    for idlist_, timelist_, currentyear_, songidlist_ in special:
        idlist.append(idlist_)
        timelist.append(timelist_)
        currentyear.append(currentyear_)
        songidlist.append(songidlist_)
        
    return idlist, timelist, currentyear, songidlist

def alldays():
    query = f'select id, time, currentyear, song from paginaweb_events_list where selection=1;'
    cur.execute(query)
    special=cur.fetchall()
    
    idlist, timelist, currentyear, songidlist = ([] for i in range(4))
    
    for idlist_, timelist_, currentyear_, songidlist_ in special:
        idlist.append(idlist_)
        timelist.append(timelist_)
        currentyear.append(currentyear_)
        songidlist.append(songidlist_)
    return idlist, timelist, currentyear, songidlist

def playsong(option, song):
        if option == 1:
            filepath = os.path.join(songspath, song)
            os.system(f'python3 {filepath}')
            año, mes, dia, hora, minuto, segundo=now()
            print(f"ID: {song} | [FINISHED] I've finished waiting working at {año}-{mes}-{dia} | {hora}:{minuto}:{segundo}")
                        
        elif option == 0:
            filepath = os.path.join(songspath, 'defaultsong.py')
            os.system(f'python3 {filepath}')
            año, mes, dia, hora, minuto, segundo=now()
            print(f"ID: {song} | [FINISHED] I've finished waiting working at {año}-{mes}-{dia} | {hora}:{minuto}:{segundo}")
            



def getsong(ids: int):
    query = f'select filename from paginaweb_events_files where id={ids};'
    cur.execute(query)
    res = cur.fetchall()
    
    
    if len(res) == 0:
        print("Es cero")
        año, mes, dia, hora, minuto, segundo=now()
        print(f"ID: {ids} | [STARTING] I've started working at {año}-{mes}-{dia} | {hora}:{minuto}:{segundo}")
        today = datetime.now(pytz.timezone('Etc/GMT+6'))

        playsong(0, '')

    
        
    elif len(res) == 1:
        songfile = "".join(res[0])
        songname = songfile.replace(".py", "")
        año, mes, dia, hora, minuto, segundo=now()
        print(f"ID: {ids} | [STARTING] {songfile} I've started working at {año}-{mes}-{dia} | {hora}:{minuto}:{segundo}")
        today = datetime.now(pytz.timezone('Etc/GMT+6'))
        # customsong = threading.Thread(
        #     target=playsong,
        #     name=f'Custom song player {today}',
        #     args=(1, songfile),
        # )   
        playsong(1, songfile)

# getsong(10)
    
    ## Here goes the code
    
