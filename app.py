import streamlit as st
import random
import pandas as pd
import joblib

# Load ML Digital Twin
model = joblib.load("digital_twin/latency_model.pkl")

st.set_page_config(page_title="5G RAN Digital Twin Simulator", layout="centered")

st.title("📡 5G RAN Network Slicing Simulator")
st.subheader("ML-based Digital Twin")

st.markdown("""
This simulator demonstrates **5G RAN network slicing** using an  
**ML-based Digital Twin** for latency prediction and slice recommendation.
""")

slice_type = st.selectbox(
    "Select Network Slice",
    ["eMBB", "URLLC", "mMTC"]
)

slice_traffic = {
    "eMBB": (50, 100),
    "URLLC": (5, 20),
    "mMTC": (1, 10)
}

if st.button("Run Simulation"):
    traffic = random.randint(*slice_traffic[slice_type])

    X = pd.DataFrame([[traffic]], columns=["Traffic"])
    latency = model.predict(X)[0]
    throughput = traffic * random.uniform(0.8, 1.2)

    if latency < 2:
        recommendation = "URLLC"
    elif latency < 30:
        recommendation = "eMBB"
    else:
        recommendation = "mMTC"

    st.success("Simulation Completed")

    st.metric("Traffic Load", traffic)
    st.metric("Predicted Latency (ms)", f"{latency:.2f}")
    st.metric("Estimated Throughput (Mbps)", f"{throughput:.2f}")

    st.info(f"🔁 Digital Twin Recommendation: **{recommendation}**")
