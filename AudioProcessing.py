import librosa
import numpy as np

def extract_spectrogram(file_path, n_mels=128, duration=2.0, sr=44100):
    y, sr = librosa.load(file_path, sr=sr, duration=duration)  # Load audio with specific duration

    # Generate a Mel-spectrogram
    mel_spectrogram = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels, fmax=8000)
    mel_spectrogram_db = librosa.power_to_db(mel_spectrogram, ref=np.max)
    
    # Normalize [0, 1]
    mel_spectrogram_db = (mel_spectrogram_db + 80) / 80  # Since librosa returns [-80,0] dB

    return mel_spectrogram_db
