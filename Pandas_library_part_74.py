# Pandas Practice Worksheet

# Topics: Inner Join, Merge, Join, GroupBy & Duplicate Rows

# Difficulty: Medium to Hard
# Total Questions: 5

# ---

# Dataset 1: Students



# Question 3: Department-wise Analysis

import pandas as pd

students = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105, 106, 107],
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Rohit", "Simran", "Karan"],
    "Department": ["CSE", "IT", "CSE", "ECE", "IT", "CSE", "ECE"],
    "City": ["Lucknow", "Delhi", "Lucknow", "Kanpur", "Delhi", "Noida", "Kanpur"],
    "Attendance": [90, 75, 85, 60, 95, 80, 70]
})

marks = pd.DataFrame({
    "Student_ID": [101, 102, 103, 105, 106, 108, 109],
    "Python": [88, 65, 92, 78, 85, 70, 60],
    "SQL": [80, 72, 95, 82, 79, 75, 55],
    "Project": [90, 60, 96, 85, 88, 72, 58]
})

departments = pd.DataFrame({
    "Department": ["CSE", "IT", "ECE", "ME"],
    "HOD": ["Dr. Sharma", "Dr. Verma", "Dr. Singh", "Dr. Gupta"],
    "Annual_Fee": [90000, 80000, 85000, 75000]
})
# 1. Perform an inner join between "students" and "marks".

result=students.merge(marks,on="Student_ID",how="outer")
print(result)

# 2. Calculate the total number of matching students in each department.
matching=students.merge(marks,on="Student_ID",how="inner")
print(matching)

# 3. Calculate the average Python marks for each department.
b=matching.groupby("Department")["Python"].mean()
print(b)


