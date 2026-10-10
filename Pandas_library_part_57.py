import pandas as pd

data = {
    "order_id": [1, 2, 3, 4, 5, 6, 7],
    "item": ["Cappuccino", "Espresso", "Croissant", "Cold Coffee", "Muffin", "Latte", "Croissant"],
    "item_type": ["Beverage", "Beverage", "Food", "Beverage", "Food", "Beverage", "Food"],
    "price": [180, 120, 150, 220, 110, 200, 150],
    "payment_mode": ["UPI", "Cash", "Card", "UPI", "UPI", "Card", "UPI"],
    "hour_of_day": [9, 10, 10, 14, 15, 16, 17]
}
df = pd.DataFrame(data)
df.to_excel("08_cafe_orders.xlsx", index=False)

# Q1: Payment mode stats
pay_stats = df.groupby("payment_mode").agg(txn_count=("order_id", "count"), total_revenue=("price", "sum"))
print("Q1 - Payment Mode Stats:\n", pay_stats)

# Q2: Most frequent item
popular_item = df["item"].mode()[0]
print("\nQ2 - Most Popular Item:", popular_item)

# Q3: Item type average price
type_avg = df.groupby("item_type")["price"].mean()
print("\nQ3 - Item Type Avg Price:\n", type_avg)

# Q4: Peak hour order counts
peak_hours = df["hour_of_day"].value_counts().head(3)
print("\nQ4 - Peak Hours:\n", peak_hours)

# Q5: Pivot table for item sales summary
item_pivot = pd.pivot_table(df, values="price", index="item", aggfunc=["count", "sum"])
print("\nQ5 - Item Sales Summary:\n", item_pivot)