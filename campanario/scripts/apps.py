import os, sys, time as t
from datetime import datetime, timedelta
connection = os.path.join(os.path.expanduser('~'), '.campanario')
sys.path.append(connection)
from connection import cur
from django.conf import settings


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
    
    try:
        if option == 1:
            filepath = sys.path.append(os.path.join(settings.MEDIA_ROOT, 'songs/', song))
            # filename = song.replace('.py', '')
            os.system(f'python3 -m {filepath}')
            
        elif option == 0:
            filepath = sys.path.append(os.path.join(settings.MEDIA_ROOT, 'backups/', 'utilities/', 'defaultsong.py'))
            os.system(f'python3 -m {filepath}')
            # with open(filenamepath) as f:
            #     exec(compile(f.read(), filename, "exec"))
        else:
            print("Ha habido un error")
    except Exception as ex:
        print(f'[EXCEPCIÓN] {ex}')
        


def getsong(ids: int):
    query = f'select filename from paginaweb_events_files where id={ids};'
    cur.execute(query)
    res = cur.fetchall()
    if len(res) == 0:
        print(res)
        # playsong(0, 'defaultsong')
        
    elif len(res) == 1:
        songfile = "".join(res[0])
        # playsong(0, songfile)
        print(songfile)
    else:
        print("QUE")



    año, mes, dia, hora, minuto, segundo=now()
    print(f"ID: {ids} | [STARTING] I've started working at {año}-{mes}-{dia} | {hora}:{minuto}:{segundo}")
    ## Here goes the code
    t.sleep(20)
    año, mes, dia, hora, minuto, segundo=now()
    print(f"ID: {ids} | [FINISHED] I've finished waiting working at {año}-{mes}-{dia} | {hora}:{minuto}:{segundo}")
