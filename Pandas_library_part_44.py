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
