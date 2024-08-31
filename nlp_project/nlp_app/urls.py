# nlp_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('analyze/', views.analyze_text, name='analyze_text'),
]