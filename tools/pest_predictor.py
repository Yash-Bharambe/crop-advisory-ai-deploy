from functools import lru_cache
from pathlib import Path
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

MODEL_PATH = (
    Path(__file__).resolve()
    .parents[1]
    / "models"
    / "best.pt"
)


@lru_cache(maxsize=1)
def load_pest_model():

    from ultralytics import YOLO

    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Pest model missing: {MODEL_PATH}"
        )

    model = YOLO(str(MODEL_PATH))

    return model



def predict_pest(image):

    model = load_pest_model()

    results = model.predict(
        image,
        device="cpu",
        verbose=False
    )

    detections=[]

    for result in results:

        for box in result.boxes:

            cls=int(box.cls[0])

            conf=float(box.conf[0])


            detections.append(
                {
                    "pest": model.names[cls],
                    "confidence": round(conf*100,2)
                }
            )

    return detections