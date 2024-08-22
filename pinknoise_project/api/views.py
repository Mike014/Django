# api/views.py
import sys
import os

# Aggiungi il percorso al sys.path
sys.path.append(os.path.abspath(r'D:\Django\Git\Django\pinknoise_project\pinknoise'))

from django.shortcuts import render
from rest_framework import viewsets
from .models import PinkNoise
from .serializers import PinkNoiseSerializer

class PinkNoiseViewSet(viewsets.ModelViewSet):
    queryset = PinkNoise.objects.all()
    serializer_class = PinkNoiseSerializer

def dsp_view(request):
    return render(request, 'pinknoise/dsp_view.html')

       
   

