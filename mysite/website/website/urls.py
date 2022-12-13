from django.contrib import admin
from django.urls import path

from mywebsite import views

urlpatterns = [
    path('', views.index,name='index'),
]
