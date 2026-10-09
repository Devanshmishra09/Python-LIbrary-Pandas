# Pandas – Null Value Handling Practice

#  rows where City is null.

# 6. Display all rows where Marks is null.

import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b=a[a["Marks"].isna()]
print(b)


# 7. Display all rows where Attendance is null.

import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b=a[a["Attendance"].isna()]
print(b)

# 8. Remove all rows where Marks is null using dropna().

import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b=a.dropna(subset="Marks")
print(b)


# 9. Remove all rows where City is null using dropna(subset=[]).

import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b=a.dropna(subset="City")
print(b)

# 10. Remove rows where either Marks or Attendance is null.
import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b=a.dropna(subset=["Marks","Attendance"])
print(b)