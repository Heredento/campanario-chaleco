from ctypes import string_at
import os, sys, os.path, ipaddress, re, time as t
root = os.path.join(os.path.expanduser('~'), '.campanario')
dbfileservice= os.path.join(root, 'db.py')
emailcon= os.path.join(root, 'emailcon.py')
connection = os.path.join(root, 'connection.py')
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

## Get dir and files existences
rootvalidation = os.path.isdir(root)
dbexists=os.path.exists(dbfileservice)
emailconexists=os.path.exists(emailcon)
conexists=os.path.exists(connection)

## Get py and git versions
getversion=sys.version_info
pyversion3=int(getversion[0])
pyversion_10=int(getversion[1])
pytrue=True
gitisinstalled=False

def read_delayed(mensaje:str):
    print(mensaje)
    t.sleep(1/15)

def validateip(address):
    try:
        ipaddress.ip_address(address)
        return True
    except ValueError:
        return False

def validateemail(email):
    email=str(email)
    if re.fullmatch(regex, email):
      return True
    else:
      return False


try:
    os.system('git version')
    os.system('python3 --version')
    gitisinstalled=True

except Exception:
    gitisinstalled=False

while(pyversion_10):
    if (pyversion3 >= 3 and pyversion_10 >= 10) and (gitisinstalled is True):
        read_delayed("¡Requisitos superados! 🙌\n")
        pyversion_10=False
    else:
        read_delayed("Parece que no cumples los siguientes requisitos:")
        if gitisinstalled == False:
            read_delayed("Se requiere git instalado...")
            read_delayed("Puede instalarlo desde https://git-scm.com/downloads")
        if pyversion3 >= 3 and 10 >= pyversion_10:
            read_delayed("Se requiere una versión de python más reciente...")
            read_delayed("La versión de python debe ser mayor o igual a 3.10")
            read_delayed("Puedes descargar la última versión desde https://www.python.org/downloads/")
        sys.exit()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')




