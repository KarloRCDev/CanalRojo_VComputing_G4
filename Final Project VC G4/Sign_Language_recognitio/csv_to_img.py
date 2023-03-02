import numpy as np
import pandas as pd
import os
import cv2
from pathlib import Path

current_directory = Path(__file__).resolve().parent

# Change this to the path where you have saved the CSV files
csv_path = f'{current_directory}/csv_files'

# Change this to the path where you want to save the image files for the training set
train_image_path = f'{current_directory}/model_train/train'

# Change this to the path where you want to save the image files for the test set
test_image_path = f'{current_directory}/model_train/test'

# Load the training set CSV file
train_df = pd.read_csv(os.path.join(csv_path, "sign_mnist_train.csv"))

# Loop over each row in the training set and convert it to an image
for index, row in train_df.iterrows():
    # Create a directory for the letter if it doesn't exist
    letter_dir = os.path.join(train_image_path, chr(row[0]+65))
    if not os.path.exists(letter_dir):
        os.makedirs(letter_dir)

    # Convert the pixel values to a 28x28 grayscale image
    pixels = row[1:].values.reshape((28, 28)).astype("uint8")
    img_path = os.path.join(letter_dir, f"{index}.png")
    cv2.imwrite(img_path, pixels)

# Load the test set CSV file
test_df = pd.read_csv(os.path.join(csv_path, "sign_mnist_test.csv"))

# Loop over each row in the test set and convert it to an image
for index, row in test_df.iterrows():
    # Create a directory for the letter if it doesn't exist
    letter_dir = os.path.join(test_image_path, chr(row[0]+65))
    if not os.path.exists(letter_dir):
        os.makedirs(letter_dir)

    # Convert the pixel values to a 28x28 grayscale image
    pixels = row[1:].values.reshape((28, 28)).astype("uint8")
    img_path = os.path.join(letter_dir, f"{index}.png")
    cv2.imwrite(img_path, pixels)
