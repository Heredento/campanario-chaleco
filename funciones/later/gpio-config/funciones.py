# Configuración
import RPi.GPIO as GPIO
import time 
global tempo
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BOARD)
# Definiciones de salidas Raspberry y sus notas
pines = [8, 10, 12, 16, 18, 22, 24, 26]


# constantes para notas sostenidas
mH = 7/8
mL = 1/8

conteo=range(len(pines))
C = pines[0]
D = pines[1]
E = pines[2]
F = pines[3]
G = pines[4]
A = pines[5]
B = pines[6]
C_ = pines[7]

for i in conteo: #Confifura como OUTPUT los pines en la lista 
        GPIO.setup(pines[i], GPIO.OUT)

# Funciones de utilidad principales
def allLow(x): # 0 Logico en todos los pines de salida de notas
    for i in conteo:
        GPIO.output(pines[i], False)
    time.sleep(x)

def s(x): #Tipo de silencio
    tps = 60/tempo
    match x:
        case 1: # Redonda
            y = tps*4 
            time.sleep(y)
        case 2: # Blanca
            y = tps*2
            time.sleep(y)
        case 3: #Negra
            y = tps*1
            time.sleep(y)
        case 4: #Corchea
            y = tps*(1/2)
            time.sleep(y)
        case 5: #Semicorchea
            y = tps*(1/4)
            time.sleep(y)
        case 6: #Fusa
            y = tps*(1/8)
            time.sleep(y)
        case 7: #Semifusa
            y = tps*(1/16)
            time.sleep(y)
        case other: #No existente
            pass

def mt(x): # Tipo de nota (tiempo), x = redonda, blanca, negra, corchea etc..
    tps = 60/tempo
    match x:
        case 1: #Redonda
            y = tps*4
            time.sleep(mH*y)
            allLow(mL*y)
        case 2: #Blanca
            y = tps*2
            time.sleep(mH*y)
            allLow(mL*y)
        case 3: #Negra
            y = tps*1
            time.sleep(mH*y)
            allLow(mL*y)
        case 4: #Corchea
            y = tps*(1/2)
            time.sleep(mH*y)
            allLow(mL*y)
        case 5: #Semicorchea
            y = tps*(1/4)
            time.sleep(mH*y)
            allLow(mL*y)
        case 6: #Fusa
            y = tps*(1/8)
            time.sleep(mH*y)
            allLow(mL*y)
        case 7: #Semifusa
            y = tps*(1/16)
            time.sleep(mH*y)
            allLow(mL*y)
        case other: #No existente
            pass

def playNota(duracion, *notas): # Funcion para tocar x cantidad de notas + el tipo que es
    nota=list(notas)
    c = range(len(notas))
    for arg in c:
        GPIO.output(nota[arg], True)
    mt(duracion)

# Funcion principal, reproduce cantidad notas, configura su tiempo e indica si es o no silencio 
def play(modo=0, tipo=3, *notas): #*argv: notas a reproducir, usar C, D, E, F.. C_ como notas.
    #print(tempo) # verificar tempo ( FUNCIONA! )
    match modo:
        case 0:
            s(tipo)
        case 1:
            playNota(tipo, *notas)
        case other:
            print("Argumentos invalidos")
            pass

def utilidad():
    print("Configuración:")
    print(f"{pines}")
    print(f"C, D, E, F, G, A, B, C+")
    print(f"Empezando script midi..")
    print(f"tempo: {tempo}")
def interrupcion():
    print("Partitura interrumpida")
    GPIO.cleanup()

def limpieza():
    time.sleep(0.1)
    GPIO.cleanup()

def finalizar():
    for y in range(3,0,-1):
        print(f"Terminando en {y}")
        time.sleep(1)
    limpieza()
