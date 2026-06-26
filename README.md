# Crop Disease and Pest Advisory Assistant

A computer-vision based agricultural advisory system that detects crop diseases and pests from images, validates the prediction using symptom questions, estimates risk severity, and generates safe source-backed advisory recommendations for farmers.

This README is intentionally detailed. It is written so that a student can explain the complete project during placements, viva, project review, resume discussion, or technical interviews.

---

## 1. One-Minute Project Pitch

The Crop Disease and Pest Advisory Assistant is an AI-powered Streamlit application designed to help farmers and agricultural advisors identify crop health issues early. The system accepts a crop image, runs two computer vision models, and produces an advisory report.

The project has two main AI modules:

1. Disease detection using a TensorFlow/Keras MobileNetV2 image classification model.
2. Pest detection using an Ultralytics YOLO object detection model.

After prediction, the system does not directly give treatment blindly. It asks follow-up symptom questions, calculates a risk level from field conditions, and then generates recommendations from a curated knowledge base. This makes the system more practical than a simple image classifier because it combines AI prediction with rule-based agricultural advisory logic.

---

## 2. Problem Statement

Crop diseases and pest attacks can reduce yield significantly if they are not detected early. Many farmers may not have immediate access to agricultural experts, especially in rural areas. Manual inspection can also be slow, subjective, and dependent on expert availability.

The problem this project solves is:

> Given a crop or leaf image, identify whether the crop is affected by a disease or pest, assess the severity, and provide safe advisory recommendations that can support early decision-making.

The system is not intended to replace agricultural experts. It acts as an early-warning and decision-support tool.

---

## 3. Main Objectives

The system is designed to:

- Detect crop diseases from leaf images.
- Detect pests from crop or pest images.
- Display prediction confidence.
- Ask symptom-based validation questions.
- Estimate risk severity using AI confidence and field observations.
- Generate safe recommendations using a knowledge base.
- Provide prevention guidance.
- Reference source categories such as ICAR, FAO, and CIMMYT.
- Avoid unsafe or overconfident pesticide advice.
- Provide a simple Streamlit frontend usable by non-technical users.

---

## 4. Key Features

- Image upload through Streamlit.
- Disease prediction using a Keras model.
- Pest detection using YOLO.
- Parallel model execution in the frontend for faster user experience.
- Confidence score display.
- Symptom validation engine.
- Risk assessment engine.
- Recommendation engine.
- JSON-based knowledge base.
- Source-backed advisory output.
- Local model loading with caching.
- Modular project structure with separate folders for app, tools, training, datasets, models, and knowledge base.

---

## 5. Technology Stack

### Programming Language

- Python

### Frontend

- Streamlit

### Disease Detection

- TensorFlow
- Keras
- MobileNetV2
- Transfer learning

### Pest Detection

- Ultralytics YOLO
- PyTorch backend
- Object detection

### Image Processing

- Pillow
- OpenCV
- NumPy

### Data Processing and Analysis

- Pandas
- Matplotlib
- Seaborn
- scikit-learn

### Knowledge Base

- JSON files

### Development Environment

- Windows
- Python virtual environments
- Separate model/runtime environments for TensorFlow and YOLO experiments

---

## 6. High-Level System Architecture

```text
Farmer / User
     |
     v
Streamlit Frontend
     |
     v
Image Upload
     |
     +----------------------------+
     |                            |
     v                            v
Disease Detection            Pest Detection
MobileNetV2 CNN              YOLO Detector
     |                            |
     v                            v
Disease Prediction           Pest Prediction
     |                            |
     +-------------+--------------+
                   |
                   v
          Advisory Intelligence
                   |
     +-------------+--------------+--------------+
     |                            |              |
     v                            v              v
Symptom Validation          Risk Engine     Recommendation Engine
     |                            |              |
     +-------------+--------------+--------------+
                   |
                   v
          Final Farmer Advisory
```

---

## 7. Project Folder Structure

