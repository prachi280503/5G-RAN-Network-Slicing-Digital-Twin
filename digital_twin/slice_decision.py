import pandas as pd
import joblib

model = joblib.load("latency_model.pkl")

def recommend_slice(traffic):
    X = pd.DataFrame([[traffic]], columns=["Traffic"])
    latency = model.predict(X)[0]

    if latency < 2:
        return "URLLC"
    elif latency < 30:
        return "eMBB"
    else:
        return "mMTC"

# Test
for t in [5, 25, 70]:
    print(f"Traffic {t} → Recommended Slice: {recommend_slice(t)}")
