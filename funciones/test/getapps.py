import os, sys
from datetime import datetime, timedelta
connection = os.path.join(os.path.expanduser('~'), '.campanario')
sys.path.append(connection)
from connection import cur

def now():
    # dd/mm/YY H:M:S
    now = datetime.now()
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
    idlist=[]
    timelist=[]
    datelist=[]
    thisyear=[]
    songidlist=[]
    for event in special:
        idlist.append(event[0])
        datelist.append(event[1])
        timelist.append(event[2])
        thisyear.append(event[3])
        songidlist.append(event[4])
    return idlist, timelist, datelist, thisyear, songidlist


def singleweek():
    query=f'select id, week, time, currentyear, song from paginaweb_events_list where selection=5;'
    cur.execute(query)
    items=cur.fetchall()

    idlist=[]
    timelist=[]
    weeklist=[]
    thisyear=[]
    songidlist=[]

    for event in items:
        idlist.append(event[0])
        weeklist.append(event[1])
        timelist.append(event[2])
        thisyear.append(event[3])
        songidlist.append(event[4])

    list1=[]
    for week in weeklist:
        dates = datetime.strptime(week + '-1', "%Y-W%W-%w")
        list1.append(dates)
        
    weekdays=[]
    for day in list1:
        dayweeklist=[]
        for i in range(7):

            tomorrow = str(day + timedelta(days = i))
            dayweeklist.append(tomorrow[:-9])
            # print(i+1, tomorrow)    
        weekdays.append(dayweeklist)
    
    
    return idlist, timelist, weekdays, thisyear, songidlist



    