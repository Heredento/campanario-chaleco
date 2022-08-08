import os, sys, os.path, ipaddress, re
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

## Get versions
getversion=sys.version_info
pyversion3=int(getversion[0])
pyversion_10=int(getversion[1])
pytrue=True
gitisinstalled=False

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
    gitisinstalled=True

except Exception:
    gitisinstalled=False

while(pyversion_10):
    if (pyversion3 >= 3 and 10 >= pyversion_10) and gitisinstalled == True:
        print("Requisitos superados.\n")
        pyversion_10=False
    else:
        print("Parece que no cumples los siguientes requisitos:")
        if gitisinstalled == False:
            print("Se requiere que esté git instalado...")
            print("Se puede instalar desde https://git-scm.com/downloads")
        if pyversion3 >= 3 and 10 >= pyversion_10:
            print("Se requiere una versión de python más reciente...")
            print("La versión de python debe ser mayor o igual a 3.10")
            print("Puedes descargar la última versión desde https://www.python.org/downloads/")
        sys.exit()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def creacionDBFiles(): 
    try:
        print("\n> CONFIGURACIÓN DE BASE DE DATOS DEL CAMPANARIO <")
        print("En este momento vamos a declarar información que se usará en adelante para el campanario.")
        print("Presiona CTRL + C para pasar a la creación de correos.")
        print("Vuelve a presionar CTRL + C para CANCELAR.") 
        print("Cuando '(default)' sea mencionado significa que lo puedes dejar en blanco y tomará el mencionado")
        print("ESTA INFORMACIÓN ES IMPORTANTE, POR FAVOR GUARDALA\n")
        
        def InputArchivos():
            name = input("Escribe el nombre de la base de datos: ")
            nametrue=True
            while(nametrue):
                if name=='':
                    print("El nombre no puede estar vacío")
                    name = input("Escribe el nombre de la base de datos: ")
                else:
                    nametrue=False
            usertrue=True
            user = input("Escribe de el usuario dueño de la base de datos: ")
            while(usertrue):
                if user=='':
                    print("El nombre no puede estar vacío")
                    user = input("Escribe el nombre de la base de datos: ")
                else:
                    usertrue=False

            password = input("Escribe una contraseña mayor a 8 caracteres: ")
            passtrue=True
            while(passtrue):
                if 8 > len(password):
                    print("La contrasea es muy corta")
                    password = input("Escribe una contraseña mayor a 8 caracteres: ")
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
                    print("Host ingresado es invalido")
                    host = input("Escribe un host válido (default: localhost): ")
                    
                else: 
                    hosttrue=False
                
            port = input("Ingresa el puerto(default: 5432): ")
            porttrue=True
            while(porttrue):
                if port == '':
                    port='5432'
                    porttrue=False
                elif int(port) > 65535 or 0 or 65535:
                    print("Puerto ingresado no es válido")
                    port=input("Ingresa un puerto válido (default: 5432): ")
                elif int(port) < 65535:
                    port=port
                    porttrue=False
                else:
                    porttrue=True
            
            print("La información es la siguiente: ")
            dbservice= (f'''
class dbservice:
    name ='{name}'
    user ='{user}'
    password= '{password}'
    host =  '{host}'
    port = '{port}'
                ''')
            print(dbservice)
            
            return name, user, password, host, port
        

        inputs = InputArchivos()
        
        
        confirm=True
        while(confirm):
            confirmation = input("¿Es correcto?(y/n) ")
            if confirmation=='y':
                print(f"El archivo y sus dependencias se crearán en {root}")
                print("Dependencias:")
                print(f"> {dbfileservice}")
                print(f"> {connection}")
                confirm=False
            elif confirmation=='n':
                inputs = InputArchivos()

            else:
                print("Ingresaste algo equivocado...\n")
                inputs = InputArchivos()
        
        
        
        
        name = inputs[0]
        user = inputs[1]
        password = inputs[2]
        host = inputs[3]
        port = inputs[4]
        
        dbservice= (f'''
class dbservice:
    name ='{name}'
    user ='{user}'
    password= '{password}'
    host =  '{host}'
    port = '{port}'
                ''')
        if (os.path.isdir(root) == True):
            dbservicecreation=open(f'{dbfileservice}', 'w')
            for line in dbservice:
                dbservicecreation.write(line)
            dbservicecreation.close()
        elif os.path.isdir(root) == False:
            os.mkdir(root)
            dbservicecreation=open(f'{dbfileservice}', 'w')
            for line in dbservice:
                dbservicecreation.write(line)
            dbservicecreation.close()

            
    
        conection=f'''
import psycopg2 
from db import dbservice
try:
    connection=psycopg2.connect(
        host=dbservice.host,
        user=dbservice.user,
        password=dbservice.password,
        database=dbservice.name,
    cur = connection.cursor()    
except Exception as ex:
    print(ex)
        '''
        
        
        dbservicecreation=open(f'{connection}', 'w')
        for line in conection:
            dbservicecreation.write(line)
        dbservicecreation.close()
        
        
        print("Configuración para la base de datos creada exitosamente!")
        
        

    except KeyboardInterrupt:
        try:
            os.remove(dbfileservice)
            os.remove(emailcon)
            os.remove(connection)
        except Exception:
            pass
        finally:
            try:
                os.rmdir(root)
            except Exception:
                pass

