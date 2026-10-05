# PANDAS – SELECTION & FILTERING PRACTICE

# Dataset:
# Record.xlsx
# Instructions:
# * Use Pandas to solve all questions.
# * Use only the concepts taught so far:
#   - Selecting columns
#   - Selecting rows
#   - loc
#   - iloc
#   - Conditional selection
#   - &, |
#   - isin()
# * Do not use groupby(), sort_values(), apply(), merge(), or aggregation functions.

# SECTION F – MEDIUM LEVEL
# --------------------------------------------------

# 1. Display Name, Age, Marks, and Attendance
#     where Marks > 75 AND Attendance > 80.
import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[(a["Marks"]>75)& (a["Attendance"]>80),["Name","Age","Marks","Attendance"]]
print(b)


# 2. Display Name, City, and Marks
#     for students from Lucknow with Marks > 80.

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[(a["Marks"]>80)& (a["City"]=="Lucknow"),["Name","City","Marks"]]
print(b)



# 3. Display Name, Department, and Exam_Status
#     for students from CSE or IT who have not failed.

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[(a["Department"].isin(["CSE","IT"]))& (a["Exam_Status"]=="Pass"),["Name","Department","Exam_Status"]]
print(b)



# 4. Using loc, display Name, Age, and Marks
#     where Age > 20 AND Marks > 75.

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[(a["Marks"]>75)& (a["Age"]>20),["Name","Age","Marks"]]
print(b)




# 5. Using iloc, select the first 15 rows
#     and only Name, Department, and Marks.

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.iloc[0:15,[1,5,9]]
print(b)



# 6. Display Name, City, Marks, and Exam_Status
#     for students from Lucknow or Delhi
#     with Marks > 75.


import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[(a["Marks"]>75)& (a["City"].isin(["Lucknow","Delhi"])),["Name","City","Marks","Exam_Status"]]
print(b)

