import cv2
from pathlib import Path
import numpy as np


current_directory = Path(__file__).resolve().parent
# Load the image
img = cv2.imread(f"{current_directory}/imagenes/per3.jpg")
# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load the face detector

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)


# Iterate over the faces
for (x, y, w, h) in faces:
    # Create a mask with a circular shape
    mask = np.zeros_like(img)
    mask = cv2.circle(mask, (x + w//2, y + h//2),
                      (w + h)//4, (255, 255, 255), -1)
    # Apply the mask to the face
    img = cv2.addWeighted(img, 0.7, mask, 0.3, 0)

# Display the image
cv2.imshow("Face Masked", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
