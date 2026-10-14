import numpy as np
import pandas as pd

# 1. SETUP MOCK DATA
print("--- Step 1: Generating Mock Sales Data ---")
np.random.seed(42)
n_rows = 100

data = {
    "Transaction_ID": range(1001, 1001 + n_rows),
    "Date": pd.date_range(start="2026-01-01", periods=n_rows, freq="D"),
    "Product_Category": np.random.choice(
        ["Electronics", "Clothing", "Home", "Books"], n_rows
    ),
    "Units_Sold": np.random.randint(1, 10, n_rows),
    "Unit_Price": np.random.uniform(10.0, 500.0, n_rows).round(2),
    "Customer_Rating": np.random.choice(
        [1.0, 2.0, 3.0, 4.0, 5.0, np.nan], n_rows, p=[0.1, 0.1, 0.2, 0.3, 0.2, 0.1]
    ),
}

df = pd.DataFrame(data)
# Inject a few duplicate rows and messy elements deliberately for cleaning practice
df = pd.concat([df, df.iloc[[5, 12]]], ignore_index=True)
df.loc[[10, 25], "Unit_Price"] = np.nan
print(f"Initial Shape: {df.shape}\n")

# 2. DATA CLEANING
print("--- Step 2: Cleaning Data ---")
# Drop absolute duplicates
df.drop_duplicates(inplace=True)

# Fill missing Unit Prices with the median price of that specific product category
df["Unit_Price"] = df.groupby("Product_Category")["Unit_Price"].transform(
    lambda x: x.fillna(x.median())
)

# Fill missing Customer Ratings with the overall average rating (rounded to 1 decimal)
avg_rating = round(df["Customer_Rating"].mean(), 1)
df["Customer_Rating"].fillna(avg_rating, inplace=True)
print(f"Cleaned Shape: {df.shape}\n")

# 3. FEATURE ENGINEERING
print("--- Step 3: Engineering Features ---")
# Calculate total revenue per transaction
df["Total_Revenue"] = (df["Units_Sold"] * df["Unit_Price"]).round(2)

# Create a calculated column identifying high-value transactions
df["Is_High_Value"] = df["Total_Revenue"] > 1500

# Extract Month name from the date field for seasonal grouping
df["Month"] = df["Date"].dt.strftime("%B")
print(df[["Date", "Product_Category", "Total_Revenue", "Is_High_Value"]].head(), "\n")

# 4. DATA ANALYSIS & AGGREGATION
print("--- Step 4: Analyzing and Aggregating ---")
# Summary metrics per product category
category_summary = (
    df.groupby("Product_Category")
    .agg(
        Total_Sales=("Total_Revenue", "sum"),
        Average_Units_Per_Order=("Units_Sold", "mean"),
        Average_Rating=("Customer_Rating", "mean"),
        Transaction_Count=("Transaction_ID", "count"),
    )
    .round(2)
)

# Sort performance to easily spot top-grossing categories
category_summary.sort_values(by="Total_Sales", ascending=False, inplace=True)
print(category_summary, "\n")

# 5. FILTERING AND EXPORT
print("--- Step 5: Filtering and Exporting ---")
# Filter data to keep only high-performing transactions
top_performers = df[df["Customer_Rating"] >= 4.0]

# Export summaries and subsets directly to CSV sheets
category_summary.to_csv("category_performance_report.csv")
top_performers.to_csv("top_rated_transactions.csv", index=False)
print("Files saved successfully! Script finished under 100 lines.")
