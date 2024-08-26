# core/views.py
import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.shortcuts import render
from .forms import SoundEffectForm
from .models import SoundEffect

def home(request):
    return render(request, 'core/home.html')

def upload_sound_effect(request):
    if request.method == 'POST':
        form = SoundEffectForm(request.POST, request.FILES)
        if form.is_valid():
            sound_effect = form.save()
            return redirect('success', sound_effect_id=sound_effect.id)
    else:
        form = SoundEffectForm()
    return render(request, 'core/upload.html', {'form': form})

def success(request, sound_effect_id):
    sound_effect = SoundEffect.objects.get(id=sound_effect_id)
    return render(request, 'core/success.html', {'sound_effect': sound_effect})

def list_files(request):
    media_path = os.path.join(settings.MEDIA_ROOT, 'sfx_files')
    files = os.listdir(media_path)
    return render(request, 'core/list_files.html', {'files': files})
   
   










       
