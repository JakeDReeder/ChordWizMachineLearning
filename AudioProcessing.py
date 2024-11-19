import librosa
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

def extract_spectrogram(file_path, n_mels=128, duration=2.0, sr=44100):
    # Load the audio file
    y, sr = librosa.load(file_path, sr=sr, duration=duration)  # Load audio with specific duration

    # Generate a Mel-spectrogram
    mel_spectrogram = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels, fmax=8000)
    
    # Convert to decibels (log scale) to visualize the energy distribution
    mel_spectrogram_db = librosa.power_to_db(mel_spectrogram, ref=np.max)
    
    # Optionally, you can normalize the spectrogram to [0, 1] if required by the model
    mel_spectrogram_db = np.expand_dims(mel_spectrogram_db, axis=-1)  # Add channel dimension (1)
    
    # Return the processed spectrogram ready for CNN input
    return mel_spectrogram_db

# Example usage: 
# file_path = 'your_audio_file.wav'
# spectrogram = extract_spectrogram(file_path)
# spectrogram.shape  # Should be (height, width, 1) for CNN input

