
from django.contrib import admin
from django.urls import path

from web import views

urlpatterns = [
    path(r'index/', views.index, name='index'),
    path(r'about/', views.about, name='about'),
    path(r'gbook/', views.gbook, name='gbook'),
    path(r'info/', views.info, name='info'),
    path(r'life/', views.life, name='life'),
    path(r'list/', views.list, name='list'),
    path(r'share/', views.share, name='share'),
    path(r'time/', views.time, name='time'),
    path(r'login/', views.login, name='login'),
    path(r'register/', views.register, name='register'),
    path(r'indexee/', views.indexee, name='indexee')
]