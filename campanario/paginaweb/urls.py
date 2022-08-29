from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Definición de paginas
        
    ## Formulario
    path('', views.signin, name='signupblank'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'), 
    path('registrated/', views.registrated, name='registrated'),
    path('validate/', views.validate, name='validate'),
    path('credits/', views.credits, name='credits'),

    ## Eventos    
    path('events/', views.eventspage, name='eventspage'), 
    path('config/', views.configpage, name='configpage'),
    
    
    # Métodos post
    ## Formulario
    path('tosignup/', views.createUser, name='tosignup'),
    path('tosignin/', views.logUser, name='tosignin'),
    path('tologout/', views.logoutUser, name='tologout'),
    path('tovalidate/', views.validateUser, name='tovalidate'),
    
    ## Eventos
    path('fileupload/', views.uploadFile, name='uploadFile'),
    path('eventcreate/', views.createEvent, name='createEvent'),
    path('eventremove/', views.deleteEvent, name='deleteEvent'),
    path('songremove/', views.deleteSong, name='deleteSong'),
    path('songrecover/', views.recoverSong, name='recoverSong'),
    path('changehour/', views.change_hour, name='change_hour'),

    
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