def creacionDBFiles(): 
    try:
        read_delayed("\n> CONFIGURACIÓN DE BASE DE DATOS DEL CAMPANARIO <")
        read_delayed("En este momento vamos a declarar información que se usará en adelante para el campanario.")
        read_delayed("Presiona CTRL + C para pasar a la creación de correos.")
        read_delayed("Vuelve a presionar CTRL + C para CANCELAR.")
        read_delayed("Cuando '(default)' sea mencionado significa que lo puedes dejar en blanco y tomará el mencionado")
        read_delayed("ESTA INFORMACIÓN ES IMPORTANTE, POR FAVOR GUARDALA\n")
        
        def InputArchivos():
            name = input("Escribe el nombre de la base de datos: ")
            nametrue=True
            while(nametrue):
                if name=='':
                    name = input("Escribe un nombre que no sea vacío: ")
                elif 3 >= len(name):
                    name = input("Ingresa un nombre no menor de cuatro caracteres: ")
                else:
                    nametrue=False

            usertrue=True
            user = input("Escribe el nommbre del dueño de la base de datos: ")
            while(usertrue):
                if user=='':
                    user = input("El nombre no del dueño no puede estar vacío: ")
                else:
                    usertrue=False

            password = input("Escribe una contraseña mayor a 8 caracteres: ")
            passtrue=True
            while(passtrue):
                if 7 > len(password):
                    password = input("Escribe una contraseña mayor a 8 caracteres: ")
                elif password == '':
                    password = input("La contraseña no puede estar vacía, ingresa una contraseña: ")
                else:
                    passtrue=False
            hosttrue=True    
            host = input("Escribe el host del servidor (default localhost: 127.0.0.1): ")
            while(hosttrue):
                if host == '':
                    host='127.0.0.1'
                    hosttrue=False
                elif validateip(host) == True:
                    host=host
                    hosttrue=False
                elif validateip(host) == False:
                    host = input("Escribe un host válido (default: localhost): ")
                
            porttrue=True           
            port = input("Ingresa el puerto(default: 5432): ")
            while(porttrue):
                if port == '':
                    port='5432'
                    porttrue=False
                elif int(port) > 65535 or 0 or 65535:
                    port=input("Ingresa un puerto válido (default: 5432): ")
                elif int(port) < 65535:
                    port=port
                    porttrue=False
                else:
                    port=input("Ingresa un puerto válido (default: 5432): ")
            
            read_delayed("La información es la siguiente: ")
            dbservice= (f'''
class dbservice:
    name ='{name}'
    user ='{user}'
    password= '{password}'
    host =  '{host}'
    port = '{port}'
                ''')
            read_delayed(dbservice)
            
            return name, user, password, host, port
        

        inputs = InputArchivos()
        
        confirm=True
        while(confirm):
            confirmation = input("¿Es correcto?(y/n) ")
            if confirmation=='y':
                read_delayed(f"El archivo y sus dependencias se crearán en {root}")
                read_delayed("Dependencias:")
                read_delayed(f"> {dbfileservice}")
                read_delayed(f"> {connection}")
                confirm=False
            elif confirmation=='n':
                inputs = InputArchivos()

            else:
                read_delayed("Ingresaste algo equivocado...\n")
                inputs = InputArchivos()
        
        
        name = inputs[0]
        user = inputs[1]
        password = inputs[2]
        host = inputs[3]
        port = inputs[4]
        
        dbservice= f'''
class dbservice:
    name ='{name}'
    user ='{user}'
    password= '{password}'
    host =  '{host}'
    port = '{port}'
'''

        match(os.path.isdir(root)):
            case True:
                pass
            case False:
                os.mkdir(root)

        with open(f'{dbfileservice}', 'w') as db:
            for line in dbservice:
                db.write(line)


            
    
        conection=f'''
import psycopg2 
from db import dbservice
try:
    connection=psycopg2.connect(
        host=dbservice.host,
        user=dbservice.user,
        password=dbservice.password,
        database=dbservice.name
        )
    cur = connection.cursor()    
except Exception as ex:
    read_delayed(ex)
        '''

        with open(f'{connection}', 'w') as con:
            for line in conection:
                con.write(line)
        
        read_delayed("Configuración para la base de datos creada exitosamente!")
        
        
    except KeyboardInterrupt:
        read_delayed("Cambiando al panel del correo...")
        exists = [rootvalidation or dbexists or emailconexists or conexists]
        for exist in exists:
            if (exist is True):
                read_delayed(f"Ya existe un directorio o archivo en: {exist}")

    except ValueError as ve:
        read_delayed(f"ValueError: {ve}")


