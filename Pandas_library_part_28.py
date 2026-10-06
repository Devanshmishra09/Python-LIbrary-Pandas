# : PANDAS – SELECTION & FILTERING PRACTICE

# Dataset: Record.xlsx: 

# • Use Pandas to solve all questions. • Use only the concepts taught so far:
# - Selecting columns - Selecting rows - loc - iloc - Conditional selection - &, | - isin() 
# • Do not use groupby(), sort_values(), apply(), merge(), or aggregation functions. 

# -------------------------------------------------- 
# SECTION D – MULTIPLE CONDITIONS
# -------------------------------------------------- 
# 1. Select students whose Marks are greater than 80 AND Attendance is greater than 85. 

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[(a["Marks"]>80)&(a["Attendance"]>85)]
print(b)

# 2. Select students whose Age is greater than 20 AND Department is CSE.
import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[(a["Age"]>20)&(a["Department"]=="CSE")]
print(b)

# 3. Select students who are from Lucknow OR Delhi.

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[a["City"].isin(["Lucknow","Delhi"])]
print(b)
 
# 4. Select students whose Marks are less than 70 OR Attendance is less than 75  

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[(a["Marks"]<70)&(a["Attendance"]<75)]
print(b)