# pinknoise/views.py
from django.shortcuts import render
from .dsp_code import PinkNoise

def dsp_view(request):
    pink_noise = PinkNoise()
    pink_noise.generate_and_plot()
    return render(request, 'pinknoise/dsp_view.html')


