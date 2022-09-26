import os, sys, RPi.GPIO as GPIO, pytz
from datetime import datetime
from time import sleep
GPIO.setmode(GPIO.BOARD)
from getapps import now, singleday, singleweek, singleweekdays, singleweekendays, getsong, alldays


cwd = os.getcwdb()
connection = os.path.join(os.path.expanduser('~'), '.campanario')
mediapath = os.path.join(os.getcwd(), 'campanario/', 'media/')
songspath = os.path.join(mediapath, 'songs/')
utilities = os.path.join(songspath, 'utilities/')
sys.path.append(connection)
sys.path.append(cwd)
sys.path.append(mediapath)
sys.path.append(songspath)
sys.path.append(utilities)

from connection import cur
from appfunctions import play, C, D, E, F, G, A, B, C_, utilidad, finalizar, pines
from validation import music_state, server_state, update_music_state
# import appfunctions, time as t
for pin_num, pin in enumerate(pines): #Confifura como OUTPUT los pines en la lista 
    GPIO.setup(pin, GPIO.OUT)

### Sistema de una canción a la vez
### Si un evento concide con la hora
### -> Reproducir 

print(f"[DONE] {os.path.basename(__file__)} cargado.")


year, month, day, hour, minute, second = (None for i in range(6))


while server_state()[0][0]:

### Primera orden
    
    # ahora=    
    single=singleday()
    idlist, timelist, datelist, thisyear, songidlist = single

    
    class Now:
        año, mes, dia, hora, minuto, segundo = now()

    for items in enumerate(idlist):
        itemid = items[0]
        ids, times = idlist[itemid], timelist[itemid] 
        dates, cy, songs = datelist[itemid], thisyear[itemid], songidlist[itemid]
        year, month, day = int(dates[:-6]), int(dates[5:-3]), int(dates[8:]) 
        hour, minute = int(times[:-3]), int(times[3:])

    ## 1. Valida si el mes, día, hora y minuto coincide con un evento específico
    ## 2. El evento sólo se puede reproducir en los primeros cinco segundos de ese minuto:
    ## -> Condición creada para evitar que el mismo evento se repita dentro del mismo minuto
    

    ## Si sólo existe el thread principal, significa que puede crear un thread 
    ## para reproducir la canción
        specificday=[Now.mes==month and Now.dia==day and 
                    Now.hora==hour and Now.minuto==minute and
                    5 >= Now.segundo and music_state()[0][0] is False]
                    
        if all(specificday):
            print(f"[ID: {ids}] Iniciando evento de día específico...") 
            update_music_state(True)
            getsong(songs,)
            update_music_state(False)
            sleep(5)
            
            
### Segunda orden
    
    idlist, timelist, weekdays, thisyear, songidlist = singleweek()
    items=enumerate(idlist)
    for item in items: ### Por cada evento
        idnum=item[0] ## Recibe los siete días de esa semana
        for weekday in range(7):
            cy, songid = thisyear[idnum], songidlist[idnum] 
            ids, times, days = idlist[idnum], timelist[idnum], weekdays[idnum][weekday]   
            year, month, day = int(days[:-6]), int(days[5:-3]), int(days[8:])
            hour, minute = int(times[:-3]), int(times[3:]) 

            # Validation time
            ### Válida si hay un evento en perfil de semana específica que coincida para 
            ### Reproducirse a el momento actual
            specificweek=[Now.mes==month and Now.dia==day and 
                            Now.hora==hour and Now.minuto==minute and 
                            5 >= Now.segundo and music_state()[0][0] is False]
            
            if all(specificweek):
                print(f"[ID: {ids}] Iniciando evento de semana...")

                update_music_state(True)
                getsong(songid,)
                update_music_state(False)
                sleep(5)




### Tercera orden
    
    idlist, timelist, currentyear, songidlist = singleweekendays()

    today = datetime(Now.año, Now.mes, Now.dia)
    weekday = today.weekday() 
    if weekday <= 4: ## Si es día de semana
        for num_item, items in enumerate(idlist): ## Iterar todos los items
            
            times = timelist[num_item]
            ids, cy, songid = idlist[num_item], currentyear[num_item], songidlist[num_item]
            hour, minute = int(times[:-3]), int(times[3:]) 
            
            validation=[Now.hora==hour and Now.minuto==minute and 
                        5 >= Now.segundo and music_state()[0][0] is False]
            
            if all(validation): ## Si se cumplen los requisitos
                print(f"[ID: {ids}] Iniciando lunes a viernes...")     
                update_music_state(True)            
                getsong(songid, )
                update_music_state(False)
                sleep(5)
                    
                    

### Cuarta orden

    idlist, timelist, currentyear, songidlist = singleweekdays()

    today = datetime(Now.año, Now.mes, Now.dia)
    weekday = today.weekday() 
    if weekday > 4: ## Si es fin de semana
        for num_item, items in enumerate(idlist): ## Iterar todos los items
            times = timelist[num_item]
            ids, cy, songid = idlist[num_item], currentyear[num_item], songidlist[num_item]
            hour, minute = int(times[:-3]), int(times[3:]) 
            
            validation = [
                Now.hora==hour and Now.minuto==minute and 
                5 >= Now.segundo and music_state()[0][0] is False
            ]
            if all(validation): 
                print(f"[ID: {ids}] Iniciando sabado a domingo...") 
                update_music_state(True)
                getsong(songid, )
                update_music_state(False)


                    
### Quinta orden

    idlist, timelist, currentyear, songidlist = alldays()

    for num_item, items in enumerate(idlist): ## Iterar todos los items
        
        times = timelist[num_item]
        ids, cy, songid = idlist[num_item], currentyear[num_item], songidlist[num_item]
        hour, minute = int(times[:-3]), int(times[3:]) 
        
        validation = [Now.hora==hour and Now.minuto==minute and 
                    5 >= Now.segundo and music_state()[0][0] is False]

        if all(validation): ## Si se cumplen los requisitos
            print(f"[ID: {ids}] Iniciando todos los días...")
            update_music_state(True) 
            getsong(songid, )
            update_music_state(False)
            sleep(5)