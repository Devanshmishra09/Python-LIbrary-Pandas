
# 🚀 Phase 6: Advanced Transformations (26–28)

# 26. Custom Mapping/Functions: Create a column called Price_Category where an order is labeled ' High' if Unit_Price >= 500 and 'Low' otherwise.
import pandas as pd 
import numpy as np
a=pd.read_excel("Sales_Record.xlsx")
print(a)
a["Price_Category"] = np.where(a["Unit_Price"] >= 500, "High", "Low")
print(a)

# 27. Cumulative Sum: Create a column called Cumulative_Sales that calculates the running total
# of sales over time (make sure the data is sorted by date first!).

import pandas as pd 
a=pd.read_excel("Sales_Record.xlsx")
print(a)
a["Order_Date"] = pd.to_datetime(a["Date"])

a = a.sort_values(by="Date").assign(
    Cumulative_Sales=lambda x: x["Total_Sales"].cumsum()
)
print(a)

# 28. String Manipulation: Convert all text values in the Item column to uppercase.

import pandas as pd 
a=pd.read_excel("Sales_Record.xlsx")
print(a)
a["Item"] = a["Item"].str.upper()
print(a)