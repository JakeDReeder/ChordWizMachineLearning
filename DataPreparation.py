import os
import numpy as np
from AudioProcessing import extract_audio_features

def prepare_dataset(folder_path):
    dataset = []  # Features
    labels = []   # Labels

    for chord_folder in os.listdir(folder_path):
        chord_label = chord_folder  # Ex: Minor, Major, Diminished, etc.
        chord_path = os.path.join(folder_path, chord_folder)

        # Check if the current path is a directory
        if not os.path.isdir(chord_path):
            continue

        for file_name in os.listdir(chord_path):
            file_path = os.path.join(chord_path, file_name)

            # Check if the current file is a valid file and not a directory
            if not os.path.isfile(file_path):
                continue

            # Extract features and append to dataset and labels
            features = extract_audio_features(file_path)
            dataset.append(features)
            labels.append(chord_label)

    return np.array(dataset), np.array(labels)
