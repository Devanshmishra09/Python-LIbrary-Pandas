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