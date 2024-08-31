from django import forms

class DataInputForm(forms.Form):
    frequency = forms.FloatField(label='Frequenza (Hz)', min_value=20, max_value=20000)
    duration = forms.FloatField(label='Durata (s)', min_value=0.1, max_value=10.0)
    amplitude = forms.FloatField(label='Ampiezza', min_value=0.0, max_value=1.0)
    WAVE_CHOICES = [
        ('sine', 'Sine'),
        ('square', 'Square'),
        ('saw', 'Sawtooth'),
        ('triangle', 'Triangle'),
    ]
    wave_type = forms.ChoiceField(label='Tipo di Onda', choices=WAVE_CHOICES)




