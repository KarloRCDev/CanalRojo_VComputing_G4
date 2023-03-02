import numpy as np
import tensorflow as tf
from pathlib import Path

current_directory = Path(__file__).resolve().parent

# Training data generator
training_data_gen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
training_gen = training_data_gen.flow_from_directory(directory=f'{current_directory}/model_train/train', target_size=(48, 48), color_mode='grayscale', batch_size=32, class_mode='categorical')

# Test data generator
test_data_gen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
test_gen = test_data_gen.flow_from_directory(directory=f'{current_directory}/model_train/test', target_size=(48, 48), color_mode='grayscale', batch_size=32, class_mode='categorical')

# Load the pre-trained CNN model
model = tf.keras.Sequential()

# Add convolutional layers
model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(48, 48, 1)))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))
model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))
model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))

# Flatten the output from the convolutional layers
model.add(tf.keras.layers.Flatten())

# Add a dense layer for classification
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dense(24, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
print(len(training_gen))
history = model.fit(training_gen, epochs=10, validation_data=test_gen, validation_steps=len(test_gen))


# Save the trained model
model.save(f'{current_directory}/model_train/trained_model.h5')
