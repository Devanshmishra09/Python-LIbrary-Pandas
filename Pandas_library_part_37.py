
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


# 🔍 Phase 3: Filtering & Conditional Selection (11–15)

# 11. High Value: Extract all orders where Total_Sales is strictly greater than $1,000.

import pandas as pd 
a=pd.read_excel("Sales_Record.xlsx")
print(a)
b=a["Total_Sales"]>1000
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


# 📈 Phase 4: Grouping & Aggregations (16–20)

# 16. Regional Revenue: Group by Region and find the total sum of Total_Sales.

import pandas as pd 
a=pd.read_excel("Sales_Record.xlsx")
print(a)
b= a.groupby('Region')['Total_Sales'].sum().reset_index()
print(b)


# 17. Product Quantity: Which Item had the highest number of total units sold across the whole dataset?

import pandas as pd 
a=pd.read_excel("Sales_Record.xlsx")
print(a)
b=a.groupby("Item")["Total_Sales"].sum().reset_index()
print(b)

# 18. Multi-level Grouping: Group by both Region and Item to find the average Unit_Price and total Units sold.

import pandas as pd 
a=pd.read_excel("Sales_Record.xlsx")
print(a)
b= a.groupby(['Region', 'Item']).agg(Average_Unit_Price=('Unit_Price', 'mean'),Total_Units_Sold=('Units', 'sum')).reset_index()
print(b)


# 19. Custom Aggregation: Group by Region and return both the min and max order value for Total_Sales using .agg().

import pandas as pd 
a=pd.read_excel("Sales_Record.xlsx")
print(a)
b=a.groupby('Region')['Total_Sales'].agg(['min', 'max']).reset_index()
print(b)


# 20. Top Performers: Find the top 5 individual orders sorted by Total_Sales in descending order.

import pandas as pd 
a=pd.read_excel("Sales_Record.xlsx")
print(a)
b=a.nlargest(5, 'Total_Sales')
print(b)



# 📅 Phase 5: Date-Time Manipulation (21–25)

# 21. Convert to DateTime: Convert the Date column into a proper pandas datetime format.

import pandas as pd 
a=pd.read_excel("Sales_Record.xlsx")
print(a)
b=a['Date'] = pd.to_datetime(a['Date'])
print(b)
                 
# 22. Extract Month: Create a new column named Month containing just the month name or number extracted from Date.

import pandas as pd 
a=pd.read_excel("Sales_Record.xlsx")
print(a)
b=a['Month'] = a['Date'].dt.month
print(b)


# 23. Weekday Analysis: Create a boolean column Is_Weekend that flags whether an order was placed on a Saturday or Sunday.

import pandas as pd 
a=pd.read_excel("Sales_Record.xlsx")
print(a)
b=a['Is_Weekend'] = a['Date'].dt.day_name().isin(['Saturday', 'Sunday'])
print(b)
print(a)

# 24. Date Filtering: Extract all transactions that occurred between 2026-02-01 and 2026-02-15.

import pandas as pd 
a=pd.read_excel("Sales_Record.xlsx")
print(a)
b=a[(a['Date'] >= '2026-02-01') & (a['Date'] <= '2026-02-15').index]
print(b)

# 25. Chronological Sort: Sort the entire DataFrame chronologically by Date from oldest to newest.

import pandas as pd 
a=pd.read_excel("Sales_Record.xlsx")
print(a)
b=a.sort_values(by='Date', ascending=True, inplace=True, ignore_index=True)
print(b)


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

