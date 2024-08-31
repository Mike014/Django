# translator/views.py
from django.shortcuts import render
from googletrans import Translator
import spacy

# Carica i modelli di lingua
nlp_it = spacy.load('it_core_news_sm')
nlp_en = spacy.load('en_core_web_sm')

# Inizializza il traduttore
translator = Translator()

def translate_text(request):
    if request.method == 'POST': 
        text = request.POST.get('text')
        # Traduci il testo dall'italiano all'inglese
        translation = translator.translate(text, src='it', dest='en')
        translated_text = translation.text
        return render(request, 'translator/result.html', {'translated_text': translated_text})
    return render(request, 'translator/translate.html')
    
           
           
       
           
