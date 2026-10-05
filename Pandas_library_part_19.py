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
# print(a)

     # 1. Select only the Name column.
b=a["Name"]
print(b)


     # 2. Select the Name, Age, City, and Marks columns.
c=a[["Name","Age","City","Marks"]]
print(c)


     # 3. Select the first 7 rows using iloc.
d=a.iloc[0:8:]
print(d)


     # 4. Select rows from index 5 to 12 using iloc.
e=a.iloc[5:13:]
print(e)

     # 5. Select rows at index 2, 6, 10, and 15.
f=a.iloc[[2,5,10,15]]
print(f)