from django.urls import path

from mywebsite import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('discount', views.discount, name='discount'),
]
