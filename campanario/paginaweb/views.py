import os, sys, secrets, string, socket, smtplib, ssl, bcrypt
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
from email.message import EmailMessage
from django.core.files.storage import default_storage
from django.conf import settings


cwd=f"{os.getcwd()}"
connection = os.path.join(os.path.expanduser('~'), '.campanario')
sys.path.append(connection)
sys.path.append(cwd)
from connection import cur
from emailcon import emailservice
from . import models
from datetime import datetime

## Paginas web inicial
def signin(request):
    template = loader.get_template('formulario/auth_login.html')
    contenido={
        'error': False,
        'registrado':False,
        'existe': True
    }
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
    if not filesong:
        contenido={
        'noSongs': True,
        'events': events,
        'songs': filesong,
    }
    else:
        contenido={
        'noSongs': False,
        'events': events,
        'songs': filesong,
    }
    template = loader.get_template('eventos/event_add.html')
    
    return HttpResponse(template.render(contenido, request))

@login_required(login_url='/')
def configpage(request):
    events = models.events_files.objects.all()
    backups  = models.events_backups.objects.all()
    template = loader.get_template('eventos/event_config.html')
    contenido={
        'timeDisable':False,
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
        username = ''.join(request.POST['username'])
        email = ''.join(request.POST['email'])
        pass1 = ''.join(request.POST['password1'])
        pass2 = ''.join(request.POST['password2'])
        if pass1 != pass2:
            template = loader.get_template('formulario/auth_register.html')
            contenido={
            'registered': False,
            'error': False,
            'passwordError':True,
            }
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
                #toSend, toValidateEmail, toValidateUsername
                sendAuthEmail(emailservice.receiver, email, username)
                template = loader.get_template('formulario/auth_registrated.html')
                context = {
                    'verificado': True, 
                    'correo': email,
                }
                
                return HttpResponse(template.render(context, request))
            else:
                queryvalidate = f"select * from paginaweb_auth_code where username='{username}' or email='{username}';"
                cur.execute(queryvalidate)
                res = len(cur.fetchall())
                if res > 0:
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
        username = ''.join(request.POST['username'])
        password = ''.join(request.POST['password'])
        #paginaweb_auth_code
        
        query=f"select toverify from paginaweb_auth_code where username='{username}' or email='{username}';"
        cur.execute(query)
        
        if (len(cur.fetchall()) != 0):
            cur.execute(query)
            res = cur.fetchall()[0][0]
            
            ## Debe ser verificado
            if res == True:
                template = loader.get_template('formulario/auth_login.html')
                contenido={
                    'registrado':True,
                    'error': False,
                }
                return HttpResponseRedirect(template.render(contenido, request))
                

            
            ## Ya puede accesar
            elif res== False:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("/events/")


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
        name= request.POST['name']
        selection = request.POST['selection']
        time = request.POST['time']
        week = request.POST.get('week', False) 
        song = request.POST['song']
        
        currentyear = True if request.POST.get('currentyear', False) else False
        
        events = listEvents(name, selection, time, week, song, currentyear)
        try:
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
            
        except Exception as ex:
            print(ex)   
        return redirect("/events/")
    
def deleteEvent(request):
    id = list(request.POST.keys())[1]
    event=models.events_list.objects.get(pk=id)
    event.delete()
    return redirect("/events/")
        

def changeHour(request):
    template = loader.get_template('eventos/event_config.html')
    contenido={
        'timeDisable': False,
        'fileIsValid': False,
        'successfulUpload': True,
        'songname': '',
        'timeDisable':True,
    }
    return redirect("/config/")

def uploadFile(request):
    if request.method=='POST':
            try:
                file=request.FILES['file'].readlines()
            except:
                template = loader.get_template('eventos/event_config.html')
                events = models.events_files.objects.all()
                backups  = models.events_backups.objects.all()
                contenido={
                    'timeDisable':False,
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
                contenido={
                    'timeDisable':False,
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
                    title=savedfile[1],
                )
                song.save()
                backupsong=models.events_backups(
                    filename=backupfile[0],
                    title=backupfile[1],
                    creationdate=getNowDate(),
                )
                backupsong.save()
                
                event = models.events_files.objects.all()
                backup  = models.events_backups.objects.all()
                template = loader.get_template('eventos/event_config.html')
                contenido={
                    'timeDisable':False,
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
    


        


