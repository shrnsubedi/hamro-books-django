from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
  class Meta(UserCreationForm):
    model=CustomUser
    fields=("username","email",'phone','mobile_no','address_1','address_2','address_3')

class CustomUserChangeForm(UserChangeForm):
  class Meta:
    model=CustomUser
    fields=("username","email",'phone','mobile_no','address_1','address_2','address_3')