```text
crop-advisory-ai/
|
|-- app/
|   |-- main.py
|   |-- app.py
|   |-- advisory_pipeline.py
|   |-- components/
|       |-- upload.py
|       |-- prediction.py
|       |-- symptoms.py
|       |-- risk_inputs.py
|       |-- results.py
|       |-- sidebar.py
|
|-- tools/
|   |-- disease_predictor.py
|   |-- pest_predictor.py
|   |-- symptom_engine.py
|   |-- risk_engine.py
|   |-- recommendation_engine.py
|   |-- knowledge_loader.py
|   |-- predict_disease.py
|   |-- predict_yolo.py
|   |-- test_models.py
|   |-- test_yolo.py
|   |-- test_efficientnetb2.py
|   |-- check_balanced.py
|   |-- create_balanced_ip102.py
|
|-- training/
|   |-- train_disease_model.py
|   |-- train_pest_model.py
|   |-- train_efficientnetb2.py
|   |-- finetune_pest_model.py
|
|-- knowledge_base/
|   |-- disease_guidelines.json
|   |-- pest_guidelines.json
|   |-- symptom_questions.json
|   |-- sources.json
|   |-- class_distribution.csv
|
|-- models/
|   |-- best.pt
|   |-- efficientnetb2_final.keras
|   |-- efficientnetb2_stage1.keras
|   |-- efficientnetb2_stage1.weights.h5
|
|-- datasets/
|   |-- plantvillage/
|   |-- plantdoc/
|   |-- ip102/
|   |-- ip102_balanced/
|   |-- processed/
|
|-- notebooks/
|-- test_images/
|-- requirements.txt
|-- README.md
```

### Folder Responsibilities

| Folder | Purpose |
|---|---|
| `app/` | Streamlit frontend and application pipeline |
| `app/components/` | Reusable UI sections |
| `tools/` | Inference utilities, advisory engines, data checks |
| `training/` | Model training scripts |
| `knowledge_base/` | Disease, pest, symptom, source, and recommendation data |
| `models/` | Trained model artifacts |
| `datasets/` | Raw and processed datasets |
| `notebooks/` | Dataset exploration and experiments |
| `test_images/` | Sample images for local testing |

---

## 8. Dataset Details

### 8.1 PlantVillage Dataset

PlantVillage is used for disease classification.

Purpose:

- Train the disease detection model.
- Classify crop leaf images into disease or healthy categories.

Dataset characteristics:

- Controlled leaf images.
- Multiple crops.
- Disease and healthy classes.
- Useful for initial supervised classification.

Examples of classes:

- Tomato Early Blight
- Tomato Late Blight
- Potato Early Blight
- Apple Scab
- Corn Common Rust
- Healthy leaf classes

The processed disease training folder contains 38 classes, including:

- `Apple___Apple_scab`
- `Corn_(maize)___healthy`
- `Tomato___Early_blight`
- `Potato___Late_blight`
- `Grape___Black_rot`
- `Pepper,_bell___Bacterial_spot`

### 8.2 PlantDoc Dataset

PlantDoc is included for future real-world validation.

Why PlantDoc matters:

- PlantVillage images are controlled and clean.
- Real farmer images may contain complex backgrounds, shadows, multiple leaves, occlusion, and lighting variations.
- PlantDoc helps evaluate model robustness in more realistic conditions.

### 8.3 IP102 Pest Dataset

IP102 is used for pest detection/classification experiments.

Purpose:

- Train and evaluate pest identification models.
- Provide 102 pest categories.

Characteristics:

- Real-world pest images.
- Many classes.
- More challenging than disease classification because pests may be small, occluded, or present in multiple positions.

Balanced dataset verification:

- Script: `tools/check_balanced.py`
- Dataset folder: `datasets/ip102_balanced/`
- Class count: 102
- Maximum images per class in balanced set: 300
- Minimum observed class count: 42
- Average class count: around 229

---

## 9. AI Module 1: Disease Detection

### 9.1 Purpose

The disease detection module classifies a crop leaf image into one of the trained disease or healthy categories.

