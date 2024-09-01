import librosa
import numpy as np

def extract_audio_features(file_path):
    # Load the audio file
    y, sr = librosa.load(file_path, sr=44100)  # sr is the sample rate

    # Extract Mel-frequency cepstral coefficients (MFCC) features
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)  # Use 13 MFCC coefficients
    
    # Extract Chroma features (pitch classes)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    
    # Concatenate features into a vector
    feature_vector = np.hstack((np.mean(mfccs, axis=1), np.mean(chroma, axis=1)))
    
    return feature_vector
