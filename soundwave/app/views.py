from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from pydub import AudioSegment
from pydub.generators import Sine
import logging
import os

# Configura il logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def index(request):
    return HttpResponse("""
        <h1>Welcome to Soundwave</h1>
        <p>This project allows you to generate and manipulate sounds using Python libraries.</p>
        <p><a href="/polls/generate_sound/">Click here to generate a sound</a></p>
    """)

def generate_sound(request):
    try:
        sine_wave = Sine(440).to_audio_segment(duration=2000)
        
        file_path = "generated_sound.wav"
        sine_wave.export(file_path, format="wav")
        
        if os.path.exists(file_path):
            logger.debug(f"File {file_path} created successfully.")
            response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename="generated_sound.wav")
            return response
        else:
            logger.error(f"File {file_path} was not created.")
            return HttpResponse("Error generating sound: File not created.", status=500)
    except Exception as e:
        logger.error(f"Error generating sound: {e}")
        return HttpResponse(f"Error generating sound: {e}", status=500)









