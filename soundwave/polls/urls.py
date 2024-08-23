# polls/urls.py
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('generate_sound/', views.generate_sound, name='generate_sound')
]