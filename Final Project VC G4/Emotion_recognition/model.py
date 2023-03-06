import tensorflow as tf
from pathlib import Path
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Conv2D, MaxPooling2D
current_directory = Path(__file__).resolve().parent

# Training data generator
training_data_gen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
training_gen = training_data_gen.flow_from_directory(directory=f'{current_directory}/model_train/train', target_size=(48, 48), color_mode='grayscale', batch_size=32, class_mode='categorical')

# Test data generator
test_data_gen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
test_gen = test_data_gen.flow_from_directory(directory=f'{current_directory}/model_train/test', target_size=(48, 48), color_mode='grayscale', batch_size=32, class_mode='categorical')

# Load the pre-trained CNN model
model = tf.keras.Sequential()
emotions = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

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
model.add(tf.keras.layers.Dense(len(emotions), activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit_generator(training_gen, steps_per_epoch=len(training_gen), epochs=20,
                              validation_data=test_gen, validation_steps=len(test_gen))

# Save the trained model
model.save(f'{current_directory}/model_train/trained_model2.h5')
