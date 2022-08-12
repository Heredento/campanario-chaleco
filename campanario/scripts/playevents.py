import os, sys, time as t, threading
from datetime import datetime
connection = os.path.join(os.path.expanduser('~'), '.campanario')
cwd = os.getcwdb()
sys.path.append(connection)
sys.path.append(cwd)
from apps import now, singleday, singleweek, singleweekdays, singleweekendays, getsong


### Sistema de una canción a la vez
### Si un evento concide con la hora
### -> Iniciar un thread
### Si ya existe un thread -> pass


evento = threading.Thread(
            target=getsong, name="Song replayer", 
            args=(None,))


year, month, day, hour, minute, second = (None for i in range(6))

try:
    print("Está activo ekisde")

    notinterruption=True
    threadlist=[]
    while notinterruption:
        

    ### Primer orden
        
        ahora=now()        
        single=singleday()
        idlist, timelist, datelist, thisyear, songidlist = single

        
        class Now:
            año, mes, dia, hora, minuto, segundo = ahora
        

        ## Obtiene la cantidad de threads sucediendo en ese momento
        for thread in threading.enumerate():
            if thread.name not in threadlist:
                threadlist.append(thread.name)
        thread_lenght=len(threadlist)

    
        for items in enumerate(idlist):
            itemid = items[0]
            ids, times = idlist[itemid], timelist[itemid] 
            dates, cy, songs = datelist[itemid], thisyear[itemid], songidlist[itemid]
            year, month, day = int(dates[:-6]), int(dates[5:-3]), int(dates[8:]) 
            hour, minute = int(times[:-3]), int(times[3:])

        ## 1. Valida si el mes, día, hora y minuto coincide con un evento específico
        ## 2. El evento sólo se puede reproducir en los primeros cinco segundos de ese minuto:
        ## -> Condición creada para evitar que el mismo evento se repita dentro del mismo minuto
            
            
        ## Main thread y evento actual
        ## Si ya existe un thread aparte del principal y el de song replayer


        ## Si sólo existe el thread principal, significa que puede crear un thread 
        ## para reproducir la canción
            specificday=[Now.mes==month and 
                         Now.dia==day and 
                         Now.hora==hour and 
                         Now.minute==minute and
                         5 >= Now.segundo and
                         thread_lenght == 1]
                        
            if all(specificday):
                print(f"[ID: {ids}] Iniciando evento de día específico...") 
                evento = threading.Thread(
                    target=getsong, name="Song replayer", 
                    args=(songs,))
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


        week = singleweek()
        idlist, timelist, weekdays, thisyear, songidlist = week
        # print(idlist, timelist, thisyear, songidlist)
        items=enumerate(idlist)
        for item in items: ### Por cada evento
            idnum=item[0] ## Recibe los siete días de esa semana
            # print(idnum, item)
            for weekday in range(7):
                cy, songid = thisyear[idnum], songidlist[idnum] 
                ids, times, days = idlist[idnum], timelist[idnum], weekdays[idnum][weekday]   
                year, month, day = int(days[:-6]), int(days[5:-3]), int(days[8:])
                hour, minute = int(times[:-3]), int(times[3:]) 

                # Validation time
                ### Válida si hay un evento en perfil de semana específica que coincida para 
                ### Reproducirse a el momento actual
                specificweek=[Now.mes==month and
                              Now.dia==day and 
                              Now.hora==hour and 
                              Now.minuto==minute and 
                              5 >= Now.segundo]
                
                # Now.mes == month and Now.dia == day and Now.hora == hour 
                #     and Now.minuto == minute and 5 >= Now.segundo
                
                
                if all(specificweek):

                    ## Si sólo existe el thread principal, significa que puede crear un thread 
                    ## para reproducir la canción
                    if thread_lenght == 1:
                        print(f"[ID: {ids}] Iniciando evento de semana...") 
                        evento = threading.Thread(
                            target=getsong, name="Song replayer", 
                            args=(songid,))
                        evento.start()

                        ## Placeholder
                        t.sleep(10)
                        print("Acaba de terminar algo algo...")

                ### Revisa todos los thread y valida si termino de funcionar
                ### Si es así, lo elimina de la lista, y otro evento puede reproducirse
                if evento.name in threadlist:
                    if evento.is_alive() is False:
                        threadlist.remove(evento.name)



    ### Tercera orden

        ## Validate if there are threads apart of the main
        for thread in threading.enumerate():
            if thread.name not in threadlist:
                threadlist.append(thread.name)
        thread_lenght=len(threadlist)
        
        weekenddays = singleweekendays()

        idlist, timelist, currentyear, songidlist = weekenddays

        
        today = datetime(Now.año, Now.mes, Now.dia)
        weekday = today.weekday() 
        if weekday <= 4: ## Si es día de semana
            for num_item, items in enumerate(idlist): ## Iterar todos los items
                
                times = timelist[num_item]
                ids, cy, songid = idlist[num_item], currentyear[num_item], songidlist[num_item]
                hour, minute = int(times[:-3]), int(times[3:]) 
                
                validation=[Now.hora==hour and 
                            Now.minuto==minute and 
                            5 >= Now.segundo and 
                            thread_lenght == 1]
                
                if all(validation): ## Si se cumplen los requisitos
                    print(f"[ID: {ids}] Iniciando todos los días...") 
                    evento = threading.Thread(
                        target=getsong, 
                        name="Song replayer", 
                        args=(songid,))
                    evento.start()

                    ## Placeholder
                    t.sleep(6)
                    print("Acaba de terminar algo algo...")
                       
                       

    ### Cuarta orden

        ## Validate if there are threads apart of the main
        for thread in threading.enumerate():
            if thread.name not in threadlist:
                threadlist.append(thread.name)
        thread_lenght=len(threadlist)
        
        weekdays = singleweekdays()
        idlist, timelist, currentyear, songidlist = weekdays

        today = datetime(Now.año, Now.mes, Now.dia)
        weekday = today.weekday() 
        if weekday > 4: ## Si es fin de semana
            for num_item, items in enumerate(idlist): ## Iterar todos los items
                
                
                times = timelist[num_item]
                ids, cy, songid = idlist[num_item], currentyear[num_item], songidlist[num_item]
                hour, minute = int(times[:-3]), int(times[3:]) 
                
                validation = [
                    Now.hora==hour and 
                    Now.minuto==minute and 
                    5 >= Now.segundo
                ]
                if all(validation): ## Si se cumplen los requisitos
                    if thread_lenght == 1: ## Si no existen eventos thread
                        print(f"[ID: {ids}] Iniciando todos los días...") 
                        evento = threading.Thread(
                            target=getsong, 
                            name="Song replayer", 
                            args=(songid,))
                        evento.start()

                        ## Placeholder
                        t.sleep(6)
                        print("Acaba de terminar algo algo...")
                        
    
    
    
    ### Quinta orden

        ## Validate if there are threads apart of the main
        for thread in threading.enumerate():
            if thread.name not in threadlist:
                threadlist.append(thread.name)
        thread_lenght=len(threadlist)
        
        weekdays = singleweekdays()
        idlist, timelist, currentyear, songidlist = weekdays

        today = datetime(Now.año, Now.mes, Now.dia)
        weekday = today.weekday() 
        
        for num_item, items in enumerate(idlist): ## Iterar todos los items
            
            times = timelist[num_item]
            ids, cy, songid = idlist[num_item], currentyear[num_item], songidlist[num_item]
            hour, minute = int(times[:-3]), int(times[3:]) 
            
            validation = [
                Now.hora==hour and 
                Now.minuto==minute and 
                5 >= Now.segundo and
                thread_lenght == 1]
            if all(validation): ## Si se cumplen los requisitos
                print(f"[ID: {ids}] Iniciando todos los días...") 
                evento = threading.Thread(
                    target=getsong, 
                    name="Song replayer", 
                    args=(songid,))
                evento.start()

                ## Placeholder
                t.sleep(6)
                print("Acaba de terminar algo algo...")


            
                
                


except Exception as ve:
    print(ve)
except KeyboardInterrupt:
    print("Interrupción por teclado")
    notinterruption=False
