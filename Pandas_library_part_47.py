# Pandas – Rows & Columns Practice


# 16. Create a new column named "Attendance_Status" and set "Good" for students whose Attendance is greater than 85 and "Poor" 
# otherwise using the loc approach.

import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
print(a)
a["Attendance_status"]="Good"
b=a.loc[a["Attendance"]<80,"Attendance_status"]="Poor"
print(b)
print(a)

# 17. Delete the row at index 5.

import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
b=a.drop([5])
print(b)
print(a)


# 18. Delete rows at indexes 8, 12 and 15.

import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
b=a.drop([5,12,15])
print(b)
print(a)

# 19. Delete the "City" column using drop().

import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
b=a.drop( columns="City")
print(b)
print(a)

# 20. Delete both "Age" and "Exam_Status" columns using drop().
import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
b=a.drop( columns=["Age","Exam_Status"])
print(b)
print(a)
