import pandas as pd

data = {
    "symbol": ["TCS", "INFY", "RELIANCE", "HDFCBANK", "TATAMOTORS"],
    "shares": [10, 25, 15, 20, 40],
    "buy_price": [3500, 1400, 2400, 1600, 650],
    "current_price": [3800, 1450, 2350, 1720, 820],
    "sector": ["IT", "IT", "Energy", "Banking", "Auto"]
}
df = pd.DataFrame(data)
df.to_excel("07_portfolio.xlsx", index=False)

# Q1: PnL calculation
df["invested"] = df["shares"] * df["buy_price"]
df["current_val"] = df["shares"] * df["current_price"]
df["pnl"] = df["current_val"] - df["invested"]
print("Q1 - Portfolio PnL Sample:\n", df[["symbol", "pnl"]])

# Q2: Total portfolio return percentage
total_inv = df["invested"].sum()
total_curr = df["current_val"].sum()
total_return_pct = ((total_curr - total_inv) / total_inv) * 100
print(f"\nQ2 - Total Portfolio Return: {total_return_pct:.2f}%")

# Q3: Sector-wise invested capital
sector_inv = df.groupby("sector")["invested"].sum()
print("\nQ3 - Sector Investment:\n", sector_inv)

# Q4: Top profit-making stock
top_stock = df.loc[df["pnl"].idxmax(), "symbol"]
print("\nQ4 - Top Profit Stock:", top_stock)

# Q5: Portfolio weight percentage per stock
df["weight_pct"] = (df["current_val"] / total_curr) * 100
print("\nQ5 - Portfolio Weights:\n", df[["symbol", "weight_pct"]])