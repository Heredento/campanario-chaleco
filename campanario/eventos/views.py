from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

def eventspage(request):
    template = loader.get_template('eventos/event_add.html')
    contenido={
        'error': False,
        'registrado':True,
    }
    return HttpResponse(template.render(contenido, request))

def configpage(request):
    template = loader.get_template('eventos/event_config.html')
    contenido={
        'error': False
    }
    return HttpResponse(template.render(contenido, request))