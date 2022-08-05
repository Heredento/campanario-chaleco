from django.template import loader
import bcrypt #https://www.geeksforgeeks.org/hashing-passwords-in-python-with-bcrypt/
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from . import models #authfunctions, db


## Paginas web inicial
def signin(request):
    template = loader.get_template('formulario/auth_login.html')
    contenido={
        'error': False,
        'registrado':False,
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
        'verificado': False,
        'correo': ''
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
        email = ''.join(request.POST['email'])
        print(email)
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            template = loader.get_template('formulario/auth_registrated.html')
            context = {
                'error': True, 
                'registered': False,
            }
            return HttpResponse(template.render(context, request))
            # print(form)
        else:            
            template = loader.get_template('formulario/auth_validate.html')
            context = {
                'verificado': True, 
                'correo': email,
            }
            return HttpResponse(template.render(context, request))

def logUser(request):
    if (request.method == 'POST'):
        username = ''.join(request.POST['username'])
        password = ''.join(request.POST['password'])
        user = authenticate(request, username=username, password=password)
        print(username, password)
        
        if user is not None:
            login(request, user)
            template = loader.get_template('eventos/event_add.html')
            contenido={}
            return HttpResponse(template.render(contenido, request))
        
        else:
            template = loader.get_template('formulario/auth_login.html')
            context = {
                'error': True, 
                'registrado': False,
            }
            return HttpResponse(template.render(context, request))
            
            
def logoutUser(request):
    logout(request)
    return redirect('/')



