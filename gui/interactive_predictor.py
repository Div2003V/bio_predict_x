from utils import load_model_and_config
model, le, si = load_model_and_config()
import json
import datetime
from gui.utils import load_model_and_config

def ask_follow_ups(symptom):
    print(f"\n🩺 Follow-up questions for: {symptom}")
    
    duration = input("📆 How long have you had this symptom? (e.g. 2 days 5 hours): ")
    severity = input("⚠️ On a scale of 1-10, how severe is it? ")
    
    # Mock co-symptom options
    related_symptoms_map = {
        "headache": ["blurred vision", "dizziness", "nausea"],
        "fever": ["chills", "sweating", "body ache"],
        "cough": ["sore throat", "shortness of breath", "chest pain"],
        "fatigue": ["sleepiness", "lack of focus", "muscle weakness"],
        "stomach_pain": ["vomiting", "diarrhea", "bloating"],
    }
    
    co_symptoms = related_symptoms_map.get(symptom.lower(), ["none", "none", "none"])
    
    print("❓ Do you also experience any of the following?")
    for i, option in enumerate(co_symptoms, 1):
        print(f"{i}. {option}")
    selected = input("Choose a number (or press enter to skip): ")
    
    try:
        co_symptom = co_symptoms[int(selected)-1] if selected else "none"
    except:
        co_symptom = "none"
    
    return {
        "symptom": symptom,
        "duration": duration,
        "severity": severity,
        "co_symptom": co_symptom
    }

def interactive_predict():
    model, label_encoder, symptom_index = load_model_and_config()

    all_symptoms = list(symptom_index.keys())
    print("\n🩺 Welcome to BioPredictX: Intelligent Disease Diagnosis 🧠\n")
    
    patient_data = {
        "timestamp": str(datetime.datetime.now()),
        "symptoms": []
    }

    while True:
        print("📋 Available symptoms to choose from:")
        for i, sym in enumerate(all_symptoms, 1):
            print(f"{i}. {sym}")
        
        selected = input("\n🔍 Enter the number of your symptom (or type 'done' to finish): ").strip()
        if selected.lower() == "done":
            break

        try:
            symptom_idx = int(selected) - 1
            if 0 <= symptom_idx < len(all_symptoms):
                symptom = all_symptoms[symptom_idx]
                follow_up_data = ask_follow_ups(symptom)
                patient_data["symptoms"].append(follow_up_data)
            else:
                print("❗ Invalid choice.")
        except ValueError:
            print("❗ Please enter a number or 'done'.")

    # Prediction input vector
    input_data = [0] * len(symptom_index)
    for entry in patient_data["symptoms"]:
        key = entry["symptom"]
        if key in symptom_index:
            input_data[symptom_index[key]] = 1

    if sum(input_data) == 0:
        print("\n⚠️ No valid symptoms selected. Exiting.")
        return

    prediction = model.predict([input_data])[0]
    predicted_disease = label_encoder.inverse_transform([prediction])[0]

    print(f"\n🧾 Based on the symptoms provided, the predicted disease is: **{predicted_disease}**\n")
    patient_data["predicted_disease"] = predicted_disease

    # Save to logs
    with open("patient_logs.json", "a") as f:
        f.write(json.dumps(patient_data) + "\n")

    print("📁 Patient interaction saved to patient_logs.json ✅")

if __name__ == "__main__":
    while True:
        interactive_predict()
        again = input("\n🔁 Do you want to diagnose another patient? (yes/no): ").strip().lower()
        if again != "yes":
            print("👋 Thanks for using BioPredictX. Stay healthy!")
            break
