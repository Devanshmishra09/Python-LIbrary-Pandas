# Pandas – Null Value Handling Practice

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
