# audio/forms.py

from django import forms
from .models import AudioFile

class AudioFileForm(forms.ModelForm):
    class Meta:
        model = AudioFile
        fields = ['file']  
        
# The AudioFileForm class is a ModelForm that is used to create a form for uploading audio files.
# The Meta class specifies the model to use (AudioFile) and the fields to include in the form (file).        