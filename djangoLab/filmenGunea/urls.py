from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('filmakIkusi', views.filmakIkusi, name='filmakIkusi'),
    path('bozkatu', views.bozkatu, name='bozkatu'),
    path('zaleak', views.zaleak, name='zaleak'),
    path('amaituSaioa', views.amaituSaioa, name='amaituSaioa'),
]
