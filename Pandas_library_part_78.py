# Program 1: Student Marks Analysis and Grade Calculator
# Description: Creates a student DataFrame, calculates total, average, and grades.

import numpy as np
import pandas as pd


def initialize_student_data():
    """Initializes raw dictionary data for student scores."""
    data = {
        "Roll_No": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
        "Name": [
            "Aarav",
            "Vivaan",
            "Aditya",
            "Vihaan",
            "Arjun",
            "Sai",
            "Reyansh",
            "Ayaan",
            "Krishna",
            "Ishaan",
        ],
        "Math": [85, 42, 90, 75, 63, 88, 95, 52, 79, 68],
        "Science": [78, 65, 85, 80, 58, 92, 89, 60, 74, 71],
        "English": [82, 55, 88, 70, 72, 85, 91, 58, 81, 76],
        "Computer": [90, 70, 95, 85, 80, 95, 98, 68, 85, 82],
    }
    return pd.DataFrame(data)


def compute_metrics(df):
    """Computes total, average, percentage, and assigned grades."""
    df["Total_Marks"] = df[["Math", "Science", "English", "Computer"]].sum(
        axis=1
    )
    df["Average_Score"] = df["Total_Marks"] / 4.0
    df["Percentage"] = (df["Total_Marks"] / 400.0) * 100.0

    def assign_grade(pct):
        if pct >= 85:
            return "A+"
        elif pct >= 75:
            return "A"
        elif pct >= 65:
            return "B"
        elif pct >= 50:
            return "C"
        else:
            return "F"

    df["Grade"] = df["Percentage"].apply(assign_grade)
    return df


def display_summary(df):
    """Prints top performers and subject averages."""
    print("=== FULL STUDENT PERFORMANCE DATAFRAME ===")
    print(df.to_string(index=False))
    print("\n" + "=" * 45)
    print("=== SUBJECT-WISE AVERAGE SCORES ===")
    subjects = ["Math", "Science", "English", "Computer"]
    for sub in subjects:
        print(f"{sub} Average: {df[sub].mean():.2f}")
    print("\n=== TOP PERFORMER ===")
    top_student = df.loc[df["Percentage"].idxmax()]
    print(
        f"Rank 1: {top_student['Name']} (Roll No: {top_student['Roll_No']}) with {top_student['Percentage']:.2f}%"
    )


def main():
    student_df = initialize_student_data()
    processed_df = compute_metrics(student_df)
    display_summary(processed_df)


if __name__ == "__main__":
    main()
