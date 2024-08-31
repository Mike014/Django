# -*- coding: utf-8 -*-
import spacy
from django.shortcuts import render
from collections import Counter

# Carica il modello pre-addestrato di spaCy
nlp = spacy.load("en_core_web_sm")

def analyze_text(request):
    try:
        if request.method == 'POST':
            text = request.POST['text']
            doc = nlp(text)
            tokens = [token.text for token in doc]
            stop_words = spacy.lang.en.stop_words.STOP_WORDS
            filtered_tokens = [token.text for token in doc if token.text.lower() not in stop_words]
            freq_dist = Counter(filtered_tokens)
            
            # Riconoscimento di Entità Nominate (NER)
            entities = [(ent.text, ent.label_) for ent in doc.ents]
            
            # Part-of-Speech (POS) Tagging
            pos_tags = [(token.text, token.pos_) for token in doc]
            
            # Lemmatizzazione
            lemmas = [(token.text, token.lemma_) for token in doc]
            
            context = {
                'text': text,
                'tokens': tokens,
                'filtered_tokens': filtered_tokens,
                'freq_dist': freq_dist.most_common(10),
                'entities': entities,
                'pos_tags': pos_tags,
                'lemmas': lemmas,
            }
            return render(request, 'nlp_app/analyze.html', context)
        return render(request, 'nlp_app/analyze.html')
    except Exception as e:
        return render(request, 'nlp_app/analyze.html', {'error': str(e)})

  
  
     
  





























