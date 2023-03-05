# Importar las bibliotecas necesarias
import cv2
import numpy as np
import tensorflow as tf
from pathlib import Path

# Obtener la ruta del directorio actual
current_directory = Path(__file__).resolve().parent

# Cargar la cascada de Haar para la detección de manos
hand_cascade = cv2.CascadeClassifier(f'{current_directory}/xml/haarcascade_hand.xml')

# Cargar el modelo pre-entrenado para la clasificación de letras
model = tf.keras.models.load_model(f'{current_directory}/model_train/trained_model.h5')

# Definir las clases (letras del alfabeto)
classes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']

# Cargar la imagen a procesar
img = cv2.imread(f'{current_directory}/imagen/A_mano.jpg', cv2.IMREAD_COLOR)

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detectar las manos en la imagen utilizando la cascada de Haar
hands = hand_cascade.detectMultiScale(gray, 1.1, 4)

# Dibujar un rectángulo alrededor de cada mano y clasificarla en una letra
for (x, y, w, h) in hands:
    # Recortar la región de interés (ROI) de la mano
    roi = gray[y:y+h, x:x+w]
    # Redimensionar la ROI para que coincida con la forma de entrada del modelo
    roi = cv2.resize(roi, (48, 48))
    # Convertir la ROI a un tensor 3D
    roi = np.expand_dims(roi, axis=-1)
    roi = np.expand_dims(roi, axis=0)
    # Realizar la predicción de la letra correspondiente a la mano
    prediction = model.predict(roi)
    # Obtener la clase con la mayor probabilidad
    class_idx = np.argmax(prediction)
    # Obtener la letra correspondiente a la clase predicha
    letter = classes[class_idx]
    # Dibujar un rectángulo alrededor de la mano
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Colocar la letra predicha sobre la imagen
    cv2.putText(img, letter, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

# Mostrar la imagen resultante con las manos detectadas y las letras clasificadas
cv2.imshow('image', img)
cv2.waitKey(0)

# Liberar los recursos utilizados por la ventana de visualización
cv2.destroyAllWindows()