from django.db import close_old_connections, models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

 



# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'email',
#             'password1',
#             'password2',
#         ]
