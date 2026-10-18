import numpy as np
import pandas as pd

# ---- PROBLEM 1: CUSTOM ROW-WISE OPERATIONS (apply) ----
# Task: Calculate dimensions conditionally across columns.
df_box = pd.DataFrame({"Length": [10, 20, 30], "Width": [5, 10, 15]})

# Solution: Use axis=1 to process data row-by-row
df_box["Area"] = df_box.apply(lambda row: row["Length"] * row["Width"], axis=1)
print("--- Problem 1: Calculated Areas ---")
print(df_box, "\n")


# ---- PROBLEM 2: UNPIVOTING DATA (melt) ----
# Task: Convert wide quarterly data into a clean, long layout.
df_wide = pd.DataFrame({"ID": [101, 102], "Q1_Sales": [150, 210], "Q2_Sales": [180, 240]})

# Solution: Unpivot using melt to separate keys from values
df_long = pd.melt(
    df_wide, id_vars=["ID"], value_vars=["Q1_Sales", "Q2_Sales"], 
    var_name="Quarter", value_name="Revenue"
)
print("--- Problem 2: Melted (Long) Format ---")
print(df_long, "\n")


# ---- PROBLEM 3: SEGMENTING NUMERIC DATA (cut) ----
# Task: Bin continuous numerical data into categorized text buckets.
df_users = pd.DataFrame({"Age": [14, 28, 42, 67]})

# Solution: Segment values into fixed interval bins using pd.cut
bins = [0, 18, 35, 60, 100]
labels = ["Minor", "Young Adult", "Middle Aged", "Senior"]
df_users["Age_Group"] = pd.cut(df_users["Age"], bins=bins, labels=labels)
print("--- Problem 3: Age Demographics ---")
print(df_users, "\n")


# ---- PROBLEM 4: REGEX TEXT EXTRACTION (str.extract) ----
# Task: Isolate and extract specific substrings out of messy text columns.
df_emails = pd.DataFrame({"Email": ["alex@google.com", "sam@nasa.gov", "lina@mit.edu"]})

# Solution: Use a regex capture group to isolate the website domain
df_emails["Domain"] = df_emails["Email"].str.extract(r"@([\w.]+)")
print("--- Problem 4: Extracted Email Domains ---")
print(df_emails)
