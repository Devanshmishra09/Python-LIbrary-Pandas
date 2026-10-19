import pandas as pd

data = {
    "city": ["Lucknow", "Delhi", "Mumbai", "Lucknow"],
    "aqi_score": [85, 160, 92, 210]
}
df = pd.DataFrame(data)

# Goal: Keep AQI scores if they are healthy/moderate (<= 100).
# Anything above 100 gets replaced by a fallback value like -1 or None.
df["capped_aqi"] = df["aqi_score"].where(df["aqi_score"] <= 100, other=-1)

print(df)
