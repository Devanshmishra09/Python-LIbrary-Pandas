
#  Phase 1: Basic Inspection & Overview (1–5)

# 1. Load & Inspect: Read the dataset and display the first 10 rows.

import pandas as pd
a=pd.read_excel("Sales_Record.xlsx")
print(a)
print(a.head(10))


# 2. Dimensions: Find the total number of rows and columns without using len().

import pandas as pd
a=pd.read_excel("Sales_Record.xlsx")
print(a)
print(a.shape)

# 3. Data Types: Check the data types of all columns. 

import pandas as pd
a=pd.read_excel("Sales_Record.xlsx")
print(a)
print(a.dtypes)



# 4. Summary Stats: Generate the descriptive statistics (mean, min, max, quartiles) for all numeric columns.

import pandas as pd
a=pd.read_excel("Sales_Record.xlsx")
print(a)
print(a.describe())



# 5. Unique Categories: List all unique products sold in the Item column.

import pandas as pd
a=pd.read_excel("Sales_Record.xlsx")
print(a)
b=a[a["Units"]==1]
print(b)