Input:

```text
Leaf image
```

Output:

```python
{
    "disease": "Tomato___Early_blight",
    "confidence": 91.25
}
```

### 9.2 Model Architecture

The disease model uses MobileNetV2 with transfer learning.

Architecture:

```text
Input Image
     |
Data Augmentation
     |
MobileNetV2 Preprocessing
     |
MobileNetV2 Backbone
     |
Global Average Pooling
     |
Dropout
     |
Dense Softmax Layer
     |
Disease Class Prediction
```

### 9.3 Why MobileNetV2?

MobileNetV2 is a good choice because:

- It is lightweight.
- It is faster than many large CNN architectures.
- It is suitable for deployment in low-resource environments.
- It supports transfer learning from ImageNet.
- It performs well for image classification tasks.

### 9.4 Training Details

Training script:

```text
training/train_disease_model.py
```

Important configuration:

```python
IMG_SIZE = (224, 224)
BATCH_SIZE = 16
EPOCHS = 10
BASE_MODEL = MobileNetV2(weights="imagenet", include_top=False)
```

Loss:

```text
sparse_categorical_crossentropy
```

Optimizer:

```text
Adam
```

Callbacks:

- `ModelCheckpoint`
- `EarlyStopping`

Model save path used by the training script:

```text
../models/disease_model.keras
```

Runtime disease model path used by the inference utility:

```text
E:/College/internship/models/disease_model.keras
```

or fallback:

```text
E:/College/internship/crop-advisory-ai/models/disease_model.keras
```

### 9.5 Important Preprocessing Note

The saved disease model already contains MobileNetV2 preprocessing inside the model graph.

Therefore, during inference the predictor sends raw resized pixel values to the model:

```python
img = image.resize((224, 224))
img_array = np.array(img, dtype=np.float32)
img_array = np.expand_dims(img_array, axis=0)
prediction = model.predict(img_array, verbose=0)
```

Do not apply `preprocess_input()` again outside the model. Applying preprocessing twice can collapse predictions and make the model repeatedly output the same class such as `Corn_(maize)___healthy`.

### 9.6 Disease Predictor File

Main file:

```text
tools/disease_predictor.py
```

Responsibilities:

- Resolve disease model path.
- Load Keras model.
- Load class names from training folder.
- Resize image to 224 x 224.
- Convert image to NumPy array.
- Run prediction.
- Return predicted label and confidence.

The model and class list are cached using `lru_cache` so they are not reloaded on every Streamlit rerun.

---

## 10. AI Module 2: Pest Detection

### 10.1 Purpose

The pest detection module identifies pests in crop images.

Input:

```text
Crop or pest image
```

Output:

```python
[
    {
        "pest": "rice leaf roller",
        "confidence": 86.2
    }
]
```

### 10.2 Initial Pest Model Experiment

Before YOLO, an EfficientNetB2 classifier experiment was performed.

Script:

```text
training/train_efficientnetb2.py
```

Configuration:

- Input size: 260 x 260
- Classes: 102
- Backbone: EfficientNetB2
- Optimizer: Adam
- Learning rate: 0.001
- Loss: categorical cross entropy
- Label smoothing: 0.1

Result:

- Validation accuracy was around 57 to 58 percent.

Reason it was not selected:

- Pest classification is harder because an image may contain multiple pests.
- Pests may appear at different positions and scales.
- Classification does not localize the pest.
- Object detection is more suitable for field images.

### 10.3 Final Pest Model: YOLO

The final pest detection model uses YOLO.

Model file:

```text
models/best.pt
```

Predictor file:

```text
tools/pest_predictor.py
```

Why YOLO?

- It detects and localizes objects.
- It can handle multiple detections in one image.
- It is faster for real-time object detection.
- It is better suited for field images where pests may appear anywhere.

### 10.4 Pest Predictor Flow

```text
PIL Image
     |
YOLO Model
     |
Detection Results
     |
For each bounding box:
     - class index
     - confidence
     - class name
     |
Return list of pest detections
```

