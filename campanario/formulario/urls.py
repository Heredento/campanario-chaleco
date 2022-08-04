from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.signin, name='signin'), 
    path('signup/', views.signup, name='signup'),
    path('registrated/', views.registrated, name='registrated'),
    path('validate/', views.validate, name='validate'),
    path('credits/', views.credits, name='credits'),
    
  
    ]

    # Enlaces de métodos post
    # path('campanario/signin/', views.register, name='register'),
    # path('campanario/signup/', views.login, name='login'),
    # path('campanario/registrated/', views.registered, name='registered'),
    # path('campanario/validate/', views.verify, name='verify'),
