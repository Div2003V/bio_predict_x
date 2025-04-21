import pandas as pd
import random

# Define 50 realistic symptoms
symptoms = [
    "fever", "cough", "headache", "fatigue", "nausea", "vomiting", "diarrhea", "chest_pain", "shortness_of_breath", "sore_throat",
    "joint_pain", "muscle_pain", "rash", "dizziness", "abdominal_pain", "loss_of_appetite", "blurred_vision", "chills", "weight_loss", "sweating",
    "anxiety", "depression", "insomnia", "palpitations", "back_pain", "ear_pain", "runny_nose", "congestion", "sneezing", "eye_pain",
    "yellow_skin", "yellow_eyes", "dry_mouth", "swollen_lymph_nodes", "bloody_stool", "frequent_urination", "burning_urination", "memory_loss", "itching", "wheezing",
    "hallucinations", "irritability", "confusion", "bruising", "bleeding_gums", "hair_loss", "numbness", "tingling", "red_eyes", "dry_skin"
]

# 20 diseases
diseases = [
    "Malaria", "Dengue", "Typhoid", "Tuberculosis", "Covid-19", "Influenza", "Hepatitis A", "Hepatitis B", "Pneumonia", "Asthma",
    "Diabetes", "Hypertension", "Arthritis", "Migraine", "Jaundice", "Chickenpox", "Measles", "Common Cold", "Kidney Stones", "Depression"
]

# Generate 1000 random samples
data = []
for _ in range(1000):
    row = [random.randint(0, 1) for _ in symptoms]
    disease = random.choice(diseases)
    row.append(disease)
    data.append(row)

# Create DataFrame
df = pd.DataFrame(data, columns=symptoms + ["Disease"])

# Save to CSV
df.to_csv("data/disease_symptom_dataset.csv", index=False)
print("✅ Generated synthetic dataset with 1000 rows and saved to data/disease_symptom_dataset.csv")
