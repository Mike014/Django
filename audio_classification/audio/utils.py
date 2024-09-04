# audio/utils.py

import librosa
import numpy as np
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
import joblib

def extract_features(audio_path):
    y, sr = librosa.load(audio_path)
    mfccs = librosa.feature.mfcc(y=y, sr=sr)
    return mfccs.mean(axis=1)

def apply_pca(features):
    pca = joblib.load('pca_model.pkl')
    return pca.transform([features])

def classify_audio(features):
    knn = joblib.load('knn_model.pkl')
    return knn.predict(features)[0]

# The extract_features function uses the librosa library to load an audio file and extract the MFCC (Mel-Frequency Cepstral Coefficients) features.
# The features are then returned as the mean of each coefficient.
# The apply_pca function loads a pre-trained PCA (Principal Component Analysis) model and applies it to the extracted features.
# The classify_audio function loads a pre-trained KNN (K-Nearest Neighbors) classifier and uses it to predict the class of the audio file based on the reduced features.
