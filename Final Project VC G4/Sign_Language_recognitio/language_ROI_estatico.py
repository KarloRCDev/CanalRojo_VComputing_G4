import cv2
import numpy as np
import tensorflow as tf
from pathlib import Path

current_directory = Path(__file__).resolve().parent

# Cargar el modelo CNN pre-entrenado
model = tf.keras.models.load_model(
    f'{current_directory}/model_train/trained_model.h5')

# Crear un diccionario para mapear los índices de clase a las letras
class_indices_to_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']

# Definir la región de interés (ROI)
roi = (200, 100, 300, 300)  # (x, y, ancho, alto)

# Abrir la cámara
cap = cv2.VideoCapture(0)

while True:
    # Capturar el fotograma por fotograma
    ret, frame = cap.read()

    # Dibujar un rectángulo azul alrededor de la ROI
    x, y, w, h = roi
    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Obtener los píxeles dentro de la ROI y cambiar el tamaño de la imagen
    roi_frame = frame[y:y+h, x:x+w]
    roi_frame_resized = cv2.resize(roi_frame, (48, 48))

    # Preprocesar la imagen
    roi_frame_resized = cv2.cvtColor(roi_frame_resized, cv2.COLOR_BGR2GRAY)
    roi_frame_resized = roi_frame_resized.reshape(1, 48, 48, 1) / 255.0

    # Realizar una predicción con el modelo
    prediction = model.predict(roi_frame_resized)
    class_index = np.argmax(prediction)
    letter = class_indices_to_letters[class_index]

    # Mostrar la letra en el fotograma
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, letter, (x, y-10), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Mostrar el fotograma resultante
    cv2.imshow('Reconocimiento de Lenguaje de Señas', frame)

    # Salir si el usuario presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()