
from django import forms

class RegisterForm(forms.Form):
    user= forms.CharField(max_length=20,required=True)
    pass1=forms.CharField(widget=forms.PasswordInput, required=True)
    pass2=forms.CharField(widget=forms.PasswordInput, required=True)

class LoginForm(forms.Form):
    user = forms.CharField(max_length=20,required=True)
    password=forms.CharField(widget=forms.PasswordInput, required=True)
