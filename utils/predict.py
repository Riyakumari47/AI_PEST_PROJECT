import numpy as np
import tensorflow as tf
from PIL import Image

# Load trained AI model
model = tf.keras.models.load_model("model/pest_model.keras")

# Class Names (Inko baad me tumhare dataset ke hisaab se update karenge)
class_names = [
    "Cashew Anthracnose",
    "Cashew Gumosis",
    "Cashew Healthy",
    "Cashew Leaf Miner",
    "Cashew Red Rust",
    "Cassava Bacterial Blight",
    "Cassava Brown Spot",
    "Cassava Green Mite",
    "Cassava Healthy",
    "Cassava Mosaic",
    "Maize Fall Armyworm",
    "Maize Grasshopper",
    "Maize Healthy",
    "Maize Leaf Beetle",
    "Maize Leaf Blight",
    "Maize Leaf Spot",
    "Maize Streak Virus",
    "Tomato Healthy",
    "Tomato Leaf Blight",
    "Tomato Leaf Curl",
    "Tomato Septoria Leaf Spot",
    "Tomato Verticillium Wilt"
]

def predict_image(image):
    image = image.resize((224, 224))
    image = np.array(image)

    if image.shape[-1] == 4:
        image = image[:, :, :3]

    image = image / 255.0
    image = np.expand_dims(image, axis=0)

    prediction = model.predict(image, verbose=0)

    class_index = np.argmax(prediction)
    confidence = float(np.max(prediction)) * 100

    pest_name = class_names[class_index]

    return pest_name, round(confidence, 2)