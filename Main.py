# This is the main process of building the Neural Network Model and training it

# PREPARING TRAINING DATA

from DataPreparation import prepare_dataset

X, y = prepare_dataset('./Chords')

from sklearn.model_selection import KFold # machine learning training library
from sklearn.preprocessing import LabelEncoder

# For training, Labels need to be converted to integers
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# preparing k-fold validation for training
k = 5 # number of folds
kkoldval = KFold(n_splits=k, shuffle=True, random_state=69)

# storing accuracies of the model on each fold
fold_accuracies = []

# TESTING THE MODEL

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from Model import create_model

# K-Fold Cross-Validation Loop
for train_index, val_index in kf.split(X):
    # Split data into training and validation sets for the current fold
    X_train, X_val = X[train_index], X[val_index]
    y_train, y_val = y_encoded[train_index], y_encoded[val_index]

    # define model (redefined each fold to reset weights)
    create_model(X_train, label_encoder)

     # Compile the model
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(X_train, y_train, epochs=50, batch_size=32, verbose=1)

    # Evaluate the model on the validation set
    val_loss, val_accuracy = model.evaluate(X_val, y_val, verbose=0)
    fold_accuracies.append(val_accuracy)
    print(f"Fold accuracy: {val_accuracy:.2f}")

# Calculate the average accuracy across all folds
average_accuracy = np.mean(fold_accuracies)
print(f"Average K-Fold Accuracy: {average_accuracy:.2f}")