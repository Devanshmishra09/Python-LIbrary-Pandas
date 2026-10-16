# Program 2: Retail Inventory and Sales Value Analysis
# Description: Evaluates stock values, applies tiered discounts, and tracks low stock.

import pandas as pd


def create_inventory_dataset():
    """Generates an initial stock and sales catalog."""
    inventory = {
        "Product_ID": [
            "P001",
            "P002",
            "P003",
            "P004",
            "P005",
            "P006",
            "P007",
            "P008",
        ],
        "Product_Name": [
            "Laptop",
            "Mouse",
            "Keyboard",
            "Monitor",
            "Printer",
            "Headset",
            "Webcam",
            "USB Hub",
        ],
        "Category": [
            "Electronics",
            "Accessories",
            "Accessories",
            "Electronics",
            "Office",
            "Audio",
            "Audio",
            "Accessories",
        ],
        "Unit_Price": [55000, 450, 1200, 12500, 8500, 2200, 1800, 600],
        "Units_In_Stock": [15, 120, 80, 25, 10, 45, 30, 150],
        "Reorder_Level": [10, 30, 20, 15, 8, 15, 10, 40],
    }
    return pd.DataFrame(inventory)


def analyze_inventory(df):
    """Calculates total inventory valuation and flags stock alerts."""
    df["Total_Stock_Value"] = df["Unit_Price"] * df["Units_In_Stock"]
    df["Restock_Required"] = df["Units_In_Stock"] < df["Reorder_Level"]

    def apply_discount(row):
        if row["Category"] == "Electronics" and row["Units_In_Stock"] > 20:
            return row["Unit_Price"] * 0.90
        elif row["Total_Stock_Value5"] if "Total_Stock_Value5" in row else False:
            return row["Unit_Price"] * 0.95
        return row["Unit_Price"]

    df["Discounted_Price"] = df.apply(
        lambda r: (
            r["Unit_Price"] * 0.90
            if r["Category"] == "Electronics"
            else r["Unit_Price"]
        ),
        axis=1,
    )
    return df


def print_report(df):
    """Displays structured warehouse findings."""
    print("=== INVENTORY VALUE OVERVIEW ===")
    print(
        df[[
            "Product_ID",
            "Product_Name",
            "Units_In_Stock",
            "Total_Stock_Value",
        ]].to_string(index=False)
    )
    print("\n" + "-" * 50)
    total_val = df["Total_Stock_Value"].sum()
    print(f"Grand Total Inventory Valuation: ₹ {total_val:,.2f}")

    print("\n=== ITEMS REQUIRING REORDER ===")
    low_stock = df[df["Restock_Required"] == True]
    if not low_stock.empty:
        print(low_stock[["Product_Name", "Units_In_Stock", "Reorder_Level"]])
    else:
        print("All items are above safety stock levels.")


def main():
    df = create_inventory_dataset()
    analyzed_df = analyze_inventory(df)
    print_report(analyzed_df)


if __name__ == "__main__":
    main()
