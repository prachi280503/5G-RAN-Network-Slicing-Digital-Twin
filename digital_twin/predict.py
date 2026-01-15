import joblib
import numpy as np

# Load trained digital twin model
model = joblib.load("latency_model.pkl")

# Example traffic loads
test_traffic = np.array([[10], [30], [60], [90]])

predicted_latency = model.predict(test_traffic)

for t, l in zip(test_traffic, predicted_latency):
    print(f"Traffic Load: {t[0]} → Predicted Latency: {l:.2f} ms")
