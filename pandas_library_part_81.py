import numpy as np
import pandas as pd

# ---- PROBLEM 1: UNNESTING LISTS IN COLUMNS (explode) ----
# Task: Unnest lists of tags into independent, individual data rows.
df_blog = pd.DataFrame({
    "Post_ID": [1, 2],
    "Tags": [["Tech", "Coding"], ["Lifestyle", "Travel"]]
})

# Solution: Use explode to flatten out lists into individual elements
df_flat = df_blog.explode("Tags")
print("--- Problem 1: Exploded (Flattened) Data ---")
print(df_flat, "\n")


# ---- PROBLEM 2: GROUP-WISE RANKING & ROW NUMBERS (rank) ----
# Task: Calculate separate numerical performance ranks inside each department.
df_sales = pd.DataFrame({
    "Dept": ["Retail", "Retail", "Online", "Online"],
    "Emp": ["Aman", "Pooja", "Raj", "Kiran"],
    "Revenue": [45000, 62000, 51000, 39000]
})

# Solution: Group by department and rank items based on revenue descending
df_sales["Rank"] = df_sales.groupby("Dept")["Revenue"].rank(ascending=False, method="dense")
print("--- Problem 2: Intragroup Sales Ranks ---")
print(df_sales.sort_values(by=["Dept", "Rank"]), "\n")


# ---- PROBLEM 3: EXPRESSION-BASED FILTERING (query) ----
# Task: Filter records using a clean, human-readable string expression.
df_inventory = pd.DataFrame({
    "Item": ["Laptop", "Mouse", "Monitor", "Keyboard"],
    "Stock": [12, 150, 8, 45],
    "Price": [800, 25, 300, 75]
})

# Solution: Write explicit query syntax conditions as single text strings
low_stock_expensive = df_inventory.query("Stock < 20 and Price >= 300")
print("--- Problem 3: Query Method Results ---")
print(low_stock_expensive, "\n")


# ---- PROBLEM 4: FREQUENCY CONTINGENCY TABLES (crosstab) ----
# Task: Find the exact overlap and volume between two categorical variables.
df_survey = pd.DataFrame({
    "Gender": ["F", "M", "F", "M", "F", "F"],
    "Preference": ["Android", "iOS", "iOS", "Android", "iOS", "Android"]
})

# Solution: Generate cross-tabulations easily using pd.crosstab
contingency_matrix = pd.crosstab(df_survey["Gender"], df_survey["Preference"])
print("--- Problem 4: Demographic Preference Matrix ---")
print(contingency_matrix)
