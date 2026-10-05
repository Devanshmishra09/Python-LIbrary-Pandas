# : PANDAS – SELECTION & FILTERING PRACTICE

# Dataset: Record.xlsx: 

# • Use Pandas to solve all questions. • Use only the concepts taught so far:
# - Selecting columns - Selecting rows - loc - iloc - Conditional selection - &, | - isin() 
# • Do not use groupby(), sort_values(), apply(), merge(), or aggregation functions. 


# -------------------------------------------------- 
# SECTION B – LOC AND ILOC 
# -------------------------------------------------- 

# 1. Using loc, select Name, Department, and Marks from index 3 to 10. 

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[3:10,["Name","Department","Marks"]]
print(b)


# 2. Using iloc, select the first 8 rows and only the following columns: Name, Gender, Age, and Marks. 

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.iloc[0:8,[1,2,3,9]]
print(b)


# 3. Using loc, select the Name and Fees_Paid of the student at index 5

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[5,["Name","Fees_Paid"]]
print(b)


