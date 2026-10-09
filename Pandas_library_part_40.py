# Pandas – Null Value Handling Practice


# 11. Fill all null values in the City column with "Unknown".

import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b=a["City"].fillna("Unknown")
print(b)

# 12. Fill all null values in the Marks column with 0.

import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b=a["Marks"].fillna(0)
print(b)

# 13. Fill all null values in the Attendance column with 0.

import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b=a["Attendance"].fillna(0)
print(b)

# 14. Fill null values in Marks with the average Marks.

import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b=a["Marks"].fillna(a["Marks"].mean())
print(b)

# 15. Fill null values in Age with the average Age.


import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b=a["Age"].fillna(a["Age"].mean())
print(b)
