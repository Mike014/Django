from django.shortcuts import render
from django.http import HttpResponse
from .forms import AudioUploadForm
import speech_recognition as sr

def index(request):
    transcription = None  
    if request.method == 'POST':
        form = AudioUploadForm(request.POST, request.FILES)
        if form.is_valid():
            audio_file = request.FILES['audio_file']

            # Use speech_recognition to transcribe the audio
            recognizer = sr.Recognizer()
            with sr.AudioFile(audio_file) as source:
                audio_data = recognizer.record(source)
                try:
                    transcription = recognizer.recognize_google(audio_data, language='en-US')
                except sr.UnknownValueError:
                    transcription = "Unable to understand the audio."
                except sr.RequestError:
                    transcription = "Error in the request to the speech recognition service."
    else:
        form = AudioUploadForm()

    return render(request, 'transcriber/index.html', {'form': form, 'transcription': transcription})



