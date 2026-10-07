
# 🔍 Phase 3: Filtering & Conditional Selection (11–15)

# 11. High Value: Extract all orders where Total_Sales is strictly greater than $1,000.

import pandas as pd 
a=pd.read_excel("Sales_Record.xlsx")
print(a)
b=a["total_Sales"]>1000
print(b)


# 12. Multi-Criteria: Find all orders from the 'West' region where the Item sold was a 'Laptop'.

import pandas as pd 
a=pd.read_excel("Sales_Record.xlsx")
print(a)
b=a.loc[(a["Region"]=="West") & (a["Item"]=="Laptop")]
print(b)


# 13. List Matching: Filter the dataset to show only rows where the item is a 'Keyboard', 'Mouse', or 'Monitor'.

import pandas as pd 
a=pd.read_excel("Sales_Record.xlsx")
print(a)
b=a.loc[a["Item"].isin(["Keyboard","Mouse","Monitor"])]
print(b)

# 14. Negation: Select all orders except those from the 'Central' region.


import pandas as pd 
a=pd.read_excel("Sales_Record.xlsx")
print(a)
b=a.loc[a["Region"]!="Central"]
print(b)

# 15. Vaue Counts: Find out how many total orders were placed in each unique Region.

import pandas as pd 
a=pd.read_excel("Sales_Record.xlsx")
print(a)
b=a['Region'].value_counts()
print(b)