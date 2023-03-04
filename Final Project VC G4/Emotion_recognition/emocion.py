import cv2
import numpy as np
import tensorflow as tf
from pathlib import Path

current_directory = Path(__file__).resolve().parent

# Load the pre-trained CNN model
model = tf.keras.models.load_model(
    f'{current_directory}/model_train/trained_model2.h5')

# Load the cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Define the list of emotions
emotions = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']


def predict_emotion_image(frame,emotion_image):
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = cv2.imread(f'{current_directory}/imagen/{emotion_image}.jpg',
                        cv2.IMREAD_GRAYSCALE)
    
    faces = face_cascade.detectMultiScale(
        img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        roi_gray = img[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
        roi = roi_gray.reshape(1, 48, 48, 1) / 255.0
        emotion = emotions[np.argmax(model.predict(roi))]
        frame = cv2.imread(f'{current_directory}/imagen/{emotion_image}.jpg')
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, emotion, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 255, 0), 2, cv2.LINE_AA)

    return frame




# Function to detect faces in an image and predict the emotions
def predict_emotion_video(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
        roi = roi_gray.reshape(1, 48, 48, 1) / 255.0
        emotion = emotions[np.argmax(model.predict(roi))]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, emotion, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 255, 0), 2, cv2.LINE_AA)

    return frame

def detection_realtime():
    # Open the default camera
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Apply emotion detection to the frame
        frame_emo = predict_emotion_video(frame)

        # Display the resulting frame
        cv2.imshow('Emotion Recognition', frame_emo)

        # Exit on ESC key
        if cv2.waitKey(1) == 27:
            break

    # Release the capture and destroy the windows
    cap.release()
    cv2.destroyAllWindows()


def menu(opcion):
    if(opcion==1):
        # Load the image file
        emotions_list = {1:'angry', 2:'disgust', 3:'fear', 4:'happy', 5:'neutral', 6:'sad', 7:'surprise'}

        emotion = int(input("\nSeleccione una imagen: \n1. angry\n2. disgust\n3. fear\n4. happy\n5. neutral\n6. sad\n7. surprise\n\t--> "))
        img = cv2.imread(f'{current_directory}/imagen/{emotions_list[emotion]}.jpg',
                        cv2.IMREAD_GRAYSCALE)
        # Predict the emotions in the image
        img_emo = predict_emotion_image(img,emotions_list[emotion])

        # Display the image
        cv2.imshow('Emotion Recognition', img_emo)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        
    elif(opcion==2):
        detection_realtime()

opcion = int(input(f"\nSeleccione una opcion:\n1. Detectar emociones de imagenes\n2. Detectar emociones en tiempo real.\n\t--> "))
menu(opcion)
