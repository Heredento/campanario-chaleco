from ast import Is
from datetime import datetime as dtime
import time as t

# Tiempo definido de espera para cada adelanto y retraso de tiempo
TiempoParaRotacion = 1
estadoActivo = TiempoParaRotacion * 0.8 # ochenta porciento
estadoApagado = TiempoParaRotacion *  0.2 # ochenta porciento


#Funcion para contar el tiempo de la funcion validacion de tiempo
def contarTiempoMain(correrFuncion, *tiempo):
    st = t.time()
    correrFuncion(tiempo[0], tiempo[1])
    et = t.time()
    tEjecucion = round(et-st, 2)
    #tEjecucion = 120
    print(f"Tiempo de ejecucion: {tEjecucion}s | Main")
    return tEjecucion

#Funcion para contar el tiempo de la funcion retraso y adelanto
def contarTiempoMinor(correrFuncion, AdelantoRetraso):
    st = t.time()
    correrFuncion(AdelantoRetraso)
    et = t.time()
    tEjecucion = round(et-st, 2)
    #tEjecucion = 120
    print(f"Tiempo de ejecucion: {tEjecucion}s | Minor")
    return tEjecucion


def currentTime():
    now = dtime.now()
    secReal = int(now.strftime('%S'))
    horaReal = int(now.strftime('%I'))
    minReal = int(now.strftime('%M'))
    tReal = [horaReal, minReal, secReal]
    return tReal

def displayCurrentTime():
    print(f"Hora real: {int(currentTime()[0])}:{int(currentTime()[1])}:{int(currentTime()[2])}")

#t.sleep(3)
def horaReal():
    horaReal = int(currentTime()[0])
    return horaReal

def minReal():
    minReal = int(currentTime()[1])
    return minReal

def secReal():
    secReal = int(currentTime()[2])
    return secReal


#NumeroDeAdelantosEnMinutos indica la cantidad de veces que se debe adelantar o retrasar
def adelanto(NumeroDeAdelantosEnMinutos):
    for n in range(NumeroDeAdelantosEnMinutos):
        pass # salida alta (adelantar uno)
        t.sleep(estadoActivo)
        pass # salida baja
        t.sleep(estadoApagado)
    print(f"\nSe han adelantado: {NumeroDeAdelantosEnMinutos}min")

def retraso(NumeroDeAdelantosEnMinutos):
    for n in range(NumeroDeAdelantosEnMinutos):
        pass # salida alta (retrasar uno)
        t.sleep(estadoActivo)
        pass # salida baja
        t.sleep(estadoApagado)
    print(f"Se han restablecido: {NumeroDeAdelantosEnMinutos}min\n")
        


