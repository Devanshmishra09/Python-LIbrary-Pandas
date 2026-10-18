import numpy as np
import pandas as pd

# ----------------- PROBLEM 1: DROPPING DUPLICATES -----------------
# Task: Remove duplicate records keeping the latest one based on a timestamp.
logs_data = {
    "User": ["Alice", "Bob", "Alice", "Bob", "Alice"],
    "Action": ["Login", "Login", "Click", "Logout", "Login"],
    "Timestamp": ["10:00", "10:05", "10:06", "10:10", "10:15"],
}
df_logs = pd.DataFrame(logs_data)

# Solution: Sort by time and drop duplicates keeping the last entry
df_logs = df_logs.sort_values("Timestamp")
df_unique_users = df_logs.drop_duplicates(subset=["User"], keep="last")
print("--- Problem 1: Latest User Actions ---")
print(df_unique_users, "\n")


# ----------------- PROBLEM 2: PIVOTING DATASETS -----------------
# Task: Reshape long format transaction data into a wide summary table.
sales_data = {
    "Store": ["East", "West", "East", "West", "East", "West"],
    "Product": ["Apples", "Apples", "Bananas", "Bananas", "Apples", "Bananas"],
    "Sales": [100, 150, 200, 120, 90, 130],
}
df_sales = pd.DataFrame(sales_data)

# Solution: Pivot table to see total sales by Store (rows) and Product (columns)
df_pivot = df_sales.pivot_table(
    values="Sales", index="Store", columns="Product", aggfunc="sum"
)
print("--- Problem 2: Store vs Product Sales Matrix ---")
print(df_pivot, "\n")


# ----------------- PROBLEM 3: ROLLING WINDOW METRICS -----------------
# Task: Calculate a 3-day moving average for a stock price tracking dataset.
stock_data = {
    "Day": [1, 2, 3, 4, 5, 6, 7],
    "Price": [150, 152, 155, 153, 158, 162, 160],
}
df_stock = pd.DataFrame(stock_data)

# Solution: Use .rolling() window of size 3 and calculate the mean
df_stock["3Day_Moving_Avg"] = df_stock["Price"].rolling(window=3).mean()
print("--- Problem 3: Stock Price Rolling Averages ---")
print(df_stock.round(2))
