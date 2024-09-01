import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# DETAILS ABOUT THE MODEL

# this gets pretty complex, and it may be hard to understand. 
# I would recommend some research on how a NN model works if this is too confusing to you

# 1. Input layer
# - Dense(256): Adds a fully connected (dense) layer with 256 neurons.
# - input_shape=(X_train.shape[1],): Specifies the shape of the input data. X_train.shape[1] represents the number of features in each input sample. This tells the model how many input features to expect.
# - activation='relu': Uses the ReLU (Rectified Linear Unit) activation function, which introduces non-linearity to the model and helps it learn complex patterns.

# 2. Dropout layer
# - Dropout(0.3): Adds a dropout layer that randomly sets 30% of the input units to zero during training to prevent overfitting. 
#   Dropout is a regularization technique that helps the model generalize better by preventing it from becoming too reliant on any particular set of neurons.

# 3. Second Hidden Layer
# - Dense(128): Adds another dense layer with 128 neurons.
# - activation='relu': Again, uses the ReLU activation function to introduce non-linearity.

# 4. Output Layer
# - Dense(len(label_encoder.classes_)): Adds the output layer with a number of neurons equal to the number of classes (chord types). len(label_encoder.classes_) gives the total number of unique chord labels in the dataset.
# - activation='softmax': Uses the softmax activation function, which is common for multi-class classification tasks. It converts the output of the neurons into probabilities that sum up to 1.

def create_model(X_train, label_encoder):
    model = Sequential()
    model.add(Dense(256, input_shape=(X_train.shape[1],), activation='relu'))
    model.add(Dropout(0.3))
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.3))
    model.add(Dense(len(label_encoder.classes_), activation='softmax'))
    return model