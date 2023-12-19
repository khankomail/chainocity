from django.forms import models
# from. models import User

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput

from django import forms

# class Userform(ModelForm):

#     class Meta:
#         pass

class CreateUserForm(UserCreationForm):
  class Meta:

    model=User
    fields = ['username','email', 'password1','password2']


class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())