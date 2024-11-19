# This is the main process of building the Neural Network Model and training it

# PREPARING TRAINING DATA

from DataPreparation import prepare_dataset

# Prepare the dataset using the new extract_spectrogram method
dataset, labels = prepare_dataset('./Audio_Files')

from sklearn.model_selection import KFold  # machine learning training library
from sklearn.preprocessing import LabelEncoder

# For training, Labels need to be converted to integers
label_encoder = LabelEncoder()
label_encoded = label_encoder.fit_transform(labels)

# preparing k-fold validation for training
k = 5  # number of folds
kfoldval = KFold(n_splits=k, shuffle=True, random_state=69)

# storing accuracies of the model on each fold
fold_accuracies = []

# TESTING THE MODEL

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from Model import create_cnn_model  # Assuming we are using the CNN model

# K-Fold Cross-Validation Loop
for train_index, val_index in kfoldval.split(dataset):
    # Split data into training and validation sets for the current fold
    dataset_train, dataset_val = dataset[train_index], dataset[val_index]
    label_train, label_val = label_encoded[train_index], label_encoded[val_index]

    # Define model (redefined each fold to reset weights)
    model = create_cnn_model(dataset_train, label_encoder)

    # Compile the model
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(dataset_train, label_train, epochs=50, batch_size=32, verbose=1)

    # Evaluate the model on the validation set
    val_loss, val_accuracy = model.evaluate(dataset_val, label_val, verbose=0)
    fold_accuracies.append(val_accuracy)
    print(f"Fold accuracy: {val_accuracy:.2f}")

# Calculate the average accuracy across all folds
average_accuracy = np.mean(fold_accuracies)
print(f"Average K-Fold Accuracy: {average_accuracy:.2f}")
