import pandas as pd

# 1. Dataset Generation & Export to Excel
data = {
    "order_id": [101, 102, 103, 104, 105, 106, 107],
    "date": ["2026-03-01", "2026-03-01", "2026-03-02", "2026-03-02", "2026-03-03", "2026-03-03", "2026-03-04"],
    "category": ["Electronics", "Clothing", "Electronics", "Home", "Clothing", "Home", "Electronics"],
    "units_sold": [2, 5, 1, 3, 4, 2, 6],
    "unit_price": [2500, 400, 12000, 800, 450, 1500, 3000],
    "discount_pct": [0.05, 0.15, 0.10, 0.0, 0.20, 0.05, 0.10],
    "region": ["North", "South", "North", "West", "East", "West", "North"]
}
df = pd.DataFrame(data)
df.to_excel("01_sales_data.xlsx", index=False)

# Q1: Net Revenue with discount calculation
df["net_revenue"] = (df["units_sold"] * df["unit_price"]) * (1 - df["discount_pct"])

# Q2: Region-wise total revenue
region_revenue = df.groupby("region")["net_revenue"].sum()
print("Q2 - Region Revenue:\n", region_revenue)

# Q3: Category-wise average units sold & max unit price
cat_summary = df.groupby("category").agg({"units_sold": "mean", "unit_price": "max"})
print("\nQ3 - Category Summary:\n", cat_summary)

# Q4: Filter high discount & high revenue orders
high_val_disc = df[(df["discount_pct"] > 0.10) & (df["net_revenue"] > 1000)]
print("\nQ4 - Filtered Orders:\n", high_val_disc[["order_id", "net_revenue"]])

# Q5: Cumulative sum of net revenue over dates
df_sorted = df.sort_values("date")
df_sorted["cumulative_revenue"] = df_sorted["net_revenue"].cumsum()
print("\nQ5 - Cumulative Revenue:\n", df_sorted[["date", "net_revenue", "cumulative_revenue"]])