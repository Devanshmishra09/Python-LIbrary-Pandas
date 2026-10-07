

# 🧹 Phase 2: Data Cleaning & Missing Values (6–10)

# 6. Identify Nulls: Find the total count of missing values (NaN) in each column.

import pandas as pd
a=pd.read_excel("Sales_Record.xlsx")
print(a)
print(a.isna().sum())

# 7. Filter Missing: Filter and display all rows where the Region column contains missing values.

import pandas as pd
a=pd.read_excel("Sales_Record.xlsx")
print(a)
b=a[a["Region"].isna()]
print(b)


# 8. Impute Strings: Fill all missing values in the Region column with the string 'Unknown'.

import pandas as pd
a=pd.read_excel("Sales_Record.xlsx")
print(a)
b=a["Region"].fillna("Unknown")
print(b)

# 9. Impute Numbers: Fill missing values in the Units column with the median value of that column.

import pandas as pd
a=pd.read_excel("Sales_Record.xlsx")
print(a)
b=a['Units'] = a['Units'].fillna(a['Units'].median())
print(b)
print(a)
# 10. Fix Math: After fixing missing Units, recalculate any missing or incorrect Total_Sales values 
# # where Total_Sales = Units * Unit_Price.

import pandas as pd
a=pd.read_excel("Sales_Record.xlsx")
print(a)
b=a["Units"] = a['Units'].fillna(a['Units'].median())
print(b)
print(a)
c=a["Total_Sales"]=a["Units"]*a["Unit_Price"]
print(c)