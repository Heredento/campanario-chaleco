from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.eventspage, name='eventspage'), 
    path('admin/', views.configpage, name='configpage'),
    ]

    # Enlaces de métodos post
    # path('campanario/signin/', views.register, name='register'),
    # path('campanario/signup/', views.login, name='login'),
    # path('campanario/registrated/', views.registered, name='registered'),
    # path('campanario/validate/', views.verify, name='verify'),
