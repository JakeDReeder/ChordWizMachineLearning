import os
import numpy as np
from AudioProcessing import extract_spectrogram

def prepare_dataset(folder_path, duration=2.0, n_mels=128, sr=44100):
    dataset = []  # Features (spectrograms)
    labels = []   # Labels (chord types)

    # Iterate through each chord folder in the provided directory
    for chord_folder in os.listdir(folder_path):
        chord_label = chord_folder  # The chord type label (e.g., 'Major', 'Minor')
        chord_path = os.path.join(folder_path, chord_folder)

        # Ensure the current path is a directory
        if not os.path.isdir(chord_path):
            continue

        # Iterate through each file in the chord folder
        for file_name in os.listdir(chord_path):
            file_path = os.path.join(chord_path, file_name)

            # Ensure the current path is a file (not a directory)
            if not os.path.isfile(file_path):
                continue

            # Extract the Mel-spectrogram features for the audio file
            spectrogram = extract_spectrogram(file_path, n_mels=n_mels, duration=duration, sr=sr)
            
            # Append the spectrogram and corresponding chord label to the dataset
            dataset.append(spectrogram)
            labels.append(chord_label)

    # Convert dataset and labels to numpy arrays for model training
    dataset = np.array(dataset)
    labels = np.array(labels)

    # Normalize the spectrograms if necessary (optional, depending on your model's needs)
    dataset = dataset.astype('float32')  # Ensure the data type is float32 for CNN
    dataset = dataset / np.max(dataset)  # Normalize to the range [0, 1]

    return dataset, labels
