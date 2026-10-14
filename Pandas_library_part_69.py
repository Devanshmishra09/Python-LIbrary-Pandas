import numpy as np
import pandas as pd

# 1. SETUP MOCK DATA
print("--- Step 1: Generating User Activity Logs ---")
np.random.seed(24)
n_users = 200

data = {
    "User_ID": [f"USR_{1000 + i}" for i in range(n_users)],
    "Subscription_Tier": np.random.choice(
        ["Free", "Basic", "Premium"], n_users, p=[0.5, 0.3, 0.2]
    ),
    "Monthly_App_Opens": np.random.randint(0, 50, n_users),
    "Minutes_Streamed": np.random.uniform(0.0, 1200.0, n_users).round(1),
    "Days_Since_Last_Login": np.random.choice(
        [np.random.randint(0, 10), np.random.randint(11, 60), np.nan],
        n_users,
        p=[0.7, 0.2, 0.1],
    ),
}

df = pd.DataFrame(data)
print(f"Generated data for {len(df)} users.\n")

# 2. DATA CLEANING & REPAIR
print("--- Step 2: Imputing Missing Activity Data ---")
# If login days are missing, assume the user hasn't logged in all month (default to 30 days)
df["Days_Since_Last_Login"] = df["Days_Since_Last_Login"].fillna(30).astype(int)

# Standardize tier string names to uppercase for clean categorization
df["Subscription_Tier"] = df["Subscription_Tier"].str.upper()

# 3. METRIC & RISK ENGINEERING
print("--- Step 3: Flagging Churn Risk ---")
# Calculate engagement density (minutes streamed per app open)
# Handle potential division by zero using np.where
df["Minutes_Per_Open"] = np.where(
    df["Monthly_App_Opens"] > 0,
    (df["Minutes_Streamed"] / df["Monthly_App_Opens"]).round(1),
    0.0,
)

# Churn Risk Rule: Inactive for > 20 days OR opened the app fewer than 3 times
df["Is_Churn_Risk"] = (df["Days_Since_Last_Login"] > 20) | (
    df["Monthly_App_Opens"] < 3
)

# 4. COHORT AGGREGATION
print("--- Step 4: Tier Cohort Summary ---")
tier_summary = (
    df.groupby("Subscription_Tier")
    .agg(
        Total_Users=("User_ID", "count"),
        Avg_Minutes=("Minutes_Streamed", "mean"),
        Max_Inactivity=("Days_Since_Last_Login", "max"),
        Churn_Count=("Is_Churn_Risk", "sum"),
    )
    .round(1)
)

# Calculate churn rate percentage per tier
tier_summary["Churn_Rate_Pct"] = (
    (tier_summary["Churn_Count"] / tier_summary["Total_Users"]) * 100
).round(1)
print(tier_summary, "\n")

# 5. FILTERING AT-RISK VIPs
print("--- Step 5: Exporting High-Value Churn Targets ---")
# Isolate PREMIUM users who are at risk so marketing can send promos
premium_at_risk = df[(df["Subscription_Tier"] == "PREMIUM") & df["Is_Churn_Risk"]]

premium_at_risk.to_csv("premium_churn_alerts.csv", index=False)
print(f"Saved {len(premium_at_risk)} high-priority premium accounts to alert log.")
