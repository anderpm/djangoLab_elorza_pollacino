from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm


def index(request):
    return render(request, 'filmenGunea/index.html')

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            a=1
    else:
        form=RegisterForm()
            
    return render(request, 'filmenGunea/register.html',{'form':form})

def login(request):
    
    return render(request, 'filmenGunea/login.html')

def filmakIkusi(request):
    return render(request, 'filmenGunea/filmakIkusi.html')

def bozkatu(request):
    return render(request, 'filmenGunea/bozkatu.html')

def zaleak(request):
    return render(request, 'filmenGunea/zaleak.html')