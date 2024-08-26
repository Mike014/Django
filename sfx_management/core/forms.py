# core/forms.py
from django import forms
from .models import SoundEffect

class SoundEffectForm(forms.ModelForm):
    class Meta:
        model = SoundEffect
        fields = ['name', 'duration', 'category', 'file', 'games']