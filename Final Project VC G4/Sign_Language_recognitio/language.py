import cv2
import numpy as np
import tensorflow as tf
from pathlib import Path

current_directory = Path(__file__).resolve().parent

# Load the pre-trained CNN model
model = tf.keras.models.load_model(
    f'{current_directory}/model_train/trained_model.h5')

# Load the cascade classifier for hand detection
#cascade_path = "fullpath_to_hand_cascade/haarcascade_hand.xml"
hand_cascade = cv2.CascadeClassifier("haarcascade_hand.xml")

# Define the list of letters
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']

# Function to detect hands in an image and predict the letters


letter_image = "A_mano"


def predict_letter(img):
    # Detect hands in the image
    hands = hand_cascade.detectMultiScale(
        img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in hands:
        # Extract the hand region
        hand_roi = img[y:y + h, x:x + w]
        # Resize the hand region to 48x48 pixels
        hand_roi = cv2.resize(hand_roi, (48, 48), interpolation=cv2.INTER_AREA)
        # Normalize the pixel values to [0, 1]
        hand_roi = hand_roi.reshape(1, 48, 48, 1) / 255.0
        # Predict the letter
        letter = letters[np.argmax(model.predict(hand_roi))]
        # Draw a rectangle around the hand and display the predicted letter
        frame = cv2.imread(str(current_directory / "imagen" / f"{letter_image}.jpg"))
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, letter, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 255, 0), 2, cv2.LINE_AA)

    return frame


# Loop through all the letter images and predict the letters in each image
for letter in letters:
    # Load the image file
    #
    img = cv2.imread(str(current_directory/"imagen"/ f"{letter}.jpg"),
                     cv2.IMREAD_GRAYSCALE)
    # Predict the letter in the image
    img_letter = predict_letter(img)

    # Display the image
    cv2.imshow('Letter Recognition', img_letter)
    cv2.waitKey(0)

cv2.destroyAllWindows()
