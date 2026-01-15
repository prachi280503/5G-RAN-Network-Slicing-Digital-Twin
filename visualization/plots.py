import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE_DIR, "data", "simulation_data.csv")

df = pd.read_csv(data_path)

plt.figure(figsize=(8,6))

for slice_type in df["Slice"].unique():
    subset = df[df["Slice"] == slice_type]
    plt.scatter(subset["Traffic"], subset["Latency"], label=slice_type)

plt.xlabel("Traffic Load")
plt.ylabel("Latency (ms)")
plt.title("5G RAN Network Slicing Performance")
plt.legend()
plt.grid(True)
plt.show()
