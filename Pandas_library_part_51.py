import pandas as pd

data = {
    "emp_id": ["E1", "E2", "E3", "E4", "E5", "E6", "E7"],
    "name": ["Aman", "Priya", "Rohit", "Sneha", "Vikas", "Neha", "Karan"],
    "department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance"],
    "experience_yrs": [5, 2, 8, 4, 6, 3, 10],
    "salary": [75000, 50000, 120000, 65000, 72000, 68000, 135000],
    "rating": [4.2, 3.8, 4.9, 4.0, 3.5, 4.1, 4.8],
    "remote_status": [True, False, True, False, True, False, True]
}
df = pd.DataFrame(data)
df.to_excel("02_hr_analytics.xlsx", index=False)

# Q1: Department count and avg salary
dept_stats = df.groupby("department").agg(emp_count=("emp_id", "count"), avg_salary=("salary", "mean"))
print("Q1 - Dept Stats:\n", dept_stats)

# Q2: Most experienced employee
max_exp_emp = df.loc[df["experience_yrs"].idxmax()]
print("\nQ2 - Most Experienced:\n", max_exp_emp[["name", "experience_yrs"]])

# Q3: Conditional Bonus calculation
df["bonus"] = df.apply(lambda row: row["salary"] * 0.10 if row["rating"] > 4.0 else row["salary"] * 0.05, axis=1)
print("\nQ3 - Bonus Added:\n", df[["name", "salary", "bonus"]])

# Q4: Remote vs Non-Remote average salary
remote_comp = df.groupby("remote_status")["salary"].mean()
print("\nQ4 - Remote Salary Comparison:\n", remote_comp)

# Q5: Sort by Rating descending
sorted_df = df.sort_values(by="rating", ascending=False)
print("\nQ5 - Top Rated Employees:\n", sorted_df[["name", "rating"]])