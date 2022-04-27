from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm


def index(request):
    return render(request, 'filmenGunea/index.html')

def register(request):

    if request.method=='GET':
        form=RegisterForm()    
        return render(request, 'filmenGunea/register.html',{'form':form})
    
    if request.method=='POST':
        error=False
        errorea=""
        form=RegisterForm(request.POST)
        if form.is_valid():
            user = request.POST['user']

            #existizen da
            if User.objects.filter(username=request.POST['user']).count() >0:
                error=True
                errorea="erabiltzailea existitzen da"
                return render(request, 'filmenGunea/register.html',{'form':form, 'errorea':errorea,'error':error})
            else:
                pass1=request.POST['pass1']
                pass2=request.POST['pass2']
                #pasahitzak berdinak direla bermatu
                if pass1 != pass2:
                    #ez badira berdinak
                    error=True
                    errorea="Sartu dituzun pasahitzak ez dira berdinak"
                    return render(request, 'filmenGunea/register.html',{'form':form, 'errorea':errorea,'error':error})
                else:
                    #berdinak badira
                    User.objects.create_user(user,email=None, password=pass1)
                    form = LoginForm()
                    return render(request, 'filmenGunea/login.html',{'form': form})
    
    

def login(request):
    if request.method=='POST':
        error=False
        errorea=""
        form=LoginForm(request.POST)
        if form.is_valid():
            izena=request.POST['user']
            password=request.POST['password']
            user = authenticate(username=izena, password=password)
            if user is not None:
                request.session['erabiltzailea'] = 'izena'
                return render(request,'filmengunea/index.html')
            else:
                error=True
                errorea="Erabiltzaile edo pasahitz okerra"
                return render(request,'filmengunea/login.html',{'form':form, 'errorea':errorea, 'error':error})
    else:
        form=LoginForm()
        return render(request, 'filmenGunea/login.html',{'form':form})

def filmakIkusi(request):
    return render(request, 'filmenGunea/filmakIkusi.html')

def bozkatu(request):
    return render(request, 'filmenGunea/bozkatu.html')

def zaleak(request):
    return render(request, 'filmenGunea/zaleak.html')