Simplified logic:

```python
results = model(image)

for result in results:
    for box in result.boxes:
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        detections.append({
            "pest": model.names[cls],
            "confidence": round(conf * 100, 2)
        })
```

---

## 11. Advisory Intelligence

The advisory part makes the system more useful than a plain prediction app. It combines AI output with farmer observations.

There are three major advisory engines:

1. Symptom Validation Engine
2. Risk Assessment Engine
3. Recommendation Engine

These are orchestrated by:

```text
app/advisory_pipeline.py
```

---

## 12. Symptom Validation Engine

File:

```text
tools/symptom_engine.py
```

Knowledge file:

```text
knowledge_base/symptom_questions.json
```

Purpose:

- Ask follow-up questions based on the predicted disease or pest.
- Validate whether visible symptoms match the AI prediction.
- Calculate a symptom match percentage.

Example:

Prediction:

```text
Tomato___Early_blight
```

Possible questions:

- Are there brown target-like spots?
- Are lower leaves affected first?
- Are leaves yellowing?

Each question has a score. If the farmer answers yes, that score is added.

Formula:

```text
symptom_match_percentage = (symptom_score / maximum_score) * 100
```

Output:

```python
{
    "prediction": "Tomato___Early_blight",
    "symptom_score": 4,
    "maximum_score": 5,
    "symptom_match": 80.0
}
```

Why this matters:

- AI models can be wrong.
- Images may be blurry or taken from bad angles.
- Symptom validation adds human-in-the-loop confirmation.

---

## 13. Risk Assessment Engine

File:

```text
tools/risk_engine.py
```

Purpose:

- Estimate severity of the issue.
- Convert field observations into a risk level.

Risk factors:

| Factor | Score |
|---|---:|
| Model confidence >= 80 percent | +2 |
| Rapid spread observed | +3 |
| Stem damage present | +3 |
| Crop affected > 50 percent | +3 |

Risk mapping:

| Score Range | Risk Level |
|---:|---|
| 0 to 2 | LOW |
| 3 to 5 | MEDIUM |
| 6 or more | HIGH |

Example:

```python
calculate_risk(
    confidence=91,
    rapid_spread=True,
    stem_damage=False,
    crop_percentage=60
)
```

Output:

```python
{
    "risk_score": 8,
    "risk_level": "HIGH",
    "factors": [
        "High AI confidence",
        "Rapid spread detected",
        "Large crop area affected"
    ]
}
```

Why this matters:

- A disease with high confidence but low spread may not need urgent intervention.
- A moderate-confidence detection with rapid spread may still require attention.
- Risk scoring makes recommendations more context-aware.

---

## 14. Recommendation Engine

File:

```text
tools/recommendation_engine.py
```

Knowledge files:

```text
knowledge_base/disease_guidelines.json
knowledge_base/pest_guidelines.json
knowledge_base/sources.json
```

Purpose:

- Generate safe advisory actions based on prediction and risk level.
- Provide prevention methods.
- Attach source categories.

Recommendation levels:

- Low risk recommendations
- Medium risk recommendations
- High risk recommendations

Example output:

```python
{
    "prediction": "Tomato___Early_blight",
    "risk": "HIGH",
    "actions": [
        "Use targeted fungicides",
        "Remove heavily infected plants"
    ],
    "prevention": [
        "Crop rotation",
        "Adequate plant spacing"
    ],
    "sources": [
        "ICAR",
        "FAO"
    ]
}
```

Safety design:

- The system avoids giving highly specific chemical dosage instructions without expert validation.
- The output is advisory and recommends consulting local agricultural extension services when risk is high.
- Prevention and integrated pest management are prioritized.

---

## 15. Knowledge Base Design

The knowledge base is stored as JSON for simplicity and easy editing.

### 15.1 Disease Guidelines

File:

```text
knowledge_base/disease_guidelines.json
```

Contains:

- Display name
- Crop
- Type
- Description
- Symptoms
- Common conditions
- Risk factors
- Risk questions
- Recommendations
- Prevention
- Source category

