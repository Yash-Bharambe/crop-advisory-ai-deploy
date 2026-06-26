from PIL import Image

from disease_predictor import predict_disease
from pest_predictor import predict_pest


image = Image.open(
    "E:/College/internship/crop-advisory-ai/test_images/disease.JPG"
)


print("Disease:")
print(
    predict_disease(image)
)


print("\nPest:")
print(
    predict_pest(image)
)