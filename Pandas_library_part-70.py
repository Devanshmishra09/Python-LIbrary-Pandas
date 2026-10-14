import numpy as np
import pandas as pd

# 1. SETUP MOCK DATA
print("--- Step 1: Mocking ER Patient Records ---")
np.random.seed(88)
n_patients = 120

data = {
    "Patient_ID": range(5001, 5001 + n_patients),
    "Age": np.random.randint(1, 95, n_patients),
    "Systolic_BP": np.random.randint(90, 180, n_patients),
    "Heart_Rate": np.random.randint(50, 140, n_patients),
    "Chief_Complaint": np.random.choice(
        ["Chest Pain", "Fever", "Fracture", "Cough", "Migraine"], n_patients
    ),
}

df = pd.DataFrame(data)

# 2. CATEGORICAL DATA BINNING
print("--- Step 2: Binning Age Groups ---")
# Segment patients into logical lifecycle stages using pd.cut
age_bins = [0, 12, 19, 64, 100]
age_labels = ["Child", "Teen", "Adult", "Senior"]
df["Age_Group"] = pd.cut(df["Age"], bins=age_bins, labels=age_labels)

# 3. CONDITIONAL TRIAGE LOGIC
print("--- Step 3: Determining Critical Status ---")
# Define emergency vital cutoffs: Heart rate > 120 or Blood Pressure > 140
high_hr = df["Heart_Rate"] > 120
high_bp = df["Systolic_BP"] > 140
chest_pain = df["Chief_Complaint"] == "Chest Pain"

# Combine conditions to mark critical urgency status
df["Triage_Status"] = np.where(
    chest_pain | (high_hr & high_bp), "CRITICAL", "STABLE"
)

# 4. COMPREHENSIVE PIPELINE FILTERS
print("--- Step 4: Analyzing Vulnerable Populations ---")
# Group metrics to view baseline vitals across age bands
vitals_by_age = (
    df.groupby("Age_Group", observed=False)
    .agg(
        Avg_Heart_Rate=("Heart_Rate", "mean"),
        Avg_Systolic_BP=("Systolic_BP", "mean"),
        Total_Admissions=("Patient_ID", "count"),
    )
    .round(1)
)
print(vitals_by_age, "\n")

# 5. SORTING AND EXPORTING PRIORITY QUEUES
print("--- Step 5: Generating Emergency Action Queue ---")
# Filter to critical patients and sort them so older patients appear first
emergency_queue = df[df["Triage_Status"] == "CRITICAL"].sort_values(
    by=["Age", "Heart_Rate"], ascending=[False, False]
)

print(
    emergency_queue[["Patient_ID", "Age", "Chief_Complaint", "Triage_Status"]].head()
)
emergency_queue.to_csv("emergency_triage_queue.csv", index=False)
print("\nER Priority Queue exported safely.")
