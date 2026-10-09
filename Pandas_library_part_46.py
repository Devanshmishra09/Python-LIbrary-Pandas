# Pandas – Rows & Columns Practice

# 11. Change the Marks of the student at row position 7 to 95 using iloc.

import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
print(a)
b=a.iloc[7,6]=95
print(b)
print(a)

# 12. Change the City of the student at row position 12 to "Mumbai" using iloc.

import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
print(a)
b=a.iloc[12,3]="Mumbai"
print(b)
print(a)


# 13. Add a new student as the last row with the following details:
#     Student_ID = 231
#     Name = "Raj"
#     Department = "CSE"
#     City = "Lucknow"
#     Age = 22
#     Marks = 88
#     Attendance = 92
#     Exam_Status = "Pass"

import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
print(a)
b=a.loc[len(a)]=[231,"Raj","CSE","Lucknow",22,88,92,"Pass"]
print(b)
print(a)


# 14. Add a new column named "Result" and initially set every row to "Fail".

import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
print(a)
a["Result"]="Fail"
print(a)


# 15. Using loc, change Result to "Pass" for students whose Marks are greater than or equal to 40.
import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
a["Result"]="Fail"
b=a.loc[a["Marks"]>=85,"Result"]="Pass"
print(b)
print(a)