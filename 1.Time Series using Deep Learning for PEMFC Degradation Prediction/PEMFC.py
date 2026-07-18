import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# 1. Page Configuration
# ------------------------------
st.set_page_config(
    page_title="PEMFC Degradation & RUL Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------
# 2. Sidebar
# ------------------------------
st.sidebar.title("PEMFC Prognostics Dashboard")
st.sidebar.markdown("Select the model and metrics to view")

model = st.sidebar.selectbox(
    "Choose Model",
    ["ARIMA", "SARIMAX", "Prophet", "RNN", "LSTM", "GRU"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("📌 **Model Summary**")
st.sidebar.write("Choose a model to see its performance, predictions, and diagnostics.")

# ------------------------------
# 3. Load Data
# ------------------------------
# NOTE: Replace these with your actual files/plots
# Example:
# df_actual = pd.read_csv("data/actual_voltage.csv")
# df_pred = pd.read_csv("data/pred_voltage.csv")

# Dummy example data for layout
time = np.arange(0, 1200, 1)
actual = np.sin(time/100) * 0.1 + 3.3  # dummy
pred = np.sin(time/100) * 0.1 + 3.25   # dummy

# ------------------------------
# 4. Main Dashboard
# ------------------------------
st.title("PEMFC Degradation & RUL Analysis Dashboard")

st.markdown("""
This dashboard visualizes the performance of different prognostic models used to predict PEMFC stack voltage degradation and estimate RUL.
""")

# ------------------------------
# 5. Model Panels
# ------------------------------
if model in ["ARIMA", "SARIMAX", "Prophet"]:
    st.subheader(f"{model} Model Performance")

    # Plot: Actual vs Predicted
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(time, actual, label="Actual Voltage", linewidth=2)
    ax.plot(time, pred, label=f"{model} Forecast", linestyle="--", linewidth=2)
    ax.set_title(f"{model} Forecast vs Actual")
    ax.set_xlabel("Time (hours)")
    ax.set_ylabel("Stack Voltage (V)")
    ax.legend()
    st.pyplot(fig)

    # Metrics
    st.markdown("### 📊 Performance Metrics")
    if model == "ARIMA":
        st.write("MAE: 0.0112  |  RMSE: 0.0134")
        st.write("Note: ARIMA captures long-term trend but struggles with short-term dynamics.")
    elif model == "SARIMAX":
        st.write("MAE: 0.0120  |  RMSE: 0.0138")
        st.write("Note: SARIMAX performs well in trend estimation with confidence interval.")
    else:
        st.write("MAE: 0.0125  |  RMSE: 0.0135")
        st.write("Note: Prophet provides smooth trends but underestimates end-of-life acceleration.")

    st.markdown("---")
    st.subheader("Model Analysis")
    if model == "ARIMA":
        st.write("""
        **ARIMA Analysis**
        - Captures global degradation trend effectively.
        - Residual plots show autocorrelation and heteroskedasticity.
        - Fails to model abrupt degradation and transient events.
        - Over-smoothing limits accuracy in end-of-life.
        """)
    elif model == "SARIMAX":
        st.write("""
        **SARIMAX Analysis**
        - Good trend modeling with seasonal adjustments.
        - Confidence interval shows prediction uncertainty.
        - Still limited in capturing sudden voltage drops.
        """)
    else:
        st.write("""
        **Prophet Analysis**
        - Robust to noise and produces smooth forecasts.
        - Limited sensitivity to abrupt degradation near end-of-life.
        - Overestimates RUL due to conservative trend extrapolation.
        """)

else:
    st.subheader(f"{model} Neural Network Performance")

    # Plot: Actual vs Predicted
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(time, actual, label="Actual Voltage", linewidth=2)
    ax.plot(time, pred, label=f"{model} Prediction", linestyle="--", linewidth=2)
    ax.set_title(f"{model} Prediction vs Actual")
    ax.set_xlabel("Time (hours)")
    ax.set_ylabel("Stack Voltage (V)")
    ax.legend()
    st.pyplot(fig)

    # Metrics
    st.markdown("### 📊 Performance Metrics")
    if model == "RNN":
        st.write("MAE: 0.045  |  RMSE: 0.02")
        st.write("RNN struggles with long-term dependencies and rapid degradation.")
    elif model == "LSTM":
        st.write("MAE: 0.025  |  RMSE: 1.26e-3")
        st.write("LSTM provides stable long-term prediction and robust performance.")
    else:
        st.write("MAE: 0.015  |  RMSE: 1.1e-3")
        st.write("GRU gives best accuracy and efficiency, best for degradation modeling.")

    st.markdown("---")
    st.subheader("Model Analysis")
    if model == "RNN":
        st.write("""
        **RNN Analysis**
        - Basic sequential model.
        - Poor long-term memory.
        - Underperforms in fast degradation stages.
        """)
    elif model == "LSTM":
        st.write("""
        **LSTM Analysis**
        - Gates enable long-term dependency learning.
        - Accurate and stable degradation prediction.
        - Better generalization than RNN.
        """)
    else:
        st.write("""
        **GRU Analysis**
        - Similar to LSTM but computationally efficient.
        - Best performance in this study.
        - Ideal for real-time prognostics.
        """)

# ------------------------------
# 6. RUL Estimation Section
# ------------------------------
st.markdown("---")
st.header("RUL Estimation")

st.write("""
**Failure Threshold:** 3.2028 V (96% of initial voltage)

- LSTM prediction indicates voltage remains above threshold during test window.
- No failure detected within the test period.
- Predicted failure index = 42214 (outside test range)
- Therefore, RUL cannot be computed from the available test data.
""")

# ------------------------------
# 7. Final Model Comparison
# ------------------------------
st.markdown("---")
st.header("Model Comparison Summary")

comparison = {
    "Model": ["ARIMA", "SARIMAX", "Prophet", "RNN", "LSTM", "GRU"],
    "MAE": [0.0112, 0.0120, 0.0125, 0.045, 0.025, 0.015],
    "RMSE": [0.0134, 0.0138, 0.0135, 0.02, 0.00126, 0.0011],
    "Notes": [
        "Strong trend capture, weak transient modeling",
        "Good trend + seasonality, limited abrupt response",
        "Smooth trend, conservative RUL prediction",
        "Poor long-term performance",
        "Stable long-term prediction",
        "Best accuracy & efficiency"
    ]
}

df_compare = pd.DataFrame(comparison)
st.dataframe(df_compare)

st.markdown("""
### 🔍 Summary
- **GRU** provides the best accuracy and efficiency for PEMFC degradation prediction.
- **LSTM** offers stable and robust long-term forecasting.
- **ARIMA/SARIMAX/Prophet** provide reliable baselines but lack nonlinear transient modeling.
- **RUL estimation** requires a longer test horizon or additional data for failure detection.
""")
