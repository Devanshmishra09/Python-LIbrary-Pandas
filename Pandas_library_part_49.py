# Pandas – Rows & Columns Practice

# 1. Read the Excel file into a DataFrame named df.
import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
print(a)

# 2. Display the complete DataFrame.
print(a)
# 3. Add a new column named "Scholarship" and set "Reject" for every student.

import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
print(a)
a["Scholarship"]="Rejected"
print(a)


# 4. Change Scholarship to "Verify" for students whose Attendance is greater than 85 using loc.

import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
print(a)
a["Scholarship"]="Rejected"
b=a.loc[a["Attendance"]>85,"Scholarship"]="Verified"
print(b)
print(a)
# 5. Add a new column named "Bonus_Marks" and store Marks + 5 in it.

import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
print(a)
a["Bonus_Marks"]=a["Marks"]+5
print(a)


# 6. Change the Marks of the student at index 5 to 80 using loc.

import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
print(a)
b=a.loc[5,"Marks"]=80
print(b)
print(a)

# for Range 
import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
b=a.loc[5:20,"Marks"]=80
print(b)
print(a)


# 7. Change the City of the student at index 10 to "London" using loc.

import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
print(a)
b=a.loc[10,"City"]="London"
print(b)
print(a)


# 8. Change the City and Age of the student at index 8 to "Lucknow" and 23 using loc.

import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
print(a)
b=a.loc[8,["City","Age"]]=["Lucknow",23]
print(b)
print(a)
# 9. Access the complete row at position 5 using iloc.

import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
print(a)
b=a.iloc[5]
print(b)



# 10. Access the Name and City of the student at row position 5 using iloc.
import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
print(a)
b=a.iloc[5],["Name","City"]
print(b)



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



# 21. Add a new column named "Department_Code" and set "CS" for CSE students using loc.

import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
a["Department_Code"]=a["Department"]
b=a.loc[a["Department"]=="CSE","Department_Code"]="CS"
print(b)
print(a)
# 22. Add a new column named "Performance" and initially set every row to "Average".
# Then change it to "Excellent" for students whose Marks are greater than 85 using loc.

import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
a["Performance"]="Average"
b=a.loc[a["Marks"]>85,"Performance"]="Excellent"
print(b)
print(a)


# 23. Delete all rows where Marks are less than 50.

import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
b=a.drop(a[a["Marks"]<80].index)
print(b)
print(a)

# 24. After deleting rows, reset the DataFrame index using reset_index().
import pandas as pd 
a=pd.read_excel("Students_Marksheet.xlsx")
b=a.drop(a[a["Marks"]<80].index).reset_index()
print(b)
print(a)




