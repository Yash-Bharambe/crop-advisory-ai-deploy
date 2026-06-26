import tensorflow as tf
import numpy as np
import os

from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input

MODEL_PATH = r"E:/College/internship/models/disease_model.keras"
TRAIN_DIR = r"E:/College/internship/crop-advisory-ai/datasets/plantvillage/PlantVillage/train"

IMG_SIZE = (224, 224)

print("Loading Disease Model...")
model = tf.keras.models.load_model(MODEL_PATH)
print("Model loaded successfully")

class_names = sorted(os.listdir(TRAIN_DIR))

def predict_disease(pil_image):

    img = pil_image.resize(IMG_SIZE)

    img_array = np.array(img)

    img_array = np.expand_dims(img_array, axis=0)

    img_array = preprocess_input(img_array)

    prediction = model.predict(img_array, verbose=0)

    predicted_index = np.argmax(prediction[0])

    confidence = float(prediction[0][predicted_index]) * 100

    return {
        "disease": class_names[predicted_index],
        "confidence": round(confidence, 2)
    }


if __name__ == "__main__":

    test_img = image.load_img(
        r"E:/College/internship/crop-advisory-ai/test_images/disease.JPG",
        target_size=IMG_SIZE
    )

    result = predict_disease(test_img)

    print(result)