import cv2
import numpy as np
import tensorflow as tf
from pathlib import Path

current_directory = Path(__file__).resolve().parent

# Load the cascade
hand_cascade = cv2.CascadeClassifier(f'{current_directory}/haarcascade_hand.xml')

# Load the pre-trained CNN model
model = tf.keras.models.load_model(
    f'{current_directory}/model_train/trained_model.h5')


# Define the classes
classes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']

# Load the image
img = cv2.imread(f'{current_directory}/imagen/A_mano.jpg', cv2.IMREAD_COLOR)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect the hands
hands = hand_cascade.detectMultiScale(gray, 1.1, 4)

# Draw the rectangle around each hand
for (x, y, w, h) in hands:
    # Crop the hand region
    roi = gray[y:y+h, x:x+w]
    # Resize the ROI to match the input shape of the model
    roi = cv2.resize(roi, (48, 48))
    # Convert the ROI to a 3D tensor
    roi = np.expand_dims(roi, axis=-1)
    roi = np.expand_dims(roi, axis=0)
    # Predict the class of the hand
    prediction = model.predict(roi)
    # Get the class with highest probability
    class_idx = np.argmax(prediction)
    # Get the corresponding letter
    letter = classes[class_idx]
    # Draw the rectangle around the hand
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Put the predicted letter on the image
    cv2.putText(img, letter, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

# Display the resulting image
cv2.imshow('image', img)
cv2.waitKey(0)

# Release resources
cv2.destroyAllWindows()