def ValidacionDeTiempo(hrSubmitted, minSubmitted):
    HorasAMinutos = 60
    # 12:25 > 11:15
    # 12 > 11 -> True
    # 25 > 15 -> True
    # 15 > 25 -> False  
    if (horaReal() > hrSubmitted):
        calcularHora = horaReal() - hrSubmitted # 1h de adelanto (60m)
        if (minReal() > minSubmitted):
            calcularMin = minReal() - minSubmitted
            cambiosHora = (calcularHora * HorasAMinutos) + (calcularMin) 

            # a eliminar luego
            print(f"Hora real: {horaReal()}h:{minReal()}m")
            print(f"Hora erronea: {hrSubmitted}h:{minSubmitted}m")
            print(f"Adelanto: {calcularHora}h:{calcularMin}m | {cambiosHora}min total")

            #no eliminar
            adelanto(cambiosHora)

        elif (minReal() < minSubmitted):
            calcularMin = minSubmitted - minReal() 
            cambiosHora = (calcularHora * 60) - calcularMin
            # a eliminar luego
            print(f"Hora real: {horaReal()}h:{minReal()}m")
            print(f"Hora erronea: {hrSubmitted}h:{minSubmitted}m")
            print(f"Adelanto: {calcularHora}h | Retraso: {calcularMin}m | {cambiosHora}min total")

            # no eliminar
            adelanto(cambiosHora)

        elif (minReal() == minSubmitted):
            calcularMin = minSubmitted - minReal() 
            cambiosHora = calcularHora * 60 + calcularMin
            # a eliminar luego
            print(f"Hora real: {horaReal()}h:{minReal()}m")
            print(f"Hora erronea: {hrSubmitted}h:{minSubmitted}m")
            print(f"Adelanto: {calcularHora}h | Retraso: {calcularMin}m | {cambiosHora}min total")

            # no eliminar
            adelanto(cambiosHora)

 
    
    # 35 > 25
    elif (horaReal() < hrSubmitted):
            calcularHora = hrSubmitted - horaReal() # 1h de retraso (60m)
            if (minReal() > minSubmitted):
                calcularMin = minReal() - minSubmitted
                cambiosHora = (calcularHora * HorasAMinutos) + (calcularMin) 
                # a eliminar luego
                print(f"Hora real: {horaReal()}h:{minReal()}m")
                print(f"Hora erronea: {hrSubmitted}h:{minSubmitted}m")
                print(f"Retraso: {calcularHora}h:{calcularMin}m | {cambiosHora}min total")

                #no eliminar
                retraso(cambiosHora)

            # 1h de retraso (60m)
            # 25 < 35
            elif (minReal() < minSubmitted):
                calcularMin = minSubmitted - minReal() 
                cambiosHora = (calcularHora * HorasAMinutos) - calcularMin
                # a eliminar luego
                print(f"Hora real: {horaReal()}h:{minReal()}m")
                print(f"Hora erronea: {hrSubmitted}h:{minSubmitted}m")
                print(f"Retraso: {calcularHora}h | Adelanto de: {calcularMin}m | {cambiosHora}min total")

                # no eliminar
                #adelanto(calcularMin)
                retraso(cambiosHora)

            elif (minReal() == minSubmitted):
                calcularMin = minSubmitted - minReal() 
                cambiosHora = (calcularHora * HorasAMinutos) + calcularMin
                # a eliminar luego
                print(f"Hora real: {horaReal()}h:{minReal()}m")
                print(f"Hora erronea: {hrSubmitted}h:{minSubmitted}m")
                print(f"Retraso: {calcularHora}h | Adelanto: {calcularMin}m | {cambiosHora}min total")
                retraso(cambiosHora)

    elif (horaReal() == hrSubmitted):
                calcularHora = hrSubmitted - horaReal() # 1h de retraso (60m)
                if (minReal() > minSubmitted):
                    calcularMin = minReal() - minSubmitted
                    cambiosHora = (calcularHora * HorasAMinutos) + (calcularMin) 
                    # a eliminar luego
                    print(f"Hora real: {horaReal()}h:{minReal()}m")
                    print(f"Hora erronea: {hrSubmitted}h:{minSubmitted}m")
                    print(f"Retraso: {calcularHora}h:{calcularMin}m | {cambiosHora}min total")
                    #no eliminar
                    retraso(cambiosHora)

                # 1h de retraso (60m)
                # 25 < 35
                elif (minReal() < minSubmitted):
                    calcularMin = minSubmitted - minReal() 
                    # a eliminar luego
                    print(f"Hora real: {horaReal()}h:{minReal()}m")
                    print(f"Hora erronea: {hrSubmitted}h:{minSubmitted}m")
                    print(f"Adelanto: {calcularHora}h | Retraso: :{calcularMin}m")

                    # no eliminar
                    adelanto(calcularHora)
                    retraso(calcularMin)

                elif (minReal() == minSubmitted):
                    calcularMin = minSubmitted - minReal() 
                    cambiosHora = calcularHora * 60
                    # a eliminar luego
                    print(f"Hora real: {horaReal()}h:{minReal()}m")
                    print(f"Hora erronea: {hrSubmitted}h:{minSubmitted}m")
                    print(f"Adelanto: {calcularHora}h | Retraso: {calcularMin}m")

                    # no eliminar
                    adelanto(cambiosHora)


    elif (horaReal() == hrSubmitted and minReal() == minSubmitted):
        print(f"Hora real: {horaReal()}h:{minReal()}m")
        print(f"No han habido cambios, el reloj está sincronizado")
        



def controlManualDeHora(horaErronea, minutoErroneo):
    print(f"\n[PROCESO] Iniciando método de configuración de hora.")
    tiempoRetrasado = True
    minutosASegundos = 60

    tiempoContado = contarTiempoMain(ValidacionDeTiempo, horaErronea, minutoErroneo)
    segundosAMinutos = tiempoContado / minutosASegundos #convertir los segundos de retraso a minutos
    print(f"\n[PROCESO] Iniciando método de restablecimiento de hora retrasada.")
    #loop para adelantar el tiempo retrasado durante el proceso de adelanto
    while(tiempoRetrasado):
        # Si el tiempo del proceso es mayor a un minuto(segundosAMinutos), adelantar a ese tiempo perdido 
        if (segundosAMinutos>= 1): 
            segundosAMinutos = round(segundosAMinutos)
            print(f"segundosAMinutos: {segundosAMinutos}")

            validacion = contarTiempoMinor(adelanto, segundosAMinutos)
            segundosAMinutos = round(validacion / minutosASegundos)
            if (segundosAMinutos == 0):
                tiempoRetrasado = False
                
        elif (segundosAMinutos < 1):
            print(f"Hora real: {horaReal()}:{minReal()}")
            print(f"¡Cambios realizados! ¡Campanario en hora actual!")
            tiempoRetrasado = False



controlManualDeHora(7, 20)


