from datetime import datetime
from time import sleep
import os, sys, threading, pytz, time
from django.forms import models
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .apps import handleFile, saveFile, sendAuthEmail, generateCode, getNowDate
from .apps import recoverFileSong, listEvents, saveFileBackup, deleteFile
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required  
# https://www.geeksforgeeks.org/datetimefield-django-models/

connection = os.path.join(os.path.expanduser('~'), '.campanario')
sys.path.append(connection)
sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.getcwd(), 'funciones/'))
import fix_hour
from connection import cur
from emailcon import emailservice
from . import models
from datetime import datetime

server_active = models.ClockInformation.objects.filter(name='server_active')
clock_state = models.ClockInformation.objects.filter(name='change_hour')
music_state = models.ClockInformation.objects.filter(name='play_songs')



def input_time(object, hour_input, minute_input):
    print(hour_input, minute_input)
    object.is_active=True
    object.save()
    fix_hour.cambiarhora(hour_input, minute_input)
    object.is_active=False
    object.save()

## Paginas web inicial
def signin(request):
    contenido={
        'error': False,
        'registrado':False,
        'existe': True}
    template = loader.get_template('formulario/auth_login.html')
    return HttpResponse(template.render(contenido, request))

def signup(request):
    template = loader.get_template('formulario/auth_register.html')
    contenido={
        'registered': False,
        'error': False,
        'passwordError':False,
    }
    return HttpResponse(template.render(contenido, request))

def registrated(request):
    template = loader.get_template('formulario/auth_registrated.html')
    contenido={
        'verificado': False,
        'correo': ''
    }
    return HttpResponse(template.render(contenido, request))

def validate(request):
    template = loader.get_template('formulario/auth_validate.html')
    contenido={
        'errorAuth':False,
        'error': False,
        'success': False,
    }
    return HttpResponse(template.render(contenido, request))

def credits(request):
    template = loader.get_template('formulario/auth_credits.html')
    contenido={}
    return HttpResponse(template.render(contenido, request))

@login_required(login_url='/')
def eventspage(request):
    events = models.events_list.objects.all()
    filesong = models.events_files.objects.all()
    
    songs_state = True if not filesong else False
    contenido={
    'noSongs': songs_state,
    'events': events,
    'songs': filesong,
    'state': "d",
    }

    template = loader.get_template('eventos/event_add.html')
    return HttpResponse(template.render(contenido, request))

@login_required(login_url='/')
def configpage(request):
    events = models.events_files.objects.all()
    backups  = models.events_backups.objects.all()
    clock_state = models.ClockInformation.objects.filter(name='change_hour')
    
    
    
    if len(clock_state) == 0:
        ch = models.ClockInformation(
                name = 'change_hour',
                is_active = True,)
        ch.save()
    
    if len(clock_state) >= 2:
        clock_state.delete()
        ch = models.ClockInformation(
                name = 'change_hour',
                is_active = False,)
        ch.save()
        
    if len (clock_state) == 1:
        change_state = clock_state[0].is_active
        
    template = loader.get_template('eventos/event_config.html')
    contenido={
        'timeDisable':change_state,
        'fileIsValid': True,
        'successfulUpload': False,
        'songname': '',
        'events': events,
        'backups': backups,
    }
    return HttpResponse(template.render(contenido, request))

