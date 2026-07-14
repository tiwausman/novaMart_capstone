# ==========================================================
# NovaMart AI Retail Intelligence Platform
# Delivery Prediction Dashboard
# ==========================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ----------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------

st.set_page_config(
    page_title="Delivery Prediction",
    page_icon="🚚",
    layout="wide"
)

st.title("🚚 Delivery Prediction")

st.markdown("""
Predict whether an order is likely to be delivered **Late** or **On Time**
using the trained Random Forest classification model.
""")

# ----------------------------------------------------------
# Load Model
# ----------------------------------------------------------

@st.cache_resource
def load_model():

    model = joblib.load("random_forest_delivery_model.pkl")

    features = joblib.load("delivery_model_features.pkl")

    return model, features


delivery_model, delivery_features = load_model()

# ----------------------------------------------------------
# Sidebar
# ----------------------------------------------------------

st.sidebar.header("Prediction Inputs")

# ==========================================================
# Basic Order Information
# ==========================================================

price = st.sidebar.number_input(
    "Product Price (R$)",
    min_value=0.0,
    value=100.0
)

freight_value = st.sidebar.number_input(
    "Freight Cost (R$)",
    min_value=0.0,
    value=20.0
)

payment_value = st.sidebar.number_input(
    "Payment Value (R$)",
    min_value=0.0,
    value=120.0
)

payment_installments = st.sidebar.slider(
    "Payment Installments",
    1,
    24,
    3
)

processing_days = st.sidebar.slider(
    "Processing Days",
    0,
    20,
    2
)

shipping_days = st.sidebar.slider(
    "Shipping Days",
    1,
    40,
    8
)

# ==========================================================
# Product Information
# ==========================================================

product_weight_g = st.sidebar.number_input(
    "Product Weight (g)",
    min_value=1.0,
    value=800.0
)

product_volume_cm3 = st.sidebar.number_input(
    "Product Volume (cm³)",
    min_value=1.0,
    value=2500.0
)

product_name_lenght = st.sidebar.slider(
    "Product Name Length",
    1,
    80,
    40
)

product_description_lenght = st.sidebar.slider(
    "Product Description Length",
    1,
    3000,
    600
)

product_photos_qty = st.sidebar.slider(
    "Number of Product Photos",
    1,
    20,
    5
)

# ----------------------------------------------------------
# Build Feature Vector
# ----------------------------------------------------------

input_data = {}

# Initialize every feature with zero
for feature in delivery_features:
    input_data[feature] = 0

# Numerical Features
input_data["price"] = price
input_data["freight_value"] = freight_value
input_data["payment_value"] = payment_value
input_data["payment_installments"] = payment_installments
input_data["processing_days"] = processing_days
input_data["shipping_days"] = shipping_days
input_data["product_weight_g"] = product_weight_g
input_data["product_volume_cm3"] = product_volume_cm3
input_data["product_name_lenght"] = product_name_lenght
input_data["product_description_lenght"] = product_description_lenght
input_data["product_photos_qty"] = product_photos_qty

X = pd.DataFrame([input_data])

# Ensure correct feature order
X = X[delivery_features]

# ----------------------------------------------------------
# Prediction
# ----------------------------------------------------------

if st.button("🚚 Predict Delivery"):

    prediction = delivery_model.predict(X)[0]

    probability = delivery_model.predict_proba(X)[0]

    confidence = np.max(probability) * 100

    st.subheader("Prediction Result")

    if prediction == 1:

        st.error("⚠️ Predicted Result: Late Delivery")

    else:

        st.success("✅ Predicted Result: On-Time Delivery")

    st.metric(
        "Prediction Confidence",
        f"{confidence:.2f}%"
    )

    st.divider()

    st.subheader("Prediction Probabilities")

    col1, col2 = st.columns(2)

    col1.metric(
        "On-Time",
        f"{probability[0]*100:.2f}%"
    )

    col2.metric(
        "Late",
        f"{probability[1]*100:.2f}%"
    )

    st.divider()

    st.subheader("Input Summary")

    st.dataframe(
        X.T.rename(columns={0: "Value"}),
        use_container_width=True
    )
    # ==========================================================
# Delivery Risk Assessment
# ==========================================================

st.divider()

st.subheader("📊 Delivery Risk Assessment")

if "prediction" in locals():

    risk_score = probability[1] * 100

    if risk_score < 30:

        st.success("🟢 Low Risk of Late Delivery")

    elif risk_score < 70:

        st.warning("🟡 Moderate Risk of Late Delivery")

    else:

        st.error("🔴 High Risk of Late Delivery")

    st.progress(int(risk_score))

    st.write(f"**Risk Score:** {risk_score:.2f}%")

else:

    st.info("Click **Predict Delivery** to view the delivery risk.")

# ==========================================================
# Feature Importance
# ==========================================================

st.divider()

st.subheader("📈 Model Explainability")

try:

    importance = pd.read_csv(
        "delivery_feature_importance.csv"
    )

    top_features = importance.head(10)

    fig, ax = plt.subplots(figsize=(10,6))

    sns.barplot(
        data=top_features,
        x="Importance",
        y="Feature",
        palette="viridis",
        ax=ax
    )

    ax.set_title("Top 10 Features Influencing Delivery Prediction")

    st.pyplot(fig)

except:

    st.warning(
        "Feature importance file not found."
    )

# ==========================================================
# Business Recommendations
# ==========================================================

st.divider()

st.subheader("💡 AI Business Recommendations")

if "prediction" in locals():

    if prediction == 1:

        st.error("""

### High Delivery Risk

Recommended Actions

- Prioritize this order.

- Use a faster courier service.

- Notify the customer about possible delays.

- Monitor shipment status frequently.

- Escalate if processing exceeds expected time.

""")

    else:

        st.success("""

### Low Delivery Risk

Recommended Actions

- Continue with standard delivery process.

- Maintain current logistics workflow.

- Send automated delivery notifications.

- Monitor customer feedback after delivery.

""")

else:

    st.info(
        "Run a prediction to generate recommendations."
    )

# ==========================================================
# Prediction Report
# ==========================================================

st.divider()

st.subheader("📄 Prediction Report")

if "prediction" in locals():

    report = pd.DataFrame({

        "Feature": X.columns,

        "Value": X.iloc[0].values

    })

    report.loc[len(report)] = [

        "Prediction",

        "Late Delivery" if prediction == 1 else "On-Time Delivery"

    ]

    report.loc[len(report)] = [

        "Confidence",

        f"{confidence:.2f}%"

    ]

    st.download_button(

        label="⬇ Download Prediction Report",

        data=report.to_csv(index=False),

        file_name="delivery_prediction_report.csv",

        mime="text/csv"

    )

# ==========================================================
# Prediction History
# ==========================================================

st.divider()

st.subheader("📋 Prediction History")

if "history" not in st.session_state:

    st.session_state.history = []

if "prediction" in locals():

    st.session_state.history.append({

        "Price": price,

        "Freight": freight_value,

        "Prediction":

            "Late"

            if prediction == 1

            else "On-Time",

        "Confidence":

            round(confidence,2)

    })

history_df = pd.DataFrame(

    st.session_state.history

)

if len(history_df):

    st.dataframe(

        history_df,

        use_container_width=True

    )

else:

    st.info("No predictions made yet.")

# ==========================================================
# Dashboard Footer
# ==========================================================

st.divider()

st.success(
    "✅ Delivery Prediction Module Loaded Successfully"
)

st.caption(
"""
NovaMart AI Retail Intelligence Platform

Delivery Prediction Module

Powered by Random Forest Machine Learning
"""
)
