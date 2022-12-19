from django.urls import path

from mywebsite import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('movies', views.movies, name='movies'),
    path('youtube', views.youtube, name='youtube'),
]
