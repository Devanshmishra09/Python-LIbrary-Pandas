# : PANDAS – SELECTION & FILTERING PRACTICE

# Dataset: Record.xlsx: 

# • Use Pandas to solve all questions. • Use only the concepts taught so far:
# - Selecting columns - Selecting rows - loc - iloc - Conditional selection - &, | - isin() 
# • Do not use groupby(), sort_values(), apply(), merge(), or aggregation functions. 
# --------------------------------------------------
#     SECTION A – BASIC SELECTION
# -------------------------------------------------- 

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)


# 1. Select only the Name column.
import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a["Name"])


# 2. Select the Name, Age, City, and Marks columns. 

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a[["Name","Age","City","Marks"]]
print(b)

# 3. Select the first 7 rows using iloc.

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.iloc[0:8,]
print(b)

# 4. Select rows from index 5 to 12 using iloc. 

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.iloc[5:12,]
print(b)


# 5. Select rows at index 2, 6, 10, and 15.

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[[2,6,10,15],]
print(b)