def creacionEmailFiles():
    try: 
        read_delayed("\n> CREACIÓN DE SISTEMA DE ENVÍO DE CORREOS (NO-REPLY) <")
        read_delayed("Antes de empezar a ingresar la información, asegurate que la contraseña sea de aplicación.")
        read_delayed("Porfavor usar una cuenta de google. Puedes abrir el siguiente enlace donde explica como obtenerla")
        read_delayed("Placeholder: https://myaccount.google.com/apppasswords")
        
        def inputCorreo():
            sendertrue=True
            sender = input("Ingresa el correo que enviará a terceros correos: ")
            while sendertrue:
                if validateemail(sender) == True:
                    sendertrue=False
                elif validateemail(sender) == False:
                    sender = input("Ingresa un correo VÁLIDO que enviará a terceros: ")
            passtrue=True
            password=input("Ingresa la contraseña formateada para app de google: ")
            while passtrue:
                if 7 > len(password):
                    password = input("Ingresa una contraseña VÁLIDA: ")
                elif len(password) >= 8:
                    passtrue=False
            receivertrue=True
            receiver=input("Ingresa el correo que estará recibiendo los códigos de verificación: ")
            while receivertrue:
                if validateemail(receiver) == True:
                    receivertrue=False
                elif validateemail(receiver) == False:
                    receiver = input("Ingresa un correo VÁLIDO que recibirá los códigos: ")

                        
            read_delayed("La información es la siguiente: ")
                
            emailservicefile=f'''
class emailservice:
    email='{sender}'
    password='{password}'
    receiver='{receiver}'
            '''     
            read_delayed(emailservicefile)
            return sender, password, receiver 

        
        emailserv=inputCorreo()
                
        confirmation=True
        while confirmation:
            confirm=input("¿Es correcto?(y/n)")
            if confirm=='y':
                confirmation=False
            elif confirm=='n':
                emailserv=inputCorreo()
                pass
            else:
                read_delayed("Ingresa un comando válido.")
                confirm=input("¿Es correcto?(y/n)")
            
        email=emailserv[0]
        password=emailserv[1]
        sender=emailserv[2]
        
        emailservicefile=f'''
class emailservice:
    email='{email}'
    password='{password}'
    receiver='{sender}'
'''     

        match(os.path.isdir(root)):
            case True:
                pass
            case False:
                os.mkdir(root)

        with open(f'{emailcon}', 'w') as emailfile:
            for line in emailservicefile:
                emailfile.write(line)
            
        read_delayed("Creación de sistema envío de correo creado exitosamente.")
    except KeyboardInterrupt:
        read_delayed("Saliendo...")

            
### MAIN
try:
    if (rootvalidation == True) and (dbexists or emailconexists or conexists == True):
        read_delayed("Parece que ya tienes archivos creados para la conexión.")
        read_delayed("Archivos encontrados en: ")
        if dbexists is True:
            read_delayed(f'> {dbfileservice}')
        if emailconexists is True:
            read_delayed(f'> {emailcon}')
        if conexists is True:
            read_delayed(f'> {connection}')

        selectiontrue=True
        while selectiontrue:    
            read_delayed("Escribe 1 si deseas revisar los contenidos o 2 si deseas reescribir y/o crear sus contenidos")
            existselection=input('Tu selección: ')
            if existselection == '1':
                if dbexists is True:
                    read_delayed(f"Archivo encontrado en: {dbfileservice}")
                    with open(dbfileservice, "r") as file1:
                        read_delayed(file1.read())

                elif dbexists is False:
                    read_delayed(f"El archivo {dbfileservice} no existe")
                
                if emailconexists is True:
                    read_delayed(f"Archivo encontrado en: {emailcon}")
                    with open(emailcon, "r") as file2:
                        read_delayed(file2.read())
                elif emailconexists is False:
                    read_delayed(f"Archivo {emailcon} no existe")
                
                if conexists is True:
                    read_delayed(f"Archivo encontrado en: {connection}")
                    with open(connection, "r") as file3:
                        read_delayed(file3.read())
                elif conexists is False:
                    read_delayed(f"El archivo {connection} no existe")

            elif existselection == '2':
                creacionDBFiles()
                creacionEmailFiles()
                selectiontrue=False
            
            else:
                read_delayed("Selección invalida, vuelve a ingresarla.")
                existselection=input('Tu selección: ')
            
                
    elif rootvalidation is True and (dbexists or emailconexists or conexists is False):
        start=True
        while start:
            read_delayed('Parece que el directorio existe, pero no tiene contenidos.')
            read_delayed('Escriba 1 si desea crearlos o escriba 2 si desea salir')
            createfiles = input('Su selección: ')
            if createfiles == '1':
                creacionDBFiles()
                creacionEmailFiles()
                start=False
            elif createfiles == '2':
                read_delayed("Saliendo.....")
                sys.exit()
            else:
                read_delayed("Comando desconocido, por favor escriba denuevo su selección.")
                createfiles = input('Su selección: ')
                
                
        match(rootvalidation):
            case True:
                pass
            case False:
                os.mkdir(root)
    
    else:
        creacionDBFiles()
        creacionEmailFiles()
except KeyboardInterrupt:
    read_delayed("Saliendo...")
    
