# Pandas Practice Worksheet

# Topics: Inner Join, Merge, Join, GroupBy & Duplicate Rows

# Difficulty: Medium to Hard
# Total Questions: 5

# ---

# Question 2: Department Details Join

# 1. First merge "students" and "marks" using an inner join.
# 2. Merge the result with "departments" using the "Department" column.
# 3. Filter students belonging to CSE or IT whose attendance is at least 80.
# 4. Display only "Name", "Department", "HOD", "Annual_Fee" and "Total_Marks".



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


# 1. First merge "students" and "marks" using an inner join.

result=students.merge(marks,on="Student_ID",how="inner")
print(result)

# 2. Merge the result with "departments" using the "Department" column.
a=result.merge(departments,on="Department",how="inner")
print(a)

# 3. Filter students belonging to CSE or IT whose attendance is at least 80.

b=a[(a["Department"].isin(["CSE","IT"])) & (a["Attendance"]>80)]
print(b)

# 4. Display only "Name", "Department", "HOD", "Annual_Fee" and "Total_Marks".

print(a[["Name","Department","HOD","Annual_Fee"]])

