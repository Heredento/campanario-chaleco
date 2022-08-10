from math import sin
import os, sys, datetime, time as t, psycopg2, threading
from pickle import APPEND
from datetime import date, datetime
connection = os.path.join(os.path.expanduser('~'), '.campanario')
cwd = os.getcwdb()
sys.path.append(connection)
sys.path.append(cwd)
from connection import cur
from getapps import singleday, singleweek, now
        
### Sistema de una canción a la vez
### Si un evento concide con la hora
### -> Iniciar un thread
### Si ya existe un thread -> pass

def getsong(id, hora, minuto):
    print(f"ID: {id} | I've started to work at {hora}:{minuto}...", )
    t.sleep(20)
    tnow=now()
    print(f"ID: {id} | I've finished waiting working at {tnow[3]}:{tnow[4]}...")

evento = threading.Thread(
            target=getsong, name="Song replayer", 
            args=(None, None, None))


try:
    notinterruption=True
    threadlist=[]
    while notinterruption:
    
        
        
    ### Primer orden
        single=singleday()
        ahora=now()
        
        


        for thread in threading.enumerate():
            if thread.name not in threadlist:
                threadlist.append(thread.name)
        thread_lenght=len(threadlist)

        
        # print(f'single: {threadlist}')

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

        ## 1. Valida si el mes, día, hora y minuto coincide con un evento específico
        ## 2. El evento sólo se puede reproducir en los primeros cinco segundos de ese minuto:
        ## -> Condición creada para evitar que el mismo evento se repita dentro del mismo minuto
            
            if (ahora[1]==mes and ahora[2]==dia and 
                ahora[3]==hora and ahora[4]==minuto and 5 >= ahora[5]):

                ## Obtiene la cantidad de threads sucediendo en ese momento
                
                ## Main thread y evento actual
                ## Si ya existe un thread aparte del principal y el de song replayer


                ## Si sólo existe el thread principal, significa que puede crear un thread 
                ## para reproducir la canción
                if thread_lenght == 1:
                    print(f"[ID: {ids}] Iniciando evento de día específico...") 
                    evento = threading.Thread(
                        target=getsong, name="Song replayer", 
                        args=(ids, ahora[3], ahora[4]))
                    evento.start()
                    
                    
                    
                    ## Placeholder
                    t.sleep(10)
                    print("Acaba de terminar algo...")
            if evento.name in threadlist:
                if evento.is_alive() is False:
                    threadlist.remove(evento.name)
    ### Segunda orden
        
        ## Validate if there are threads apart of the main
        for thread in threading.enumerate():
            if thread.name not in threadlist:
                threadlist.append(thread.name)
        thread_lenght=len(threadlist)


        weeks=singleweek()

        items=enumerate(weeks[0])
        for item in items: ### For every event
            idnum=item[0] ## Gets event id
            # print(idnum, item)
            for weekday in range(7):
                #idlist, timelist, weekdays, thisyear, songidlist
                ids=weeks[0][idnum]
                times=weeks[1][idnum]
                days=weeks[2][idnum][weekday]
                cy=weeks[3][idnum]
                songid=weeks[4][idnum]
                hour=int(times[:-3])
                minute=int(times[3:])
                day=int(days[8:])
                month=int(days[5:-3])
                # year=(days[:-3])
                # print(f'ID: {ids} | {hora}:{minute} | {year}-{month}-{day} | {songid} | {cy} ')


                ### Validation time
                ### año, mes, dia, hora, minuto, segundo
                print(ahora[1], ahora[2], ahora[3], ahora[4], ahora[5], threadlist, evento.is_alive())
                # print(month, day, hour, minute, type(songid))

                if (
                    ahora[1] == month and ahora[2] == day and 
                    ahora[3] == hour and ahora[4] == minute and 5 >= ahora[5]
                ):

                    ## Si sólo existe el thread principal, significa que puede crear un thread 
                    ## para reproducir la canción
                    if thread_lenght == 1:
                        print(f"[ID: {ids}] Iniciando evento de semana...") 
                        evento = threading.Thread(
                            target=getsong, name="Song replayer", 
                            args=(ids, ahora[3], ahora[4]))
                        evento.start()

                        ## Placeholder
                        t.sleep(10)
                        print("Acaba de terminar algo algo...")
                        # print(ids, times, days)
                if evento.name in threadlist:
                    if evento.is_alive() is False:
                        threadlist.remove(evento.name)

except Exception as ve:
    print(ve)
except KeyboardInterrupt:
    print("Interrupción por teclado")
    notinterruption=False
