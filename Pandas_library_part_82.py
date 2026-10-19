import numpy as np
import pandas as pd

# ==============================================================================
# 1. GENERATE PRACTICE DATAFRAME WITH DATE AND TIME
# ==============================================================================
# Setting a constant date range to build our base timeline
dates = pd.date_range(start="2026-10-15 08:00:00", periods=5, freq="D")

# Building a structured dictionary with mock tracking data
data = {
    "timestamp": dates,
    "location": ["Lucknow", "Delhi", "Mumbai", "Lucknow", "Bangalore"],
    "sensor_reading": [120, 85, 150, 65, 110],
    "status": ["Active", "Active", "Inactive", "Active", "Inactive"],
}

# Constructing our core Pandas DataFrame
df = pd.DataFrame(data)

# Extracting standalone date and time components via the .dt accessor
df["date_only"] = df["timestamp"].dt.date
df["time_only"] = df["timestamp"].dt.time

# ==============================================================================
# 2. APPLYING CONDITIONAL FILTERING WITH 'WHERE'
# ==============================================================================
# Question A: Use pandas.where() to hide readings above 110 (replace with NaN)
df["bounded_readings"] = df["sensor_reading"].where(df["sensor_reading"] <= 110)

# Question B: Use numpy.where() to classify locations based on a local flag
df["is_local"] = np.where(df["location"] == "Lucknow", "Local", "Remote")

# ==============================================================================
# 3. INTERACTIVE CHALLENGE PRACTICE QUESTIONS
# ==============================================================================
questions = [
    {
        "id": 1,
        "q": "Which dt attribute extracts only the clock time from a datetime series?",
        "options": ["A) .dt.clock", "B) .dt.time", "C) .dt.hour", "D) .dt.timestamp"],
        "answer": "B",
    },
    {
        "id": 2,
        "q": "How does pandas.DataFrame.where() handle rows that evaluate to False?",
        "options": ["A) Drops them", "B) Kept as NaN / custom value", "C) Raises error", "D) Inverts them"],
        "answer": "B",
    },
    {
        "id": 3,
        "q": "Which native Pandas write method exports a DataFrame directly to a CSV file?",
        "options": ["A) df.save_csv()", "B) df.write_csv()", "C) df.to_csv()", "D) df.export_csv()"],
        "answer": "C",
    },
]

# Displaying questions for learning evaluation
print("--- PANDAS ASSESSMENT QUESTIONS ---")
for item in questions:
    print(f"\nQuestion {item['id']}: {item['q']}")
    for opt in item["options"]:
        print(opt)
    print(f"Correct Answer Key: {item['answer']}")

# ==============================================================================
# 4. EXECUTING THE WRITE METHOD TO PERSIST DATA
# ==============================================================================
# Saving our processed metrics out to a local storage file path safely
output_filepath = "pandas_datetime_report.csv"
df.to_csv(output_filepath, index=False)

print("\n--- DATAFRAME SAMPLE OUTPUT ---")
print(df.head())
print(f"\nSuccess: DataFrame written perfectly to '{output_filepath}'.")
# ==============================================================================