### 15.2 Pest Guidelines

File:

```text
knowledge_base/pest_guidelines.json
```

Contains:

- Pest display name
- Crop category
- Description
- Symptoms
- Damage type
- Common conditions
- Risk factors
- Risk questions
- Low, medium, and high risk recommendations
- Prevention guidance
- Source categories

### 15.3 Symptom Questions

File:

```text
knowledge_base/symptom_questions.json
```

Contains:

- Prediction-specific questions
- Score for yes answer
- Importance level
- Maximum score
- Minimum questions required

### 15.4 Sources

File:

```text
knowledge_base/sources.json
```

Source categories include:

- ICAR
- FAO
- CIMMYT

These provide credibility and context for agricultural recommendations.

---

## 16. Full Advisory Pipeline

File:

```text
app/advisory_pipeline.py
```

Function:

```python
run_advisory_pipeline(
    prediction,
    model_confidence,
    answers,
    rapid_spread=False,
    stem_damage=False,
    crop_percentage=0
)
```

Pipeline steps:

1. Calculate symptom score.
2. Calculate risk score and risk level.
3. Generate recommendation based on prediction and risk.
4. Return final advisory object.

Final result structure:

```python
{
    "prediction": prediction,
    "model_confidence": model_confidence,
    "symptom_match": symptom_match,
    "risk": risk_result,
    "recommendation": recommendation
}
```

This pipeline separates AI prediction from advisory reasoning. That separation makes the system easier to debug and explain.

---

## 17. Streamlit Frontend

Main file:

```text
app/main.py
```

The frontend handles:

- Page layout
- Sidebar information
- Model preload
- Image upload
- Image display
- Parallel disease and pest model execution
- Prediction display
- User selection of advisory target
- Symptom input
- Risk input
- Advisory report display

### 17.1 User Flow

```text
Open app
   |
Upload crop image
   |
Click Analyze Image
   |
Disease and pest models run
   |
Predictions are shown
   |
User selects the prediction to validate
   |
User answers symptom questions
   |
User enters field risk factors
   |
Click Generate Field Advisory
   |
System displays final report
```

### 17.2 Why Streamlit?

Streamlit is used because:

- It is simple for Python-based ML demos.
- It requires less frontend boilerplate.
- It can directly call Python model inference functions.
- It is suitable for academic projects and prototypes.
- It allows quick iteration during model testing.

### 17.3 Parallel Model Execution

The frontend uses `concurrent.futures.ThreadPoolExecutor` to run disease and pest predictions in parallel.

Why?

- Disease and pest models are independent.
- Running them in parallel improves perceived response time.
- The user gets both results together.

---

## 18. Model Loading and Caching

Both disease and pest predictors use `lru_cache`.

Purpose:

- Avoid reloading large models repeatedly.
- Improve Streamlit rerun performance.
- Reduce inference delay after first load.

Disease model:

```python
@lru_cache(maxsize=1)
def load_disease_model():
    return tf.keras.models.load_model(str(model_path))
```

Pest model:

```python
@lru_cache(maxsize=1)
def load_pest_model():
    from ultralytics import YOLO
    return YOLO(MODEL_PATH)
```

The YOLO import is inside the function so the app does not fail at module import time if the dependency is missing.

---

## 19. Installation and Setup

### 19.1 Create Virtual Environment

```powershell
python -m venv venv
```

### 19.2 Activate Virtual Environment

