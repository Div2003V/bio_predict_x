import joblib
import json
import os
from datetime import datetime

def load_model_and_config():
    model = joblib.load("models/disease_model.joblib")
    label_encoder = joblib.load("models/label_encoder.joblib")
    
    with open("models/symptom_index.json", "r") as f:
        symptom_index = json.load(f)

    return model, label_encoder, symptom_index

def log_prediction(symptoms, prediction):
    log_file_path = os.path.join("logs", "prediction_history.log")
    
    with open(log_file_path, "a") as log_file:
        log_file.write(f"{datetime.now()} - Symptoms: {symptoms} -> Predicted: {prediction}\n")
