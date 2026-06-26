import tensorflow as tf
import numpy as np
import json
from functools import lru_cache
from pathlib import Path


# Project root: crop-advisory-ai-deploy
PROJECT_ROOT = Path(__file__).resolve().parents[1]

MODEL_PATH = PROJECT_ROOT / "models" / "disease_model.keras"
CLASS_FILE = PROJECT_ROOT / "knowledge_base" / "disease_classes.json"


def _resolve_model_path():

    if MODEL_PATH.exists():
        return MODEL_PATH

    raise FileNotFoundError(
        f"Disease model not found: {MODEL_PATH}"
    )


@lru_cache(maxsize=1)
def load_disease_model():

    model_path = _resolve_model_path()

    return tf.keras.models.load_model(
        str(model_path)
    )


@lru_cache(maxsize=1)
def load_class_names():

    if not CLASS_FILE.exists():
        raise FileNotFoundError(
            f"Disease class file missing: {CLASS_FILE}"
        )

    with open(CLASS_FILE, "r") as file:
        classes = json.load(file)

    return classes



def predict_disease(image):

    model = load_disease_model()
    classes = load_class_names()

    image = image.convert("RGB")
    image = image.resize((224, 224))

    img_array = np.array(
        image,
        dtype=np.float32
    )

    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    prediction = model.predict(
        img_array,
        verbose=0
    )

    index = int(np.argmax(prediction[0]))

    confidence = float(
        np.max(prediction[0])
    ) * 100


    return {
        "disease": classes[index],
        "confidence": round(confidence, 2)
    }