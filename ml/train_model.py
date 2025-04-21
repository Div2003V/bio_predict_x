import pandas as pd
import numpy as np
import joblib
import json
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from pathlib import Path

# Load dataset
df = pd.read_csv("data/disease_symptom_dataset.csv")

# Split features & target
X = df.drop("Disease", axis=1)
y = df["Disease"]

# Encode disease labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model and encoders
Path("models").mkdir(exist_ok=True)

joblib.dump(model, "models/disease_model.joblib")
joblib.dump(le, "models/label_encoder.joblib")

# Save symptom index for GUI reference
symptom_index = {symptom: idx for idx, symptom in enumerate(X.columns)}
with open("models/symptom_index.json", "w") as f:
    json.dump(symptom_index, f, indent=4)

# Print accuracy
accuracy = model.score(X_test, y_test)
print(f"✅ Model trained successfully with {accuracy * 100:.2f}% accuracy.")
