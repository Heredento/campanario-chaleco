from django.db.models import F
from django.template import loader
import bcrypt #https://www.geeksforgeeks.org/hashing-passwords-in-python-with-bcrypt/
from django.contrib.auth.forms import UserCreationForm
from django.urls.resolvers import re
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from . import models
import os, sys, secrets, string
connection = os.path.expanduser('~') + '/.campanario'
sys.path.append(connection)
from connection import cur

## Funciones internas de utilidad

def generateCode():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(6))  # for a 20-character password
    return password


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
        'error': False
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
    template = loader.get_template('eventos/event_add.html')
    contenido={
        'error': False,
        'registrado':True,
    }
    return HttpResponse(template.render(contenido, request))

@login_required(login_url='/')
def configpage(request):
    template = loader.get_template('eventos/event_config.html')
    contenido={
        'error': False
    }
    return HttpResponse(template.render(contenido, request))


### Métodos post
def createUser(request):
    form = UserCreationForm()
    
    if (request.method=='POST'):
        username = ''.join(request.POST['username'])
        email = ''.join(request.POST['email'])
        print(email)
        form = CreateUserForm(request.POST)
        if form.is_valid():
            print("Válido")
            auth_create=models.auth_code(
                username=username,
                email=email,
                code=generateCode(),
                toverify=True
            )
            auth_create.save()
            form.save()
            
            template = loader.get_template('formulario/auth_registrated.html')
            context = {
                'error': True, 
                'registered': False,
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
                return HttpResponse(template.render(contenido, request))
                

            
            ## Ya puede accesar
            elif res== False:
                user = authenticate(request, username=username, password=password)
                print(username, password)
                if user is not None:
                    login(request, user)
                    # return redirect('eventos/event_add.html')
                    template = loader.get_template('eventos/event_add.html')
                    contenido={}
                    return HttpResponse(template.render(contenido, request))

                else:
                    template = loader.get_template('formulario/auth_login.html')
                    contenido={
                        'error': True, 
                        'registrado': False,
                        'existe': True,
                    }
                    return HttpResponse(template.render(contenido, request))
        else:
            print("no existe")
        
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



