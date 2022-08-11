import RPi.GPIO as GPIO, time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Definiciones de salidas Raspberry y sus notas
pines = [8, 10, 12, 16, 18, 22, 24, 26]
C, D, E, F, G, A, B, C_ = pines
global tempo

# Constantes para notas
mH, mL= 7/8, 1/8

for pin_num, pin in enumerate(pines): #Confifura como OUTPUT los pines en la lista 
    GPIO.setup(pin, GPIO.OUT)

# Funciones de utilidad principales
def allLow(x): # 0 Logico en todos los pines de salida de notas
    for pin_num, pin in enumerate(pines):
        GPIO.output(pin, False)
    time.sleep(x)

def s(silencio): #Tipo de silencio
    tps = 60/tempo
    for i in range(1,8):
        if silencio is i:
            sucesion=8*(1/2**silencio)
            y = tps*sucesion 
            time.sleep(y)

def mt(nota): # Tipo de nota (tiempo), x = redonda, blanca, negra, corchea etc..
    tps = 60/tempo
    for i in range(1,8):
        if nota is i:
            sucesion=8*(1/2**nota)
            y = tps*sucesion 
            time.sleep(mH*y)
            allLow(mL*y)

def playNota(duracion, *notas): # Funcion para tocar x cantidad de notas + el tipo que es
    nota=list(notas)
    for num, arg in enumerate(notas):
        GPIO.output(nota[num], True)
    mt(duracion)

# Funcion principal, reproduce cantidad notas, configura su tiempo e indica si es o no silencio 
def play(modo=0, tipo=3, *notas): #*argv: notas a reproducir, usar C, D, E, F.. C_ como notas.
    match modo:
        case 0:
            s(tipo)
        case 1:
            playNota(tipo, *notas)
        case other:
            print(f"Argumentos invalidos en play({modo},{tipo},{notas})")
            if modo == 1:
                if notas not in pines:
                    print(f"La notas entre {notas} tienen problemas, sólo puedes usar C, D, E, F, G, A, B, C_ SIN COMILLAS y CON COMMAS")
            if modo < 0 or modo > 1:
                print(f"El módo es {modo} pero sólo puede ser 0 o 1.")
            if tipo < 0 > tipo > 7:
                print(f"El tipo es {tipo} pero sólo se puede usar entre 1 y 7")

            

def utilidad():
    print("Configuración:")
    print(f"{pines}")
    print(f"C, D, E, F, G, A, B, C+")
    print(f"Empezando script midi..")
    print(f"tempo: {tempo}")
    

def finalizar(now, start_time):
    elapsed= now - start_time
    horas, minutos, segundos, milisegundos = int(elapsed/3600), int(elapsed/60), int(elapsed),int(round(elapsed*100, 4))
    print(f'Tiempo tardado: {horas}h {minutos}m {segundos}s {milisegundos}ms')
    time.sleep(0.1)
    GPIO.cleanup()
