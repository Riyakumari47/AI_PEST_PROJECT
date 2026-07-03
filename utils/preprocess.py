import cv2
import numpy as np

def preprocess_image(image):
    # Resize image
    image = cv2.resize(image, (224, 224))

    # Convert image to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Normalize image
    image = image / 255.0

    # Add batch dimension
    image = np.expand_dims(image, axis=0)

    return image