import pandas as pd

data = {
    "timestamp": ["2026-03-01 10:00:00", "2026-03-01 10:30:00", "2026-03-01 11:00:00", 
                  "2026-03-01 11:30:00", "2026-03-01 12:00:00", "2026-03-01 12:30:00"],
    "sensor_id": ["S1", "S1", "S1", "S1", "S1", "S1"],
    "temperature": [28.5, 31.0, 35.8, 38.2, 29.4, 27.1],
    "humidity": [55, 52, 45, 40, 60, 65],
    "status_alert": ["OK", "OK", "WARNING", "CRITICAL", "OK", "OK"]
}
df = pd.DataFrame(data)
df.to_excel("05_sensor_readings.xlsx", index=False)

# Q1: Set datetime index
df["timestamp"] = pd.to_datetime(df["timestamp"])
df_indexed = df.set_index("timestamp")

# Q2: Sensor-wise mean stats
sensor_means = df.groupby("sensor_id")[["temperature", "humidity"]].mean()
print("Q2 - Sensor Means:\n", sensor_means)

# Q3: Max temperature timestamp
max_temp_time = df.loc[df["temperature"].idxmax(), "timestamp"]
print("\nQ3 - Max Temp Timestamp:", max_temp_time)

# Q4: Filter warning or critical statuses
alerts = df[df["status_alert"].isin(["WARNING", "CRITICAL"])]
print("\nQ4 - Active Alerts:\n", alerts[["timestamp", "temperature", "status_alert"]])