### Métodos post
def createUser(request):
    form = UserCreationForm()
    if (request.method=='POST'):
        
        # username = ''.join(request.POST['username'])
        # email = ''.join(request.POST['email'])
        # pass1 = ''.join(request.POST['password1'])
        # pass2 = ''.join(request.POST['password2'])
        
        
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            template = loader.get_template('formulario/auth_register.html')
            contenido={
            'registered': False,
            'error': False,
            'passwordError':True,}
            return HttpResponse(template.render(contenido, request))
        else:
            form = CreateUserForm(request.POST)
            if form.is_valid():
                auth_create=models.auth_code(
                    username=username,
                    email=email,
                    code=generateCode(),
                    toverify=True
                )
                auth_create.save()
                form.save()
                today = datetime.now(pytz.timezone('Etc/GMT+6'))
                sendEmail = threading.Thread(
                    target=sendAuthEmail, 
                    name=f"AuthenticationEmail: {today}", 
                    args=(emailservice.receiver, email, username))
                
                try:
                    sendEmail.start()
                except RuntimeError as re:
                    print("Ha sucedido un problema al enviar el correo.")
                    print(f"RuntimeError: {re}")
                    
                template = loader.get_template('formulario/auth_registrated.html')
                context = {
                    'verificado': True, 
                    'correo': email,}
                return HttpResponse(template.render(context, request))
            
            else:
                username_existence = models.auth_code.objects.filter(username=username).first()
                email_existence = models.auth_code.objects.filter(email=email).first()
                
                
                
                if username_existence != None or email_existence != None:
                    template = loader.get_template('formulario/auth_register.html')
                    contenido={
                    'registered': True,
                    'error': False,
                    }
                    return HttpResponse(template.render(contenido, request))
                
                else:
                    template = loader.get_template('formulario/auth_register.html')
                    contenido={
                    'registered': False,
                    'error': True,
                    }
                    return HttpResponse(template.render(contenido, request))

