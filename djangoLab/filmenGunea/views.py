from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm, BozkatuForm
from filmenGunea.models import Filma, Bozkatzailea
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def index(request):
    return render(request, 'filmenGunea/index.html')

def register(request):
    if request.user.is_authenticated:
        return render(request, 'filmengunea/index.html')
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
    if request.user.is_authenticated:
        return render(request, 'filmengunea/index.html')
    if request.method=='POST':
        error=False
        errorea=""
        form=LoginForm(request.POST)
        if form.is_valid():
            izena=request.POST['user']
            password=request.POST['password']
            user = authenticate(username=izena, password=password)
            if user is not None:
                request.session['erabiltzailea'] = izena
                auth_login(request, user)

                #request.session['id'] = auth_user.objects.get(username=izena).id
                return render(request,'filmengunea/index.html')
            else:
                error=True
                errorea="Erabiltzaile edo pasahitz okerra"
                return render(request,'filmengunea/login.html',{'form':form, 'errorea':errorea, 'error':error})
    else:
        form=LoginForm()
        return render(request, 'filmenGunea/login.html',{'form':form})

@login_required(login_url=login)
def filmakIkusi(request):
    filmak = Filma.objects.all()

    paginator = Paginator(filmak, 4) # Show 4 films per page
    page = request.GET.get('page')
    try:
        filmak = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        filmak = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        filmak = paginator.page(paginator.num_pages)

    return render(request, 'filmenGunea/filmakIkusi.html', {'filmak': filmak})

@login_required(login_url=login)
def bozkatu(request):
    filmak = Filma.objects.all()
    if request.method=='POST':
        form=BozkatuForm(request.POST)
        hautatutakoa=request.POST['dropdown']
        filma=Filma.objects.get(izenburua=hautatutakoa)
        if form.is_valid:

            if Bozkatzailea.objects.filter(erabiltzailea_id=request.user).exists():
                bozkatzaile=Bozkatzailea.objects.get(erabiltzailea_id=request.user)
                if not bozkatzaile.gogokofilmak.filter(izenburua=hautatutakoa).exists():  
                    bozkatzaile.gogokofilmak.add(filma)
                    filma.bozkak=filma.bozkak+1
                    filma.save()
            else:
                bozkatzaileBerri=Bozkatzailea(erabiltzailea_id=request.user)
                bozkatzaileBerri.save()
                bozkatzaileBerri.gogokofilmak.add(filma)
                filma.bozkak=filma.bozkak+1
                filma.save()
        return render(request, 'filmenGunea/bozkatu.html', {'form':form, 'filmak': filmak})

    else:
        form=BozkatuForm()
        return render(request, 'filmenGunea/bozkatu.html', {'form':form, 'filmak': filmak})

@login_required(login_url=login)
def zaleak(request):
    return render(request, 'filmenGunea/zaleak.html')

@login_required(login_url=login)
def amaituSaioa(request):

    logout(request)
   
    return render(request, 'filmenGunea/index.html')