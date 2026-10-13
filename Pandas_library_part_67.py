# DataFrame with price and quantity
import pandas as pd
df_orders = pd.DataFrame({
    'Price': [10, 20, 15],
    'Quantity': [3, 1, 4]
})

# Add a 'Total_Cost' column
df_orders['Total_Cost'] = df_orders['Price'] * df_orders['Quantity']
print(df_orders)

# Sample sales data
sales_data = {
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Clothing'],
    'Revenue': [500, 200, 300, 150]
}
df_sales = pd.DataFrame(sales_data)

# Group by Category and get the total revenue per category
category_revenue = df_sales.groupby('Category')['Revenue'].sum().reset_index()
print(category_revenue)


from turtle import pd

import numpy as np

# Creating a DataFrame with missing values
import pandas as pd
df_missing = pd.DataFrame({
    'Product': ['A', 'B', 'C'],
    'Price': [100, np.nan, 150]
})

# Option A: Fill missing values with 0
df_filled = df_missing.fillna({'Price': 0})

# Option B: Drop rows with missing values
df_dropped = df_missing.dropna()
    
import pandas as pd

# Sample dictionary data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'London', 'Paris', 'Tokyo']
}

# Create DataFrame
df = pd.DataFrame(data)
print(df)