def logUser(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        username_existence = models.auth_code.objects.filter(username=username).first()
        email_existence = models.auth_code.objects.filter(email=username).first()
        if username_existence != None or email_existence != None:
            if username_existence is not None:
                user_model = models.auth_code.objects.filter(username=username).first()
                
            elif email_existence is not None:
                user_model = models.auth_code.objects.filter(email=username).first()


            if user_model.toverify == True:
                template = loader.get_template('formulario/auth_login.html')
                contenido={
                    'registrado':True,
                    'error': False,}
                return HttpResponse(template.render(contenido, request))
                

            elif user_model.toverify == False:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("/events")


                else:
                    template = loader.get_template('formulario/auth_login.html')
                    contenido={
                        'error': True, 
                        'registrado': False,
                        'existe': True,
                    }
                    return HttpResponse(template.render(contenido, request))
        else:
        
            template = loader.get_template('formulario/auth_login.html')
            context = {
                'error': False, 
                'registrado': False,
                'existe': False,
            }
            return HttpResponse(template.render(context, request))
            
def validateUser(request):
    
    if (request.method=='POST'):
        email=''.join(request.POST['email'])
        codigo=''.join(request.POST['codigo'])
        
        
        query=f"select toverify from paginaweb_auth_code where email='{email}';"
        cur.execute(query)
        if (len(cur.fetchall()) > 0): ## Existe?
            ## Sí existe
            querycode=f"select code from paginaweb_auth_code where email='{email}';"
            cur.execute(querycode)
            code = cur.fetchall()[0][0]
            if codigo == code:
                get=models.auth_code.objects.get(email=email)
                get.toverify=False
                get.save()
                
                template = loader.get_template('formulario/auth_validate.html')
                contenido={
                    'errorAuth':False,
                    'error': False,
                    'success': True,
                }
                return HttpResponse(template.render(contenido, request))
            
            elif codigo != code:
                template = loader.get_template('formulario/auth_validate.html')
                contenido={
                    'errorAuth':True,
                    'error': False,
                    'success': False,
                }
                return HttpResponse(template.render(contenido, request))
                
            
        else:
            template = loader.get_template('formulario/auth_validate.html')
            contenido={
                'errorAuth':False,
                'error': True,
                'success': False,
            }
            return HttpResponse(template.render(contenido, request))

def logoutUser(request):
    logout(request)
    return redirect('/')

def createEvent(request):
    if request.method=='POST':
        name= request.POST.get('name')
        selection = request.POST.get('selection')
        time = request.POST.get('time')
        week = request.POST.get('week', False) 
        song = request.POST.get('song')
        
        currentyear = True if request.POST.get('currentyear', False) else False
        
        events = listEvents(name, selection, time, week, song, currentyear)
        
        event=models.events_list(
            name = events[0],
            selection = events[1],
            time = events[2],
            week = events[3],
            song = events[4],
            currentyear = events[5],
            date = events[6],
        )
        event.save()
              
        return redirect("/events/")
    
def deleteEvent(request):
    id = list(request.POST.keys())[1]
    event=models.events_list.objects.get(pk=id)
    event.delete()
    return redirect("/events/")


def change_hour(request):
    if request.method == 'POST':
        time=request.POST.get('relojhora', False)
        if time == "":
            return redirect("/config/")
        
        hora, minuto = int(time[:-3]), int(time[3:])
        print(f'{time},{hora}:{minuto} ')
        active = models.ClockInformation.objects.filter(name='change_hour')
        
        clock_change_state = active[0] 
        today = datetime.now(pytz.timezone('Etc/GMT+6'))
        fix_hour = threading.Thread(
            target=input_time, 
            name=f"FixClockTime{today}", 
            args=(clock_change_state, hora, minuto))
        fix_hour.start()

        
            
        return redirect("/config/")
    else:
        return redirect("/config/")

def uploadFile(request):
    if request.method=='POST':
            try:
                file=request.FILES['file'].readlines()
            except:
                template = loader.get_template('eventos/event_config.html')
                events = models.events_files.objects.all()
                backups  = models.events_backups.objects.all()
                clock_state = models.ClockInformation.objects.filter(name='change_hour')
                change_state = clock_state[0]
                contenido={
                    'timeDisable':change_state.is_active,
                    'fileIsValid': False,
                    'successfulUpload': False,
                    'songname': '',
                    'events': events,
                    'backups': backups
                }
                return HttpResponse(template.render(contenido, request))
            
            if handleFile(file)==True: ## El archivo no es válido
                events = models.events_files.objects.all()
                backups  = models.events_backups.objects.all()
                template = loader.get_template('eventos/event_config.html')
                clock_state = models.ClockInformation.objects.filter(name='change_hour')
                change_state = clock_state[0]
                contenido={
                    'timeDisable':change_state.is_active,
                    'fileIsValid': False,
                    'successfulUpload': False,
                    'songname': '',
                    'events': events,
                    'backups': backups
                }
                return HttpResponse(template.render(contenido, request))
                
            else: ## El archivo es válido
                savedfile=saveFile(file)
                backupfile=saveFileBackup(file)
                song=models.events_files(
                    filename=savedfile[0],
                    title=savedfile[1],)
                song.save()
                backupsong=models.events_backups(
                    filename=backupfile[0],
                    title=backupfile[1],
                    creationdate=getNowDate(),)
                backupsong.save()
                clock_state = models.ClockInformation.objects.filter(name='change_hour')
                change_state = clock_state[0]
                event = models.events_files.objects.all()
                backup  = models.events_backups.objects.all()
                template = loader.get_template('eventos/event_config.html')
                contenido={
                    'timeDisable':change_state.is_active,
                    'fileIsValid': True,
                    'successfulUpload': True,
                    'songname': savedfile[1],
                    'events': event,
                    'backups': backup
                }
                return HttpResponse(template.render(contenido, request))

def deleteSong(request):
    try:
        id = list(request.POST.keys())[1]
        filename=models.events_files.objects.get(pk=id)
        deleteFile(filename.filename)
        filename.delete()

        return redirect("/config/")
    
    except Exception:
        return redirect("/config/")

def recoverSong(request):
    id = list(request.POST.keys())[1]
    song=models.events_backups.objects.get(pk=id)
    
    print(song.filename)
    recover = recoverFileSong(song.filename)
    event=models.events_files(
        filename=recover,
        title=song.title,
    )
    event.save()

    return redirect("/config/")
    


        


