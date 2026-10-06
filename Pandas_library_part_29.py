# : PANDAS – SELECTION & FILTERING PRACTICE

# Dataset: Record.xlsx: 

# • Use Pandas to solve all questions. • Use only the concepts taught so far:
# - Selecting columns - Selecting rows - loc - iloc - Conditional selection - &, | - isin() 
# • Do not use groupby(), sort_values(), apply(), merge(), or aggregation functions. 

# -------------------------------------------------- 
# SECTION E – USING isin() 
# -------------------------------------------------- 
# 1. Select students whose City is Lucknow, Delhi, or Kanpur.

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[a["City"].isin(["Lucknow","Delhi","Kanpur"])]
print(b)

 
# 2. Select students whose Department is CSE or IT. 

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[a["Department"].isin(["CSE","IT"])]
print(b)


# 3. From students belonging to CSE or ECE, display only Name, Department, and Marks.

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[a["Department"].isin(["CSE","IT"]),["Name","Department","Marks"]]
print(b)

