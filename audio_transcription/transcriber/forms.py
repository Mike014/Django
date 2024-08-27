from django import forms

class AudioUploadForm(forms.Form):
    audio_file = forms.FileField()

    def clean_audio_file(self):
        audio_file = self.cleaned_data.get('audio_file')
        if not audio_file.name.endswith('.wav'):
            raise forms.ValidationError("Only WAV files are supported.")
        return audio_file
