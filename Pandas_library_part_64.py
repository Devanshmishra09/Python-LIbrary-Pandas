

import time
import numpy as np
import pandas as pd

# ==========================================
# 1. CREATING HEAVY MEMORY FOOTPRINT DATA
# ==========================================
print("--- Step 1: Simulating High-Volume Dataset ---")
n_records = 500000

data = {
    "Row_ID": range(1, n_records + 1),
    "Status_Code": np.random.choice(["ACTIVE", "PENDING", "SUSPENDED", "ARCHIVED"], size=n_records),
    "Metric_A": np.random.randint(1, 1000, size=n_records),
    "Metric_B": np.random.uniform(10.0, 500.0, size=n_records),
}
df_perf = pd.DataFrame(data)
print(f"Memory footprint baseline initialized with {len(df_perf)} rows.")
initial_memory = df_perf.memory_usage(deep=True).sum() / (1024**2)
print(f"Initial Memory Footprint: {initial_memory:.2f} MB\n")

# ==========================================
# 2. OPTIMIZING MEMORY VIA TYPE DOWNCASTING
# ==========================================
print("--- Step 2: Running Structural Downcasting & Categorical Optimization ---")

# Optimization A: Convert arbitrary text Object streams into lean pandas Categories
df_perf["Status_Code"] = df_perf["Status_Code"].astype("category")

# Optimization B: Downcast loose standard numeric allocations into tighter bit brackets
df_perf["Row_ID"] = pd.to_numeric(df_perf["Row_ID"], downcast="unsigned")
df_perf["Metric_A"] = pd.to_numeric(df_perf["Metric_A"], downcast="unsigned")
df_perf["Metric_B"] = pd.to_numeric(df_perf["Metric_B"], downcast="float")

optimized_memory = df_perf.memory_usage(deep=True).sum() / (1024**2)
print(f"Optimized Memory Footprint: {optimized_memory:.2f} MB")
print(f"Total Overhead Saved: {((initial_memory - optimized_memory)/initial_memory)*100:.1f}%\n")

# ==========================================
# 3. PERFORMANCE BENCHMARK: INTERATION VS VECTORIZATION
# ==========================================
print("--- Step 3: Benchmarking Execution Patterns ---")


# Goal: Compute a complex conditional penalty factor based on status metrics
# Approach A: Slow row-by-row iteration loop via .iterrows()
def calculate_loop(df):
    results = []
    # Arbitrary conditional logic evaluation rule
    for idx, row in df.head(15000).iterrows():  # Subsetting because pure loops are very slow
        if row["Status_Code"] == "ACTIVE" and row["Metric_A"] > 500:
            results.append(row["Metric_B"] * 1.15)
        else:
            results.append(row["Metric_B"] * 0.90)
    return results


start_time = time.time()
_ = calculate_loop(df_perf)
loop_duration = time.time() - start_time
print(f"Iterrows Loop Execution Time (evaluated on only 15k items): {loop_duration:.4f} seconds")

# Approach B: Instant pandas native vectorization layout across entire 500k row dataframe
start_time = time.time()
condition = (df_perf["Status_Code"] == "ACTIVE") & (df_perf["Metric_A"] > 500)
df_perf["Penalty_Result"] = np.where(condition, df_perf["Metric_B"] * 1.15, df_perf["Metric_B"] * 0.90)
vector_duration = time.time() - start_time

print(f"Vectorized Expression Execution Time (evaluated on ALL 500k items): {vector_duration:.4f} seconds")
print(f"Vectorization calculation scaling advantage achieved!\n")
print("Execution complete. Optimization metrics confirmed.")

