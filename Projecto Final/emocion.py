import cv2
import numpy as np
import tensorflow as tf
from pathlib import Path

current_directory = Path(__file__).resolve().parent

# Load the pre-trained CNN model
model = tf.keras.models.load_model(f'{current_directory}/model_train/trained_model.h5')

# Load the cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Define the list of emotions
emotions = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

# Function to detect faces in an image and predict the emotions
def predict_emotion(frame):
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        roi_gray = img[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
        roi = roi_gray.reshape(1, 48, 48, 1) / 255.0
        emotion = emotions[np.argmax(model.predict(roi))]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, emotion, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2, cv2.LINE_AA)
        
    return frame

# Load the image file
img = cv2.imread(f'{current_directory}/imagen/triste.jpg', cv2.IMREAD_GRAYSCALE)
# Predict the emotions in the image
img_emo = predict_emotion(img)

# Display the image
cv2.imshow('Emotion Recognition', img_emo)
cv2.waitKey(0)
cv2.destroyAllWindows()