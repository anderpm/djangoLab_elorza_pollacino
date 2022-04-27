
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    user= forms.CharField(label='Izena',max_length=20,required=True)
    pass1=forms.CharField(label='Pasahitza',widget=forms.PasswordInput, required=True)
    pass2=forms.CharField(label='Errepikatu pasahitza',widget=forms.PasswordInput, required=True)
    

class LoginForm(forms.Form):
    user = forms.CharField(label='Izena',max_length=20,required=True)
    password=forms.CharField(label='Pasahitza',widget=forms.PasswordInput, required=True)
