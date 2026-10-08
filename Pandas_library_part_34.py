
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