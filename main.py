import pandas as pd
from ran.slice import NetworkSlice
from ran.traffic import generate_traffic
from ran.gnb import gNB

# Define network slices
slices = [
    NetworkSlice("eMBB", 50, 100),
    NetworkSlice("URLLC", 1, 20),
    NetworkSlice("mMTC", 100, 10)
]

gnb = gNB()
data = []

# Run simulation
for s in slices:
    for _ in range(100):
        traffic = generate_traffic(s.name)
        latency, throughput = gnb.allocate_resources(traffic)
        data.append([s.name, traffic, latency, throughput])

# Save simulation data
df = pd.DataFrame(
    data, columns=["Slice", "Traffic", "Latency", "Throughput"]
)
df.to_csv("data/simulation_data.csv", index=False)

print("✅ Simulation completed. Data saved to data/simulation_data.csv")
