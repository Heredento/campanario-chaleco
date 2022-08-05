from django.db import close_old_connections, models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

 
class auth_code(models.Model):
    username = models.CharField (max_length=150)
    email = models.CharField (max_length=254)
    code = models.CharField (max_length=6)
    toverify = models.BooleanField(default=True)
    
    
class events_list(models.Model):
    name = models.CharField (max_length=50)
    selection = models.CharField (max_length=2)
    time = models.CharField (max_length=20)
    week = models.CharField (max_length=20, blank=True)
    song = models.CharField (max_length=4)  # Hasta 9999 canciones agregables por cuatro digitos
    currentyear = models.BooleanField(default=False)
    
