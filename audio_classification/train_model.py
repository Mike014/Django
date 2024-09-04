# -*- coding: utf-8 -*-

# train_model.py

import librosa
import numpy as np
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
import joblib
from audio.utils import extract_features

# Directory folder of the audio files
audio_dir = 'D:/Django/Git/Django/audio_classification/sounds/'

# Actual audio files
audio_files = [
    'Brown Noise.wav',
    'Pink Noise.wav',
    'Sine 440hz.wav',
    'Sine 880hz.wav',
    'White Noise TPDF 2.wav',
    'White Noise TPDF 3.wav',
    'White Noise TPDF 4.wav',
    'White Noise TPDF.wav'
]

labels = [
    'noise',
    'noise',
    'sine',
    'sine',
    'noise',
    'noise',
    'noise',
    'noise'
]

# Extracting features from audio files
features = []
for file in audio_files:
    file_path = audio_dir + file
    mfccs = extract_features(file_path)
    features.append(mfccs)

features = np.array(features)

# PCA application
pca = PCA(n_components=2)  
# components are the number of features to keep
reduced_features = pca.fit_transform(features)

# KNN model training
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(reduced_features, labels)

# Model saving
joblib.dump(pca, 'pca_model.pkl')
joblib.dump(knn, 'knn_model.pkl')

# Model has been trained
print('Model trained and saved successfully!')
