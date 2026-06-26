import tensorflow as tf
import numpy as np
import os
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input


# ===============================
# PATHS
# ===============================

MODEL_PATH = "models/efficientnetb2_final.keras"

TEST_IMAGE = "E:/College/internship/crop-advisory-ai/test_images/01123.jpg"


# ===============================
# SETTINGS
# ===============================

IMG_SIZE = (260,260)


# ===============================
# LOAD MODEL
# ===============================

print("Loading model...")

model = tf.keras.models.load_model(
    MODEL_PATH
)

print("Model loaded successfully")


# ===============================
# LOAD CLASS NAMES
# ===============================

TRAIN_DIR = "datasets/ip102_balanced/train"

class_names = sorted(
    os.listdir(TRAIN_DIR)
)

print("Total Classes:", len(class_names))


# ===============================
# LOAD IMAGE
# ===============================

print("Loading image...")

img = image.load_img(
    TEST_IMAGE,
    target_size=IMG_SIZE
)


img_array = image.img_to_array(img)


img_array = np.expand_dims(
    img_array,
    axis=0
)


img_array = preprocess_input(
    img_array
)


# ===============================
# PREDICT
# ===============================

print("Predicting...")


predictions = model.predict(
    img_array
)


predicted_index = np.argmax(
    predictions[0]
)


confidence = predictions[0][predicted_index]


# ===============================
# OUTPUT
# ===============================


print("----------------------")
print("Prediction Result")
print("----------------------")

print(
    "Pest:",
    class_names[predicted_index]
)

print(
    "Confidence:",
    round(float(confidence)*100,2),
    "%"
)

print("----------------------")


# Top 5 predictions

top5 = np.argsort(predictions[0])[-5:][::-1]


print("\nTop 5 Predictions:")

for i in top5:
    print(
        class_names[i],
        "-",
        round(float(predictions[0][i])*100,2),
        "%"
    )