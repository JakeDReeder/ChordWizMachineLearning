# This is the main process of building the Neural Network Model and training it

# PREPARING TRAINING DATA

from DataPreparation import prepare_dataset

dataset, labels = prepare_dataset('./data')

from sklearn.model_selection import KFold  
from sklearn.preprocessing import LabelEncoder

# For training, Labels need to be converted to integers
label_encoder = LabelEncoder()
label_encoded = label_encoder.fit_transform(labels)

# preparing k-fold validation for training
k = 5  # number of folds
kfoldval = KFold(n_splits=k, shuffle=True, random_state=69)

fold_accuracies = []

# TRAINING AND TESTING THE MODEL

import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import ModelCheckpoint
from Model import create_cnn_model  

# for storing the model
# checkpoint_path = "training_1/cp.ckpt"
# checkpoint_dir = os.path.dirname(checkpoint_path)
# cp_callback = ModelCheckpoint(checkpoint_path, monitor='val_accuracy', verbose=1, save_best_only=True)

saved_model = Sequential()

# K-Fold Cross-Validation Loop
for train_index, val_index in kfoldval.split(dataset):
    # Split data into training and validation sets for the current fold
    dataset_train, dataset_val = dataset[train_index], dataset[val_index]
    label_train, label_val = label_encoded[train_index], label_encoded[val_index]

    model = create_cnn_model(dataset_train, label_encoder)

    model.compile(optimizer='adam', loss='BinaryCrossentropy', metrics=['accuracy'])

    model.fit(dataset_train, label_train, epochs=200, batch_size=32, verbose=1)

    saved_model = model

    val_loss, val_accuracy = model.evaluate(dataset_val, label_val, verbose=0)
    fold_accuracies.append(val_accuracy)
    print(f"Fold accuracy: {val_accuracy:.2f}")

saved_model.save("Major_Minor_Model.keras")

# Calculate the average accuracy across all folds
average_accuracy = np.mean(fold_accuracies)
print(f"Average K-Fold Accuracy: {average_accuracy:.2f}")


