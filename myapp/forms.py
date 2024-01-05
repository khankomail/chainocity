from django.forms import models
from. models import User,Profile,Code,Plan

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




class UpdateUserForm(forms.ModelForm):
  
  password = None

  class Meta:

    model=User
    fields=['username','email']
    exclude=['password1','password2',]


class UpdateProfileForm(forms.ModelForm):

  profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file'}))

  class Meta:

    model = Profile
    fields = ['profile_pic',]



class CheckoutForm(forms.Form):
    ADDRESS_MAX_LENGTH = 255
    PHONE_NUMBER_MAX_LENGTH = 11

    PAYMENT_CHOICES = [
        ('easypaisa', 'EasyPaisa'),
        ('jazzcash', 'JazzCash'),
        ('cashondelivery', 'Cash On Delivery'),
    ]

    address = forms.CharField(max_length=ADDRESS_MAX_LENGTH, widget=forms.TextInput(attrs={'placeholder': 'Enter your address'}))
    phone_number = forms.CharField(max_length=PHONE_NUMBER_MAX_LENGTH, widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'}))
    payment_type = forms.ChoiceField(choices=PAYMENT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # Add other fields as needed

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        # Add any custom validation for phone number
        return phone_number
    
    

