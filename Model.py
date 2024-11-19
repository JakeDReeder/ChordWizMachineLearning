import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

def create_cnn_model(X_train, label_encoder):
    model = Sequential()

    # 1. Convolutional Layer
    # Conv2D(32, (3, 3), activation='relu', input_shape=(X_train.shape[1], X_train.shape[2], 1))
    # - Conv2D: Applies a 2D convolutional filter to the input image to detect local patterns.
    # - 32: The number of filters used in this layer (controls how many features will be detected).
    # - (3, 3): The size of the convolutional filter, scanning over a 3x3 region of the image.
    # - activation='relu': Uses the ReLU activation function to introduce non-linearity, allowing the model to learn more complex patterns.
    # - input_shape: Specifies the shape of the input. X_train.shape[1] and X_train.shape[2] represent the height and width of the spectrogram.
    #   The `1` indicates that the input has one channel (grayscale).
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(X_train.shape[1], X_train.shape[2], 1)))

    # 2. MaxPooling Layer
    # MaxPooling2D: Reduces the spatial dimensions of the feature map by taking the maximum value over a (2, 2) region.
    # This helps reduce the computational complexity and prevents overfitting by focusing on the most important features.
    model.add(MaxPooling2D((2, 2)))

    # 3. Second Convolutional Layer
    # - 64 filters in this layer, detecting more complex patterns than the first layer.
    model.add(Conv2D(64, (3, 3), activation='relu'))
    
    # 4. MaxPooling Layer (again)
    model.add(MaxPooling2D((2, 2)))

    # 5. Third Convolutional Layer
    # - 128 filters to further learn higher-level features from the spectrogram.
    model.add(Conv2D(128, (3, 3), activation='relu'))
    
    # 6. MaxPooling Layer (again)
    model.add(MaxPooling2D((2, 2)))

    # 7. Flatten Layer
    # Flatten: Converts the 2D output from the previous convolutional and pooling layers into a 1D vector.
    # This is necessary because fully connected (dense) layers expect 1D input.
    model.add(Flatten())

    # 8. Fully Connected Layer (Dense Layer)
    # - Dense(128): Adds a fully connected layer with 128 neurons.
    # - activation='relu': Uses ReLU activation to introduce non-linearity.
    model.add(Dense(128, activation='relu'))

    # 9. Dropout Layer
    # Dropout(0.3): Randomly drops 30% of the neurons during training to prevent overfitting.
    model.add(Dropout(0.3))

    # 10. Output Layer
    # - Dense(len(label_encoder.classes_)): The number of neurons equals the number of classes (chord types).
    # - activation='softmax': Softmax converts the output into probabilities, making it suitable for multi-class classification tasks.
    model.add(Dense(len(label_encoder.classes_), activation='softmax'))

    return model
