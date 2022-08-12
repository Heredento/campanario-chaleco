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
    path('toSignup/', views.createUser, name='tosignup'),
    path('toSignin/', views.logUser, name='tosignin'),
    path('toLogout/', views.logoutUser, name='tologout'),
    path('toValidate/', views.validateUser, name='tovalidate'),
    
    ## Eventos
    path('uploadFile/', views.uploadFile, name='uploadFile'),
    path('createEvent/', views.createEvent, name='createEvent'),
    path('deleteEvent/', views.deleteEvent, name='deleteEvent'),
    path('deleteSong/', views.deleteSong, name='deleteSong'),
    path('recoverSong/', views.recoverSong, name='recoverSong'),

    
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