def creacionEmailFiles():
    try: 
        print("\n> CREACIÓN DE SISTEMA DE ENVÍO DE CORREOS (NO-REPLY) <")
        print("Antes de empezar a ingresar la información, asegurate que la contraseña sea de aplicación.")
        print("Porfavor usar una cuenta de google. Puedes abrir el siguiente enlace donde explica como obtenerla")
        print("Placeholder: https://myaccount.google.com/apppasswords")
        
        def inputCorreo():
            sendertrue=True
            while sendertrue:
                sender = input("Ingresa el correo que enviará a terceros correos: ")
                validation=validateemail(sender)
                if validation == True:
                    sendertrue=False
                elif validation == False:
                    sender = input("Ingresa un correo válido que enviará a terceros: ")
                    validation=validateemail(sender)
            passtrue=True
            while passtrue:
                password=input("Ingresa la contraseña formateada para app de google: ")
                if 7 > len(password):
                    password = input("Ingresa una contraseña válida: ")
                elif len(password) >= 8:
                    passtrue=False
            receivertrue=True
            while receivertrue:
                receiver=input("Ingresa el correo que estará reciviendo los códigos de verificación: ")
                if validateemail(receiver) == True:
                    receivertrue=False
                elif validateemail(receiver) == False:
                    receiver = input("Ingresa un correo válido que recibirá los códigos: ")

                        
            print("La información es la siguiente: ")
                
            emailservicefile=f'''
class emailservice:
    email='{sender}'
    password='{password}'
    receiver='{receiver}'
            '''     
            print(emailservicefile)
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
                print("Ingresa un comando válido.")
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
        
        if (os.path.isdir(root) == True):
                emailservicecreation=open(f'{emailcon}', 'w')
                for line in emailservicefile:
                    emailservicecreation.write(line)
                emailservicecreation.close()
                
        elif os.path.isdir(root) == False:
            os.mkdir(root)
            emailservicecreation=open(f'{emailcon}', 'w')
            for line in emailservicefile:
                emailservicecreation.write(line)
            emailservicecreation.close()
            
        print("Creación de sistema envío de correo creado exitosamente.")
    except KeyboardInterrupt:
        try:
            os.remove(dbfileservice)
            os.remove(emailcon)
            os.remove(connection)
        except Exception:
            pass
        finally:
            try:
                os.rmdir(root)
            except Exception:
                pass
            
### MAIN
try:
    if (rootvalidation == True) and (dbexists or emailconexists or conexists == True):
        print("Parece que ya tienes archivos creados para la conexión.")
        print("Archivos encontrados en: ")
        if dbexists == True:
            print(f'> {dbfileservice}')
        if emailconexists == True:
            print(f'> {emailcon}')
        if conexists == True:
            print(f'> {connection}')

        selectiontrue=True
        while selectiontrue:    
            print("Escribe 1 si deseas revisar los contenidos o 2 si deseas reescribir y/o crear sus contenidos")
            existselection=input('Tu selección: ')
            if existselection == '1':
                if dbexists == True:
                    print(f"Archivo encontrado en: {dbfileservice}")
                    file1=open(dbfileservice, "r")
                    lines = file1.read()
                    print(lines)
                    file1.close()
                elif dbexists == False:
                    print(f"El archivo {dbfileservice} no existe")
                if emailconexists == True:
                    print(f"Archivo encontrado en: {emailcon}")
                    file2=open(emailcon, "r")
                    lines = file2.read()
                    print(lines)

                    file2.close()
                elif emailconexists == False:
                    print(f"Archivo {emailcon} no existe")
                if conexists == True:
                    print(f"Archivo encontrado en: {connection}")
                    file3=open(connection, "r")
                    lines = file3.read()
                    print(lines)
                    file3.close()
                elif conexists == False:
                    print(f"El archivo {connection} no existe")

            elif existselection == '2':
                creacionDBFiles()
                creacionEmailFiles()
                selectiontrue=False
            
            else:
                print("Selección invalida, vuelve a ingresarla.")
                existselection=input('Tu selección: ')
            
                
    elif rootvalidation == True and (dbexists or emailconexists or conexists == False):
        start=True
        while start:
            print('Parece que el directorio existe, pero no tiene contenidos.')
            print('Escriba 1 si desea crearlos o escriba 2 si desea salir')
            createfiles = input('Su selección: ')
            if createfiles == '1':
                creacionDBFiles()
                creacionEmailFiles()
                start=False
            elif createfiles == '2':
                print("Saliendo.....")
                sys.exit()
            else:
                print("Comando desconocido, por favor escriba denuevo su selección.")
                createfiles = input('Su selección: ')
                
                
        
        try:
            os.mkdir(root)
            print(root)
        except Exception as ex:
            print(f'Excepción: {ex}')
            pass
    
    else:
        creacionDBFiles()
        creacionEmailFiles()
except KeyboardInterrupt:
    try:
        os.remove(dbfileservice)
        os.remove(emailcon)
        os.remove(connection)
        os.rmdir(root)
    except Exception:
        pass

