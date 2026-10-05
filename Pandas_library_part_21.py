# PANDAS – SELECTION & FILTERING PRACTICE

# Dataset:
# pandas_complete_practice_dataset.xlsx

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
# SECTION C – CONDITIONAL SELECTION
# --------------------------------------------------

# 1. Select students whose Marks are greater than 80.

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[a["Marks"]>80]
print(b)


# 2. Select students whose Attendance is less than 80.

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[a["Attendance"]<80]
print(b)


# 3. Select students whose Department is CSE.

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[a["Department"]=="CSE"]
print(b)



# 4. Select students whose Exam_Status is Fail.

import pandas as pd 
a=pd.read_excel("Record.xlsx")
print(a)
b=a.loc[a["Exam_Status"]=="Fail"]
print(b)
