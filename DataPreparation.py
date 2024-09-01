import os
import numpy as np

def prepare_dataset(folder_path):
    X = []  # Features
    y = []  # Labels

    for chord_folder in os.listdir(folder_path):
        chord_label = chord_folder  # Ex: Minor, Major, Diminished etc.
        chord_path = os.path.join(folder_path, chord_folder)

        for file_name in os.listdir(chord_path):
            file_path = os.path.join(chord_path, file_name)
            features = extract_features(file_path)
            
            X.append(features)
            y.append(chord_label)

    return np.array(X), np.array(y)
