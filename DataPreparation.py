import os
import numpy as np
from sklearn.model_selection import train_test_split
from AudioProcessing import extract_spectrogram

def prepare_dataset(folder_path, duration=2.0, n_mels=128, sr=44100, test_size=0.1, val_size=0.1):
    dataset = []  # spectrograms
    labels = []   # chord types

    # Iterate through each chord folder in the provided directory
    for chord_folder in os.listdir(folder_path):
        chord_label = chord_folder  # The chord type label (e.g., 'Major', 'Minor')
        chord_path = os.path.join(folder_path, chord_folder)

        if not os.path.isdir(chord_path):
            continue

        for file_name in os.listdir(chord_path):
            file_path = os.path.join(chord_path, file_name)

            if not os.path.isfile(file_path):
                continue

            # Extract the Mel-spectrogram features for the audio file
            spectrogram = extract_spectrogram(file_path, n_mels=n_mels, duration=duration, sr=sr)
            
            dataset.append(spectrogram)
            labels.append(chord_label)

    # Convert dataset and labels to numpy arrays for model training
    dataset = np.array(dataset, dtype=np.float32)
    labels = np.array(labels)

    # Split into training and temp set (where temp set will be split into val & test)
    train_data, temp_data, train_labels, temp_labels = train_test_split(
        dataset, labels, test_size=(test_size + val_size), random_state=42, stratify=labels
    )

    # Split temp set into validation and test
    val_size_adjusted = val_size / (test_size + val_size)  # Adjust proportion for splitting
    val_data, test_data, val_labels, test_labels = train_test_split(
        temp_data, temp_labels, test_size=val_size_adjusted, random_state=42, stratify=temp_labels
    )

    return train_data, train_labels, val_data, val_labels, test_data, test_labels


def prepare_multi_dataset(folder_path, duration=2.0, n_mels=128, sr=44100, test_size=0.1, val_size=0.1):
    dataset = []  # spectrograms
    labels = []   # chord labels like 'A_Major', 'B_Minor', etc.

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if not os.path.isfile(file_path) or not file_name.endswith('.wav'):
            continue

        try:
            # Extract label from filename, e.g., "A_Major_v1_0.wav" -> "A_Major"
            parts = file_name.split('_')
            chord_label = f"{parts[0]}_{parts[1]}"
        except IndexError:
            print(f"Skipping file with unexpected format: {file_name}")
            continue

        # Extract the Mel-spectrogram features for the audio file
        spectrogram = extract_spectrogram(file_path, n_mels=n_mels, duration=duration, sr=sr)

        dataset.append(spectrogram)
        labels.append(chord_label)

    # Convert dataset and labels to numpy arrays for model training
    dataset = np.array(dataset, dtype=np.float32)
    labels = np.array(labels)

    # Split into training and temp set (where temp set will be split into val & test)
    train_data, temp_data, train_labels, temp_labels = train_test_split(
        dataset, labels, test_size=(test_size + val_size), random_state=42, stratify=labels
    )

    # Split temp set into validation and test
    val_size_adjusted = val_size / (test_size + val_size)  # Adjust proportion for splitting
    val_data, test_data, val_labels, test_labels = train_test_split(
        temp_data, temp_labels, test_size=val_size_adjusted, random_state=42, stratify=temp_labels
    )

    return train_data, train_labels, val_data, val_labels, test_data, test_labels
