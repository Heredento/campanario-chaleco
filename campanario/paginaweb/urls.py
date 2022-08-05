from django.urls import path
from . import views

urlpatterns = [
    
    ## Definición de páginas
    path('', views.signin, name='signupblank'),
    path('signup/', views.signup, name='signup'),
    # path('test/', views.createtest, name='createtest'),
    path('signin/', views.signin, name='signin'), 
    path('registrated/', views.registrated, name='registrated'),
    path('validate/', views.validate, name='validate'),
    path('credits/', views.credits, name='credits'),
    
    path('events/', views.eventspage, name='eventspage'), 
    path('config/', views.configpage, name='configpage'),
    
    
    ## Métodos post 
    path('toSignup/', views.createUser, name='tosignup'),
    path('toSignin/', views.logUser, name='tosignin'),
    path('toLogout/', views.logoutUser, name='tologout'),
    path('toValidate/', views.validateUser, name='tovalidate'),
    ]

