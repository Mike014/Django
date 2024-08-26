# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('upload/', views.upload_sound_effect, name='upload_sound_effect'),
    path('success/', views.success, name='success'),
]

