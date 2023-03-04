import cv2
import numpy as np
import tensorflow as tf
from pathlib import Path

current_directory = Path(__file__).resolve().parent

# Load the pre-trained CNN model
model = tf.keras.models.load_model(
    f'{current_directory}/Sign_Language_recognitio/model_train/trained_model2.h5')

# Load the cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Define the list of emotions
emotions = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

# Function to detect faces in an image and predict the emotions
def predict_emotion(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
        roi = roi_gray.reshape(1, 48, 48, 1) / 255.0
        emotion = emotions[np.argmax(model.predict(roi))]
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(img, emotion, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 255, 0), 2, cv2.LINE_AA)

    return img


# Create a VideoCapture object to read from the camera
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Predict the emotions in the image
    img_emo = predict_emotion(frame)

    # Display the image
    cv2.imshow('Emotion Recognition', img_emo)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()