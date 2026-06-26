from ultralytics import YOLO
import tempfile
from PIL import Image

print("Loading Pest Model...")
model = YOLO("models/best.pt")
print("Model loaded successfully")


def predict_pest(image):
    """
    image = PIL Image from Streamlit

    Returns:
    {
        "pest": "...",
        "confidence": ...
    }
    """

    # Save uploaded PIL image temporarily
    with tempfile.NamedTemporaryFile(
        suffix=".jpg",
        delete=False
    ) as temp_file:

        image.save(temp_file.name)

        results = model(temp_file.name)

    if len(results[0].boxes) == 0:
        return {
            "pest": "No pest detected",
            "confidence": 0
        }

    box = results[0].boxes[0]

    cls = int(box.cls[0])
    conf = float(box.conf[0]) * 100

    return {
        "pest": model.names[cls],
        "confidence": round(conf, 2)
    }


# Test
if __name__ == "__main__":

    img = Image.open(
        "test_images/01123.jpg"
    )

    result = predict_pest(img)

    print(result)