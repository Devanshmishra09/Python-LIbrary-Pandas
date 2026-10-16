# Program 4: Weather Data Analysis and Outlier Detection
# Description: Cleans temperature/humidity logs and calculates statistical trends.

import numpy as np
import pandas as pd


def generate_weather_log():
    """Creates a sample meteorological dataset."""
    dates = pd.date_range(start="2026-06-01", periods=10, freq="D")
    data = {
        "Date": dates,
        "City": ["Lucknow"] * 10,
        "Max_Temp": [38.5, 40.2, 41.0, 39.8, 43.5, 37.0, 42.1, 40.5, 39.0, 41.5],
        "Min_Temp": [27.0, 28.5, 29.0, 28.0, 31.5, 26.5, 30.0, 28.8, 27.5, 29.2],
        "Humidity": [45, 40, 35, 50, 28, 65, 38, 42, 48, 36],
        "Rainfall_mm": [0.0, 0.0, 0.0, 2.5, 0.0, 12.0, 0.0, 0.0, 1.5, 0.0],
    }
    return pd.DataFrame(data)


def process_weather_data(df):
    """Computes temperature range and identifies extreme heat days."""
    df["Temp_Range"] = df["Max_Temp"] - df["Min_Temp"]
    df["Heatwave_Alert"] = df["Max_Temp"] > 41.0
    df["Mean_Daily_Temp"] = (df["Max_Temp"] + df["Min_Temp"]) / 2.0
    df["Rolling_Avg_Temp"] = (
        df["Mean_Daily_Temp"].rolling(window=3, min_periods=1).mean()
    )
    return df


def display_weather_report(df):
    """Prints meteorological stats and summary statistics."""
    print("=== DAILY WEATHER METRICS ===")
    print(
        df[[
            "Date",
            "Max_Temp",
            "Min_Temp",
            "Temp_Range",
            "Heatwave_Alert",
            "Rolling_Avg_Temp",
        ]].to_string(index=False)
    )
    print("\n" + "=" * 45)
    print("=== SUMMARY STATISTICS ===")
    print(f"Average Maximum Temperature: {df['Max_Temp'].mean():.2f} °C")
    print(f"Average Minimum Temperature: {df['Min_Temp'].mean():.2f} °C")
    print(f"Total Rainfall: {df['Rainfall_mm'].sum():.2f} mm")
    hot_days = df[df["Heatwave_Alert"] == True]["Date"].dt.strftime("%Y-%m-%d")
    print("Heatwave Alert Dates:")
    for d in hot_days:
        print(f" - {d}")


def main():
    weather_df = generate_weather_log()
    processed_df = process_weather_data(weather_df)
    display_weather_report(processed_df)


if __name__ == "__main__":
    main()
