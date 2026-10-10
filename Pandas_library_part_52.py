import pandas as pd

data = {
    "house_id": ["H1", "H2", "H3", "H4", "H5", "H6"],
    "sqft": [1200, 2400, 950, 3100, 1500, 2200],
    "bedrooms": [2, 4, 2, 5, 3, 3],
    "bathrooms": [2, 3, 1, 4, 2, 2],
    "location": ["Urban", "Suburban", "Urban", "Suburban", "Rural", "Urban"],
    "year_built": [2005, 2018, 1995, 2021, 2010, 2015],
    "price": [4500000, 9200000, 3100000, 12500000, 4100000, 8500000]
}
df = pd.DataFrame(data)
df.to_excel("03_housing.xlsx", index=False)

# Q1: Price per sqft
df["price_per_sqft"] = (df["price"] / df["sqft"]).round(2)
print("Q1 - Price Per Sqft Sample:\n", df[["house_id", "price_per_sqft"]])

# Q2: Location-wise median price and sqft
loc_stats = df.groupby("location").agg({"price": "median", "sqft": "median"})
print("\nQ2 - Location Medians:\n", loc_stats)

# Q3: Filter specific criteria
filtered_houses = df[(df["bedrooms"] >= 3) & (df["price"] < 10000000)]
print("\nQ3 - Filtered Houses:\n", filtered_houses[["house_id", "bedrooms", "price"]])

# Q4: Oldest house
oldest_house = df.loc[df["year_built"].idxmin()]
print("\nQ4 - Oldest House Details:\n", oldest_house[["house_id", "year_built"]])

# Q5: Correlation matrix
corr_matrix = df[["sqft", "bedrooms", "price"]].corr()
print("\nQ5 - Correlation Matrix:\n", corr_matrix)