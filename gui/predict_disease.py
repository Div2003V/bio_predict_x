import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox
import joblib
import json
import numpy as np
import datetime
import os
from gui.utils import load_model_and_config, log_prediction

# Load model, encoder, and symptom index
model, label_encoder, symptom_index = load_model_and_config()

SYMPTOMS = list(symptom_index.keys())
NUM_SYMPTOMS = 5

# GUI Setup
root = tk.Tk()
root.title("🧬 Disease Predictor")
root.geometry("600x500")
root.configure(bg="#f2f2f2")

tk.Label(root, text="Disease Prediction from Symptoms", font=("Helvetica", 18, "bold"), bg="#f2f2f2", fg="#333").pack(pady=20)

# Symptom Dropdowns
dropdown_vars = []
for i in range(NUM_SYMPTOMS):
    tk.Label(root, text=f"Symptom {i+1}", bg="#f2f2f2", anchor="w").pack(pady=(5, 0), padx=20, fill="x")
    var = tk.StringVar()
    var.set("None")
    dropdown = tk.OptionMenu(root, var, "None", *SYMPTOMS)
    dropdown.config(width=50)
    dropdown.pack(pady=2)
    dropdown_vars.append(var)

def predict():
    selected_symptoms = [var.get() for var in dropdown_vars if var.get() != "None"]
    if not selected_symptoms:
        messagebox.showerror("Error", "Please select at least one symptom.")
        return

    input_vector = np.zeros(len(symptom_index))
    for symptom in selected_symptoms:
        index = symptom_index[symptom]
        input_vector[index] = 1

    prediction = model.predict([input_vector])[0]
    disease = label_encoder.inverse_transform([prediction])[0]

    # Log prediction
    log_prediction(selected_symptoms, disease)

    messagebox.showinfo("Prediction", f"Predicted Disease: {disease}")

tk.Button(root, text="Predict Disease", command=predict, bg="#4CAF50", fg="white", font=("Helvetica", 12), padx=10, pady=5).pack(pady=30)

root.mainloop()
