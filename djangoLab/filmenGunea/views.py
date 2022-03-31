from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'filmenGunea/index.html')

def register(request):
    return render(request, 'filmenGunea/register.html')

def login(request):
    return render(request, 'filmenGunea/login.html')

def filmakIkusi(request):
    return render(request, 'filmenGunea/filmakIkusi.html')

def bozkatu(request):
    return render(request, 'filmenGunea/bozkatu.html')

def zaleak(request):
    return render(request, 'filmenGunea/zaleak.html')