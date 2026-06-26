import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

from functools import lru_cache
from pathlib import Path


from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

MODEL_PATH = ROOT_DIR / "models" / "best.pt"

@lru_cache(maxsize=1)
def load_pest_model():

    from ultralytics import YOLO

    model = YOLO(str(MODEL_PATH))

    return model



def predict_pest(image):

    model = load_pest_model()

    results = model(image)


    detections = []


    for result in results:

        for box in result.boxes:

            cls = int(box.cls[0])

            conf = float(box.conf[0])

            detections.append(
                {
                    "pest": model.names[cls],
                    "confidence": round(conf * 100, 2)
                }
            )


    return detections