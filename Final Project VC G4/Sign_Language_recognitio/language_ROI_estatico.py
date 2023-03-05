import cv2
import numpy as np
import tensorflow as tf
from pathlib import Path

current_directory = Path(__file__).resolve().parent

# Load the pre-trained CNN model
model = tf.keras.models.load_model(
    f'{current_directory}/model_train/trained_model.h5')

# Create a dictionary to map class indices to letters
class_indices_to_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']

# Define the region of interest (ROI)
roi = (200, 100, 300, 300)  # (x, y, width, height)

# Open the camera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Draw a blue rectangle around the ROI
    x, y, w, h = roi
    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Get the pixels inside the ROI and resize the image
    roi_frame = frame[y:y+h, x:x+w]
    roi_frame_resized = cv2.resize(roi_frame, (48, 48))

    # Preprocess the image
    roi_frame_resized = cv2.cvtColor(roi_frame_resized, cv2.COLOR_BGR2GRAY)
    roi_frame_resized = roi_frame_resized.reshape(1, 48, 48, 1) / 255.0

    # Make a prediction using the model
    prediction = model.predict(roi_frame_resized)
    class_index = np.argmax(prediction)
    letter = class_indices_to_letters[class_index]

    # Display the letter on the frame
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, letter, (x, y-10), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('Sign Language Recognition', frame)

    # Exit if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the windows
cap.release()
cv2.destroyAllWindows()