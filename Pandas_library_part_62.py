"""
Pandas Datetime Mastery: Advanced Time-Series Operations
Author: GitHub Contributor
Description: A comprehensive guide demonstrating advanced pandas techniques 
             for handling, filtering, resampling, and analyzing time-series data.
Topic: pandas, data-analysis, time-series, python
"""

import numpy as np
import pandas as pd

# ==========================================
# 1. GENERATING SYNTHETIC TIME-SERIES DATA
# ==========================================
print("--- Step 1: Generating Datetime DataFrame ---")

# Setting a random seed for reproducibility
np.random.seed(42)

# Generate a 1-minute frequency date range for 3 consecutive days
date_range = pd.date_range(
    start="2026-10-01 00:00:00", end="2026-10-04 00:00:00", freq="min"
)

# Create a DataFrame simulating IoT sensor metrics (Temperature and Energy Usage)
data = {
    "timestamp_raw": date_range.strftime("%Y/%m/%d %H:%M:%S"),  # Strings
    "sensor_id": np.random.choice(["SENSOR_01", "SENSOR_02"], size=len(date_range)),
    "temperature_c": np.random.normal(loc=22.0, scale=3.0, size=len(date_range)),
    "energy_kwh": np.random.uniform(low=0.5, high=4.5, size=len(date_range)),
}
df = pd.DataFrame(data)
print(f"Dataset initialized with {len(df)} rows.\n")

# ==========================================
# 2. DATETIME PARSING & TYPE CONVERSION
# ==========================================
print("--- Step 2: Parsing Strings to Datetime ---")

# Convert the raw string column into a proper pandas datetime object
df["timestamp"] = pd.to_datetime(df["timestamp_raw"], format="%Y/%m/%d %H:%M:%S")

# Drop the old raw string column
df.drop(columns=["timestamp_raw"], inplace=True)
print(df.dtypes, "\n")

# ==========================================
# 3. FILTERING WITH A REGULAR COLUMN
# ==========================================
print("--- Step 3: Filtering via Column Operations ---")

# Extracting granular time parts using the .dt accessor
df["year"] = df["timestamp"].dt.year
df["month"] = df["timestamp"].dt.month
df["day_name"] = df["timestamp"].dt.day_name()
df["hour"] = df["timestamp"].dt.hour

# Boolean indexing: Filter for rows on Friday during peak hours (09:00 to 17:00)
fridays_peak = df[(df["day_name"] == "Friday") & (df["hour"].between(9, 17))]
print(f"Found {len(fridays_peak)} records during Friday peak hours.\n")

# ==========================================
# 4. FILTERING WITH A DATETIME INDEX
# ==========================================
print("--- Step 4: Index-Based Datetime Slicing ---")

# Set the datetime column as the DataFrame Index
df.set_index("timestamp", inplace=True)
df.sort_index(inplace=True)

# Partial string slicing: Select all data from a specific day
oct_second_data = df.loc["2026-10-02"]
print(f"October 2nd Total Records: {len(oct_second_data)}")

# Slice data across a strict multi-day datetime range
range_slice = df.loc["2026-10-01 08:30:00":"2026-10-02 18:30:00"]
print(f"Custom Range Slice Records: {len(range_slice)}")

# Extract data matching a specific time of day regardless of the date
lunch_rush = df.between_time("12:00", "13:30")
print(f"Lunch Rush Records (12:00 - 13:30): {len(lunch_rush)}\n")

# ==========================================
# 5. RESAMPLING & AGGREGATION
# ==========================================
print("--- Step 5: Downsampling and Upsampling ---")

# Downsampling: Aggregate 1-minute data into 1-hour intervals
hourly_summary = (
    df[["temperature_c", "energy_kwh"]]
    .resample("h")
    .agg({"temperature_c": "mean", "energy_kwh": "sum"})
)
print("Hourly Summary Head:")
print(hourly_summary.head(3), "\n")

# Upsampling: Convert hourly summary back to 30-minute intervals and forward-fill values
ffilled_30min = hourly_summary.resample("30min").ffill()
print("Upsampled & Forward-Filled Head:")
print(ffilled_30min.head(3), "\n")

# ==========================================
# 6. ROLLING WINDOWS & CUSTOM TRANSFORMS
# ==========================================
print("--- Step 6: Rolling Calculations & Window Functions ---")

# Compute a 30-minute rolling average of temperature to smooth out noise
df["temp_rolling_avg_30m"] = (
    df["temperature_c"].rolling(window="30min").mean()
)

# Shifting Data: Compare current hour energy usage against 1 hour ago
df["energy_lag_1h"] = df["energy_kwh"].shift(periods=60)  # 60 mins = 1 hour
df["energy_hourly_delta"] = df["energy_kwh"] - df["energy_lag_1h"]

print("Rolling and Shift Calculations Preview:")
print(
    df[["temperature_c", "temp_rolling_avg_30m", "energy_hourly_delta"]]
    .dropna()
    .head(3),
    "\n",
)

# ==========================================
# 7. TIMEZONE HANDLING
# ==========================================
print("--- Step 7: Timezone Localization and Conversion ---")

# Localize naive datetime index to UTC
df_utc = df.tz_localize("UTC")

# Convert UTC time zone to US Eastern Time
df_est = df_utc.tz_convert("America/New_York")
print(f"Original Index sample (UTC): {df_utc.index[0]}")
print(f"Converted Index sample (EST): {df_est.index[0]}\n")

# ==========================================
# 8. CLEANING UP & EXPORTING
# ==========================================
print("--- Step 8: Execution Finished. Ready for Export ---")
# Resetting index to return it to a clean tabular layout before saving
final_df = df.reset_index()
print(f"Final Dataframe Shape: {final_df.shape}")
print("Script executed successfully. Ready to push to GitHub!")
