# Pandas Practice Worksheet

# Topics: Inner Join, Merge, Join, GroupBy & Duplicate Rows

# Difficulty: Medium to Hard
# Total Questions: 5

# ---

# Dataset 1: Students

# Question 1: Student Marks Inner Join

# 1. Merge "students" and "marks" using "Student_ID" with an inner join.
# 2. Create a "Total_Marks" column by adding Python, SQL and Project marks.
# 3. Sort the result by "Total_Marks" in descending order.
# 4. Display the top 3 students.


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

# Question 1: Student Marks Inner Join

# 1. Merge "students" and "marks" using "Student_ID" with an inner join.

Merge=students.merge(marks,on="Student_ID",how="inner")
print(Merge)


# 2. Create a "Total_Marks" column by adding Python, SQL and Project marks.

Merge["Total_Marks"]=Merge["Python"]+Merge["SQL"]+Merge["Project"]
print(Merge)

# 3. Sort the result by "Total_Marks" in descending order.

b=Merge.sort_values("Total_Marks",ascending=False)
print(b)

# 4. Display the top 3 students.

print(Merge.head(3))
