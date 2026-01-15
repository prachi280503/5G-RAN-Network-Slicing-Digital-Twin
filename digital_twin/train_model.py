import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE_DIR, "data", "simulation_data.csv")

df = pd.read_csv(data_path)

X = df[["Traffic"]]
y = df["Latency"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor()
model.fit(X_train, y_train)

joblib.dump(model, "latency_model.pkl")

print("✅ Digital Twin model trained and saved successfully")
