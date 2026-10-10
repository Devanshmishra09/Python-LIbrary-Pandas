import pandas as pd

data = {
    "cust_id": ["C1", "C2", "C3", "C4", "C5", "C6"],
    "contract_type": ["Month-to-Month", "1-Year", "2-Year", "Month-to-Month", "2-Year", "1-Year"],
    "tenure_months": [4, 24, 48, 2, 36, 18],
    "monthly_bill": [850, 450, 600, 920, 550, 480],
    "total_charges": [3400, 10800, 28800, 1840, 19800, 8640],
    "churn": ["Yes", "No", "No", "Yes", "No", "No"]
}
df = pd.DataFrame(data)
df.to_excel("06_customer_churn.xlsx", index=False)

# Q1: Overall churn rate percentage
churn_rate = (df["churn"].value_counts(normalize=True)["Yes"]) * 100
print(f"Q1 - Overall Churn Rate: {churn_rate:.2f}%")

# Q2: Contract-wise average metrics
contract_stats = df.groupby("contract_type")[["monthly_bill", "tenure_months"]].mean()
print("\nQ2 - Contract Stats:\n", contract_stats)

# Q3: Short tenure churners filter
short_churn = df[(df["tenure_months"] < 12) & (df["churn"] == "Yes")]
print("\nQ3 - Short Tenure Churners:\n", short_churn[["cust_id", "tenure_months"]])

# Q4: Pivot table for monthly bill sum
pivot_churn = pd.pivot_table(df, values="monthly_bill", index="contract_type", columns="churn", aggfunc="sum", fill_value=0)
print("\nQ4 - Pivot Table Sum:\n", pivot_churn)

# Q5: Median total charges by churn status
median_charges = df.groupby("churn")["total_charges"].median()
print("\nQ5 - Median Total Charges by Churn:\n", median_charges)