import os, sys, secrets, string, socket, smtplib, ssl, datetime
import itertools as it
cwd=f"{os.getcwd()}"
connection = os.path.join(os.path.expanduser('~'), '.campanario')
sys.path.append(connection)
sys.path.append(cwd)
from connection import cur
from emailcon import emailservice
from email.message import EmailMessage
from django.conf import settings
savefilepath = os.path.join(settings.MEDIA_ROOT, 'songs/')
savefilebackuppath = os.path.join(settings.MEDIA_ROOT, 'backups/')
from datetime import datetime

def capPermutations(s):
    lu_sequence = ((c.lower(), c.upper()) for c in s)
    return [''.join(x) for x in it.product(*lu_sequence)]

def handleFile(file):
    ### Comandos de lista negra
    commands=['alter', 'drop', 'truncate', 'database', 'schema',
              'select', 'dt', ';', 'drop', 'insert', 'fetch', 'lock', 'load', 
              ]
    owo=[]
    for item in commands:
        owo.append(capPermutations(item))
    ## Obtener todas las combinaciones posibles para la lista negrea
    definitivelist = [item for sublist in owo for item in sublist]
    
    try:
        a=0
        titleexists=False
        for line in file:
            line = line.decode("utf-8")
            for repetitions in range(len(definitivelist)):
                if definitivelist[repetitions] in line:
                    print(definitivelist[repetitions])
                    a=a+1
                elif 'title' in line:
                    titleexists=True
                else:
                    a=a+0
        print(a)
        ## No hay inyecciones
        if a == 0 and titleexists == True:
            return False
        ## Existen posible inyecciones
        else:
            return True
        
    except Exception as ex:
        print(ex)

def saveFile(file):
    namenumber=len(os.listdir(savefilepath))
    filename=f'song{namenumber}.py'    
    for line in file:
        line=line.decode("utf-8").replace("\n", "")
        if 'title' in line:
            title = line.replace("title", "").replace("=", "").replace("\r", "").replace('"', '')
        else:
            pass

    song=open(f'{savefilepath}{filename}', 'w')
    for line in file:
        line=line.decode("utf-8").replace("\n", "")
        song.write(line)
    song.close()
    
    return filename, title

def deleteFile(filename):
    os.remove(f'{savefilepath}{filename}')

def recoverFileSong(filename):
    namenumber=len(os.listdir(savefilepath))
    recoverednamefile=f'song{namenumber}.py'  
    recoverfile=f'{savefilepath}{recoverednamefile}'


    song=open(f'{savefilebackuppath}{filename}', 'r')
    lines = song.readlines()
    
    newfile=open(recoverfile, 'w')
    for line in lines:
        newfile.write(line)

    newfile.close()
    song.close()


    return recoverednamefile

def saveFileBackup(file):
    namenumber=len(os.listdir(savefilepath))
    filename=f'song{namenumber}.py'    
    for line in file:
        line=line.decode("utf-8").replace("\n", "")
        if 'title' in line:
            title = line.replace("title", "").replace("=", "").replace("\r", "").replace('"', '')
            continue
        else:
            pass

    song=open(f'{savefilebackuppath}{filename}', 'w')
    for line in file:
        line=line.decode("utf-8").replace("\n", "")
        song.write(line)
    song.close()
    
    return filename, title

def generateCode():
    alphabet = string.ascii_letters + string.digits
    code = ''.join(secrets.choice(alphabet) for i in range(6))
    return code

def sendAuthEmail(toSend, toValidateEmail, toValidateUsername):
    ##Query 
    query=f"select code from paginaweb_auth_code where email='{toValidateEmail}';"
    cur.execute(query)
    code=cur.fetchall()[0][0]
    ## IP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip=s.getsockname()[0]
    getip = f"{ip}:8080/validate"

    ## Correo
    subject = f'Código de validación para {toValidateEmail}'
    body = f'''
    Se ha registrado un nuevo correo en la base de datos del campanario.
    Correo: {toValidateEmail}
    Usuario: {toValidateUsername}

    Su respectivo código de validación es el siguiente:

    > {code}
    
    Por favor hacer llegar el código de verificación al correo del destinatario en caso que se le otorge el permiso de acceso a la página del campanario.
    El código se puede validar en la siguiente dirección:
    http://{getip}
    ''' 
    
    em = EmailMessage()
    em['From'] = emailservice.email
    em['To'] = toSend #emailservice.receiver
    em['Subject'] = subject
    em.set_content(body)

    try:

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(emailservice.email, emailservice.password)
            smtp.sendmail(emailservice.email, emailservice.receiver, em.as_string())
            print("Correo enviado!")
    except Exception as ex:
        print (ex)
        pass

def listEvents(name, selection, time, week, songid, currentyear):
    nombre=name
    idsong=int(songid)
    seleccion=int(selection)
    match(seleccion):
        case 1:
            hour = time
            date=''

        case 2:
            hour = time
            date=''
        case 3:
            hour = time
            date=''

        case 4:
            hour=time[11:]
            date=f"{time[:-12]}-{time[5:-9]}-{time[8:-6]}"
            
        case 5:
            hour=time
            date=''
            week=week
        
        
    match(week):
        case False:
            week=''
            pass
        case other:
            week=week
            pass
    

    return nombre, seleccion, hour, week, idsong, currentyear, date

def getNowDate():
    now = str(datetime.now())
    return now[:-7]
 

