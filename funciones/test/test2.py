from math import sin
import os, sys, datetime, time as t, psycopg2, threading
import re
from datetime import date, datetime


connection = os.path.join(os.path.expanduser('~'), '.campanario')
sys.path.append(connection)
from connection import cur

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


single=singleday()
for items in enumerate(single[0]):
    itemid=items[0]
    ids=single[0][itemid]
    times=single[1][itemid]
    dates=single[2][itemid]
    cy=single[3][itemid]
    songs=single[4][itemid]
    hora=int(times[:-3])
    minuto=int(times[3:])
    año=int(dates[:-6])
    mes=int(dates[5:-3])
    dia=int(dates[8:])

    print(f'{ids} | {hora}:{minuto} | {año}:{mes}:{dia} | {songs} | {cy} | ')
