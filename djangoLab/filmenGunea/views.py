from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User



def index(request):
    return render(request, 'filmenGunea/index.html')

def register(request):
    if request.method=='POST':
        erabil = request.POST['user']
        pasahitza1 = request.POST['pass1']
        pasahitza2 = request.POST['pass2']
        if pasahitza1==pasahitza2:
            user = authenticate(username=erabil,password=pasahitza1)
            if user is None:
              us=User.objects.create_user(erabil,email=None,password= pasahitza1)
              us.save()
              redirect('')
            
    else:
        form=RegisterForm()
            
    return render(request, 'filmenGunea/register.html',{'form':form})

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            a=1
    else:
        form=LoginForm()
    
    return render(request, 'filmenGunea/login.html',{'form':form})

def filmakIkusi(request):
    return render(request, 'filmenGunea/filmakIkusi.html')

def bozkatu(request):
    return render(request, 'filmenGunea/bozkatu.html')

def zaleak(request):
    return render(request, 'filmenGunea/zaleak.html')