import py_compile
from django.contrib import admin
from django.urls import path

from accounts import views

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]