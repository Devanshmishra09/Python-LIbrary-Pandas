"""
Data Cleaning and Profiling Pipeline
Author: GitHub Contributor
Description: A production-ready pipeline demonstrating structural data cleaning,
             outlier detection using IQR, and handling messy data text fields.
Topic: pandas, data-cleaning, outlier-detection, pipeline
"""

import numpy as np
import pandas as pd

# ==========================================
# 1. GENERATING MESSY REAL-WORLD DATA
# ==========================================
print("--- Step 1: Generating Messy Dataset ---")
np.random.seed(101)
n_rows = 2000

data = {
    "User_ID": [f" USR-{x:04d} " for x in range(n_rows)],  # Trailing/leading spaces
    "Join_Age": np.random.choice(
        [25, 34, 45, np.nan, 19, 120, -5], p=[0.4, 0.3, 0.2, 0.05, 0.03, 0.01, 0.01], size=n_rows
    ),
    "Salary_Raw": np.random.choice(
        ["$50,000", "$65,000", "$120,000", "UNKNOWN", "$85,000"], size=n_rows
    ),
    "Department": np.random.choice(
        [" sales ", "Eng.", "engineering", "SALES", "HR"], size=n_rows
    ),
    "Score": np.random.normal(loc=75, scale=12, size=n_rows),
}

df_messy = pd.DataFrame(data)
# Add explicit duplicated rows to clean later
df_messy = pd.concat([df_messy, df_messy.iloc[:50]], ignore_index=True)
print(f"Messy dataframe initialized with {len(df_messy)} rows.\n")

# ==========================================
# 2. STRING SANITIZATION & STRIP OPERATIONS
# ==========================================
print("--- Step 2: Cleaning Text and ID Columns ---")
# Strip whitespaces and standardize ID formats
df_messy["User_ID"] = df_messy["User_ID"].str.strip().str.upper()

# Standardize categorical categories using string replacements mapping
dept_mapping = {
    "ENG.": "Engineering",
    "ENGINEERING": "Engineering",
    "SALES": "Sales",
    " sales ": "Sales",
    "HR": "Human Resources",
}
df_messy["Department"] = df_messy["Department"].str.strip().str.title()
df_messy["Department"] = df_messy["Department"].replace({"Eng.": "Engineering"})
print("Unique departments after cleaning:", df_messy["Department"].unique(), "\n")

# ==========================================
# 3. PARSING NUMERIC VALUES FROM TEXT STRINGS
# ==========================================
print("--- Step 3: Cleaning and Converting Financial Strings ---")
# Remove currency symbols, commas, handle 'UNKNOWN' text safely, convert to float
df_messy["Salary"] = (
    df_messy["Salary_Raw"]
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)
df_messy["Salary"] = pd.to_numeric(df_messy["Salary"], errors="coerce")

# Impute missing salaries with the median salary of the dataset
median_salary = df_messy["Salary"].median()
df_messy["Salary"].fillna(median_salary, inplace=True)
df_messy.drop(columns=["Salary_Raw"], inplace=True)
print("Salary conversion completed.\n")

# ==========================================
# 4. REMOVING DUPLICATES & INVALID DATA
# ==========================================
print("--- Step 4: Deduplication and Structural Logic Filtering ---")
initial_count = len(df_messy)
df_messy.drop_duplicates(subset=["User_ID"], keep="first", inplace=True)
print(f"Removed {initial_count - len(df_messy)} duplicate records.")

# Drop logically impossible ages
df_messy = df_messy[(df_messy["Join_Age"] >= 18) & (df_messy["Join_Age"] <= 100)]
# Handle remaining NaNs in Age by column mean
df_messy["Join_Age"].fillna(int(df_messy["Join_Age"].mean()), inplace=True)
print(f"Remaining active rows after structure filter: {len(df_messy)}\n")

# ==========================================
# 5. STATISTICAL OUTLIER DETECTION (IQR)
# ==========================================
print("--- Step 5: Detecting and Trimming Performance Score Outliers ---")
Q1 = df_messy["Score"].quantile(0.25)
Q3 = df_messy["Score"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Segmenting outliers vs normal observations
outliers = df_messy[(df_messy["Score"] < lower_bound) | (df_messy["Score"] > upper_bound)]
df_clean = df_messy[(df_messy["Score"] >= lower_bound) & (df_messy["Score"] <= upper_bound)]

print(f"Identified {len(outliers)} statistical outliers based on Score.")
print(f"Final cleaned dataset shape: {df_clean.shape}\n")
print(df_clean.describe().T)