```powershell
venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate again.

### 19.3 Install Dependencies

```powershell
pip install -r requirements.txt
```

### 19.4 Required Model Files

Disease model expected at one of:

```text
E:/College/internship/models/disease_model.keras
E:/College/internship/crop-advisory-ai/models/disease_model.keras
```

Pest model expected at:

```text
E:/College/internship/crop-advisory-ai/models/best.pt
```

### 19.5 Run Streamlit App

```powershell
streamlit run app/main.py
```

Or:

```powershell
python -m streamlit run app/main.py
```

Open:

```text
http://localhost:8501
```

If port 8501 is busy:

```powershell
python -m streamlit run app/main.py --server.port 8511
```

---

## 20. Requirements

Current `requirements.txt`:

```text
tensorflow==2.10.0
numpy==1.23.5
pandas==1.5.3
matplotlib==3.7.5
scikit-learn==1.3.2
opencv-python==4.8.1.78
Pillow==10.4.0
seaborn==0.13.2
jupyter==1.0.0
streamlit
ultralytics
```

Important note:

- TensorFlow 2.10 is commonly used on Windows for compatibility.
- Ultralytics installs the YOLO inference stack.
- PyTorch may be installed as a transitive dependency of Ultralytics.

---

## 21. How to Test Locally

### 21.1 Test Disease and Pest Together

```powershell
python tools/test_models.py
```

### 21.2 Test YOLO Model Loading

```powershell
python tools/test_yolo.py
```

### 21.3 Test Disease Predictor Manually

```powershell
python -c "from PIL import Image; from tools.disease_predictor import predict_disease; print(predict_disease(Image.open('test_images/disease.JPG').convert('RGB')))"
```

Example output:

```python
{'disease': 'Apple___Apple_scab', 'confidence': 97.06}
```

### 21.4 Test Pest Predictor Manually

```powershell
python -c "from PIL import Image; from tools.pest_predictor import predict_pest; print(predict_pest(Image.open('test_images/01123.jpg').convert('RGB')))"
```

---

## 22. Important Debugging Lessons

### 22.1 Disease Model Always Predicting One Class

Observed issue:

```text
Model always returned Corn_(maize)___healthy
```

Root cause:

- The saved model already had MobileNetV2 preprocessing inside the model.
- The predictor also applied external preprocessing.
- This caused double preprocessing.

Fix:

- Remove external `preprocess_input()` from `tools/disease_predictor.py`.
- Send raw resized pixel values to the model.

Correct inference:

```python
img_array = np.array(img, dtype=np.float32)
img_array = np.expand_dims(img_array, axis=0)
prediction = model.predict(img_array, verbose=0)
```

### 22.2 Class Order Mismatch

For classification models, class order must match training order.

This project loads class names from:

```text
datasets/processed/diseases/train
```

and sorts them alphabetically. This must match how `image_dataset_from_directory` assigned labels during training.

### 22.3 Streamlit Import Error

Possible issue:

```text
ModuleNotFoundError: No module named 'app.advisory_pipeline'; 'app' is not a package
```

Reason:

- A root-level `app.py` file can shadow the `app/` directory when importing as a package.

Fix:

- Use local imports inside `app/main.py` when running through Streamlit.
- Or remove/rename root `app.py`.
- Or add proper package structure with `__init__.py` and avoid conflicting names.

### 22.4 TensorFlow CUDA Warning

Warning:

```text
Could not load dynamic library 'cudart64_110.dll'
```

Meaning:

- TensorFlow is looking for GPU libraries.
- If running on CPU, this warning is safe to ignore.

---

## 23. Strengths of the Project

- Combines image classification and object detection.
- Uses two different deep learning frameworks: TensorFlow/Keras and YOLO/PyTorch.
- Includes advisory intelligence instead of only prediction.
- Uses a modular architecture.
- Contains dataset preparation scripts.
- Contains training scripts and inference utilities.
- Uses JSON knowledge base for maintainability.
- Supports symptom validation and risk scoring.
- Good placement project because it connects AI with real-world agriculture.

---

## 24. Limitations

- Disease model is trained mainly on PlantVillage-style images, which may not generalize perfectly to real field images.
- Pest detection quality depends on YOLO training data and image clarity.
- Current advisory recommendations are rule-based and depend on knowledge base completeness.
- The system does not estimate exact infected area from segmentation.
- The system does not provide pesticide dosage.
- Weather, soil, location, and crop stage are not deeply integrated yet.
- The frontend is local Streamlit, not production deployed.

---

## 25. Future Enhancements

Possible improvements:

- Add real-world validation using PlantDoc.
- Add Grad-CAM or heatmap explanation for disease predictions.
- Add bounding box visualization for pest detections.
- Add multilingual support for farmers.
- Add voice input for symptom questions.
- Add weather API integration.
- Add geolocation-based crop advisory.
- Add severity estimation using segmentation.
- Add treatment calendar and reminders.
- Add offline mobile deployment.
- Add database storage for farmer history.
- Add explainable AI report.
- Add confidence thresholds and unknown-class handling.
- Add admin panel for editing knowledge base.

---

## 26. Placement Explanation Strategy

When explaining this project in an interview, use this order:

1. Start with the problem.
2. Explain why agriculture needs early disease and pest detection.
3. Explain the two AI modules.
4. Explain why disease uses classification and pest uses detection.
5. Explain the advisory pipeline.
6. Explain risk scoring.
7. Explain the knowledge base.
8. Mention debugging lessons.
9. Mention limitations honestly.
10. End with future scope.

Sample answer:

> I built a crop disease and pest advisory assistant using Streamlit. The system takes a crop image and runs two AI models: a MobileNetV2-based TensorFlow classifier for disease detection and a YOLO detector for pest detection. After prediction, it asks symptom validation questions, calculates risk based on confidence and field factors, and generates safe recommendations from a JSON knowledge base. The main idea is not just to classify an image, but to convert AI output into useful farmer advisory support.

---

## 27. Resume Points

You can write:

- Developed an AI-powered Crop Disease and Pest Advisory Assistant using Streamlit, TensorFlow, Keras, and YOLO.
- Trained a MobileNetV2 transfer learning model for multi-class crop disease classification.
- Integrated YOLO object detection for pest identification across 102 pest categories.
- Built a rule-based advisory pipeline using symptom validation, risk scoring, and JSON knowledge base recommendations.
- Designed a farmer-friendly Streamlit interface for image upload, prediction visualization, risk input, and advisory generation.
- Implemented model caching and modular inference utilities to improve app performance.
- Prepared and validated agricultural datasets including PlantVillage and IP102.

---

## 28. Common Interview Questions and Answers

### Q1. What is the main goal of your project?

The goal is to detect crop diseases and pests from images and provide advisory recommendations. It helps farmers identify problems early and take preventive or corrective action.

### Q2. Why did you use two models?

Disease detection and pest detection are different tasks. Disease detection is mostly image classification because the entire leaf image corresponds to one class. Pest detection is object detection because pests can be small, multiple, and located anywhere in the image.

### Q3. Why MobileNetV2 for disease detection?

MobileNetV2 is lightweight, efficient, and suitable for transfer learning. It gives a good balance between accuracy and speed, making it useful for practical deployment.

### Q4. Why YOLO for pest detection?

YOLO is an object detection model. It can detect pests and localize them in an image. This is better than classification because pest images may contain multiple insects at different locations.

### Q5. What is transfer learning?

Transfer learning means using a model pretrained on a large dataset, such as ImageNet, and adapting it to a new task. In this project, MobileNetV2 was used as a pretrained feature extractor, and a new classification layer was trained for crop disease classes.

### Q6. What is the role of the symptom engine?

The symptom engine validates the AI prediction using farmer answers. It asks questions related to the predicted disease or pest and calculates a symptom match percentage.

### Q7. What is the role of the risk engine?

The risk engine estimates severity. It uses model confidence, rapid spread, stem damage, and affected crop percentage to calculate a score and classify risk as low, medium, or high.

### Q8. How does the recommendation engine work?

It loads disease and pest guidelines from JSON files. Based on prediction and risk level, it selects appropriate actions, prevention advice, and source categories.

### Q9. Why use a JSON knowledge base?

JSON is simple, readable, and easy to update without changing code. It allows agricultural information to be separated from application logic.

### Q10. What are the limitations?

The disease model may not generalize perfectly to real-world field images because PlantVillage contains controlled images. The recommendations are rule-based and should be validated by experts. The system does not provide exact pesticide dosage.

### Q11. What was one important bug you solved?

The disease model was repeatedly predicting `Corn_(maize)___healthy`. The issue was double preprocessing. The saved model already contained MobileNetV2 preprocessing, but the predictor applied preprocessing again. Removing external preprocessing fixed the problem.

### Q12. How do you calculate confidence?

For the disease classifier, confidence is the maximum softmax probability multiplied by 100. For YOLO, confidence comes from the detection box confidence.

### Q13. How do you handle multiple pest detections?

The pest predictor returns a list of detections. Each detection includes pest name and confidence. The frontend can display the most confident detections and let the user select which one to use for advisory.

### Q14. How is this project useful in real life?

It can help farmers get early warning about possible crop diseases or pest attacks. It can reduce delay in decision-making and guide farmers toward safer, source-backed actions.

### Q15. Can this project be deployed?

Yes. It can be deployed as a Streamlit app, but production deployment would require proper model storage, dependency management, security checks, and possibly cloud or edge hosting.

---

## 29. Technical Terms Explained

### CNN

A Convolutional Neural Network is a deep learning model designed for image data. It extracts spatial features such as edges, textures, patterns, and shapes.

### Transfer Learning

Using a pretrained model and adapting it to a new dataset.

### Softmax

Softmax converts model output logits into probabilities across multiple classes.

### Object Detection

Object detection identifies both the class and location of objects in an image.

### YOLO

YOLO stands for You Only Look Once. It is a fast object detection architecture.

### Risk Scoring

Risk scoring converts multiple field factors into a severity level.

### Knowledge Base

A structured collection of domain information used by the advisory engine.

---

## 30. End-to-End Example

Input:

```text
Farmer uploads tomato leaf image.
```

Disease model output:

```python
{
    "disease": "Tomato___Early_blight",
    "confidence": 91.0
}
```

Pest model output:

```python
[]
```

User answers symptom questions:

```text
Brown spots visible: Yes
Lower leaves affected: Yes
Yellowing: No
```

Risk inputs:

```text
Rapid spread: Yes
Stem damage: No
Crop affected: 60 percent
```

Risk score:

```text
High AI confidence: +2
Rapid spread: +3
Crop affected > 50 percent: +3
Total: 8
Risk: HIGH
```

Recommendation:

```text
- Remove heavily infected leaves or plants.
- Use targeted fungicide guidance from local experts.
- Improve airflow and avoid overhead watering.
- Practice crop rotation next season.
```

---

## 31. Files You Should Know Before an Interview

| File | Why it matters |
|---|---|
| `app/main.py` | Streamlit frontend and full user flow |
| `app/advisory_pipeline.py` | Combines symptom, risk, and recommendation engines |
| `tools/disease_predictor.py` | Disease model inference |
| `tools/pest_predictor.py` | YOLO pest inference |
| `tools/symptom_engine.py` | Symptom validation logic |
| `tools/risk_engine.py` | Risk score calculation |
| `tools/recommendation_engine.py` | Advisory recommendation selection |
| `training/train_disease_model.py` | Disease model training |
| `training/train_efficientnetb2.py` | Pest classifier experiment |
| `tools/check_balanced.py` | Dataset balance verification |
| `knowledge_base/*.json` | Domain advisory data |

---

## 32. Final Summary

The Crop Disease and Pest Advisory Assistant is a complete applied AI project that combines:

- Computer vision
- Deep learning
- Transfer learning
- Object detection
- Rule-based decision support
- Streamlit frontend development
- Agricultural domain knowledge
- Practical debugging and deployment considerations

It is strong for placements because it is not only a model training project. It demonstrates an end-to-end system: data preparation, model development, inference, frontend integration, advisory intelligence, and real-world limitations.

The most important idea to communicate is:

> The project converts crop images into actionable advisory support by combining AI predictions with symptom validation, risk scoring, and knowledge-base recommendations.
