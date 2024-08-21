from django.urls import path
from . import views

urlpatterns = [
    path('plot/', views.plot_sinusoid, name='plot_sinusoid'),
]