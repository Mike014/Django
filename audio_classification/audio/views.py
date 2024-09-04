# audio/views.py

from django.shortcuts import render, redirect
from .forms import AudioFileForm
from .models import AudioFile
from .utils import extract_features, apply_pca, classify_audio

def upload_audio(request):
    if request.method == 'POST':
        form = AudioFileForm(request.POST, request.FILES)
        if form.is_valid():
            audio_file = form.save()
            features = extract_features(audio_file.file.path)
            reduced_features = apply_pca(features)
            prediction = classify_audio(reduced_features)
            return render(request, 'results.html', {'prediction': prediction})
    else:
        form = AudioFileForm()
    return render(request, 'upload.html', {'form': form})

def home(request):
    return redirect('upload_audio')  

# Views are the functions that handle requests and return responses. 
# In this case, the upload_audio function handles the request to upload an audio file.
# POST requests are used to submit data to the server, while GET requests are used to retrieve data from the server.
# The function checks if the request method is POST, which means the form has been submitted.
# If the form is valid, the audio file is saved to the database, and its features are extracted using the extract_features function.
# The features are then reduced using PCA (Principal Component Analysis) to reduce the dimensionality of the data.

