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
    path('registrar/', views.createUser, name='createuser'),
    path('entrar/', views.logUser, name='loguser'),
    path('logout/', views.logoutUser, name='logout'),
    
    
    # path('login', views.login, name='login'),
    ]

    # Enlaces de métodos post
    # path('campanario/signin/', views.register, name='register'),
    # path('campanario/signup/', views.login, name='login'),
    # path('campanario/registrated/', views.registered, name='registered'),
    # path('campanario/validate/', views.verify, name='verify'),
