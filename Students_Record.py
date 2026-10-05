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

# --------------------------------------------------
# SECTION A – BASIC SELECTION
# --------------------------------------------------

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)


# 1. Select only the Name column.
import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a["Name"]
print(b)


# 2. Select the Name, Age, City, and Marks columns.
import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a[["Name","Age","City","Marks"]]
print(b)


# 3. Select the first 7 rows using iloc.
import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.iloc[0:8:]
print(b)


# 4. Select rows from index 5 to 12 using iloc.
import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.iloc[5:13:]
print(b)


# 5. Select rows at index 2, 6, 10, and 15.
import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.iloc[[2,5,10,15]]
print(b)

# --------------------------------------------------
# SECTION B – LOC AND ILOC
# --------------------------------------------------

# 6. Using loc, select Name, Department, and Marks from index 3 to 10.
 
import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[3:11,["Name","Department","Marks"]]
print(b)


# 7. Using iloc, select the first 8 rows and only the following columns:
#    Name, Gender, Age, and Marks.

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.iloc[0:8,[1,2,3,9]]
print(b)


# 8. Using loc, select the Name and Fees_Paid of the student at index 5.

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[5,["Name","Fees_Paid"]]
print(b)


# --------------------------------------------------
# SECTION C – CONDITIONAL SELECTION
# --------------------------------------------------

# 9. Select students whose Marks are greater than 80.

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[a["Marks"]>80]
print(b)


# 10. Select students whose Attendance is less than 80.

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[a["Attendance"]<80]
print(b)


# 11. Select students whose Department is CSE.

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[a["Department"]=="CSE"]
print(b)



# 12. Select students whose Exam_Status is Fail.

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[a["Exam_Status"]=="Fail"]
print(b)


#--------------------------------------------------
# SECTION D – MULTIPLE CONDITIONS
# --------------------------------------------------

# 13. Select students whose Marks are greater than 80
#     AND Attendance is greater than 85.

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[(a["Marks"]>80)&(a["Attendance"]>85)]
print(b)



# 14. Select students whose Age is greater than 20
#     AND Department is CSE.

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[(a["Age"]>20)&(a["Department"]=="CSE")]
print(b)




# 15. Select students who are from Lucknow OR Delhi.

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b = a.loc[a["City"].isin(["Lucknow", "Delhi"])]
print(b)



# 16. Select students whose Marks are less than 70
#     OR Attendance is less than 75.


import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[(a["Marks"]<70)&(a["Attendance"]<75)]
print(b)


# SECTION E – USING isin()
# --------------------------------------------------

# 17. Select students whose City is Lucknow, Delhi, or Kanpur.

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[a["City"].isin(["Lucknow","Delhi","Kanpur"])]
print(b)

# 18. Select students whose Department is CSE or IT.


import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[a["Department"].isin(["CSE","IT"])]
print(b)


# 19. From students belonging to CSE or ECE,
#     display only Name, Department, and Marks.

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[a["Department"].isin(["CSE","ECE"]),["Name","Department","Marks"]]
print(b)


# SECTION F – MEDIUM LEVEL
# --------------------------------------------------

# 20. Display Name, Age, Marks, and Attendance
#     where Marks > 75 AND Attendance > 80.
import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[(a["Marks"]>75)& (a["Attendance"]>80),["Name","Age","Marks","Attendance"]]
print(b)


# 21. Display Name, City, and Marks
#     for students from Lucknow with Marks > 80.

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[(a["Marks"]>80)& (a["City"]=="Lucknow"),["Name","City","Marks"]]
print(b)



# 22. Display Name, Department, and Exam_Status
#     for students from CSE or IT who have not failed.

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[(a["Department"].isin(["CSE","IT"]))& (a["Exam_Status"]=="Pass"),["Name","Department","Exam_Status"]]
print(b)


# 23. Using loc, display Name, Age, and Marks
#     where Age > 20 AND Marks > 75.

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[(a["Marks"]>75)& (a["Age"]>20),["Name","Age","Marks"]]
print(b)


# 24. Using iloc, select the first 15 rows
#     and only Name, Department, and Marks.

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.iloc[0:15,[1,5,9]]
print(b)



# 25. Display Name, City, Marks, and Exam_Status
#     for students from Lucknow or Delhi
#     with Marks > 75.


import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[(a["Marks"]>75)& (a["City"].isin(["Lucknow","Delhi"])),["Name","City","Marks","Exam_Status"]]
print(b)

