# Pandas – Rows & Columns Practice


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



