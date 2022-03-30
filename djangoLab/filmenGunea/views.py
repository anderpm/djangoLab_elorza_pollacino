from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'filmenGunea/index.html')

def register(request):
    return render(request, 'filmenGunea/register.html')