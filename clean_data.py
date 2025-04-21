import pandas as pd

df = pd.read_csv('data/disease_symptom_dataset.csv')

# Replace all non-numeric values in symptom columns with 0
symptom_cols = df.columns[:-1]  # All except 'Disease'
for col in symptom_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

# Clean Disease column (remove rows where disease is missing)
df = df[df['Disease'].notnull()]

df.to_csv('data/disease_symptom_dataset_clean.csv', index=False)
print("✅ Cleaned dataset saved as disease_symptom_dataset_clean.csv")
