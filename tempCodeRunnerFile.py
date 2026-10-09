# Pandas – Null Value Handling Practice

# Use the given Excel dataset and solve all questions using Pandas.

# 1. Read the Excel file into a DataFrame named df.

import pandas as  pd 
a=pd.read_excel("student_data.xlsx")


# 2. Display the complete DataFrame.


import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)


# 3. Find the total number of null values in each column.

import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b=a.isna().sum()
print(b)

# 4. Find the total number of null values in the complete DataFrame.

import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b=a.isna().sum().sum()
print(a)

# 5. Display all rows where City is null.

import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b=a[a["City"].isna()]
print(b)



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




# Use the given Excel dataset and solve all questions using Pandas.

# 16. Fill null values in Marks with the median Marks.

import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b=a["Marks"].fillna(a["Marks"].median())
print(b)


# 17. Fill null values in City with the most frequently occurring City using mode().


import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b=a["City"].fillna(a["City"].mode())
print(b)


# 18. Use fillna() to fill Marks with 0 and City with "Unknown" in one statement.


import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b=a.fillna({"Age":0,"City":"Unknown"})
print(b)

# 19. Find the row position of Deepak.

import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b =  a.loc[a["Name"] == "Deepak"].index
print(b)

# 20. Access Deepak's row using iloc.

import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b =  a.iloc[a["Name"] == "Deepak"].index
print(b)


#
# Use the given Excel dataset and solve all questions using Pandas.


# 21. Using iloc and fillna(), fill Deepak's City with "London" if his City is null.

import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b =a.iloc[20:21,3]=a.iloc[20:21,3].fillna("London")
print(b)


# 22. Using loc, fill Deepak's City with "London" if his City is null.

import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b =a.loc[20:21,"City"]=a.loc[20:21,"City"].fillna("London")
print(b)

# 23. Display all students whose City is not null.

import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b =a[a["City"].notna()]
print(b)


# 24. Display all students whose Marks are not null.

import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b =a[a["Marks"].notna()]
print(b)


# 25. After filling all required null values, display the final DataFrame.

import pandas as  pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b =a.fillna({"City":"Unknown","Age":0,"Marks":0,"Attendance":0},inplace=True)
print(b)
print(a)


# 26. Check again whether any null values are remaining in the DataFrame.
import pandas as pd 
a=pd.read_excel("student_data.xlsx")
print(a)
b =a.fillna({"City":"Unknown","Age":0,"Marks":0,"Attendance":0},inplace=True)
print(b)
c=a.isna().sum().sum()
print(c)
