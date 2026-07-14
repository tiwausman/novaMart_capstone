# ==========================================================
# NovaMart AI Retail Intelligence Platform
# Customer Satisfaction Prediction
# ==========================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------

st.set_page_config(
    page_title="Customer Satisfaction",
    page_icon="😊",
    layout="wide"
)

st.title("😊 Customer Satisfaction Prediction")

st.markdown("""
Predict customer satisfaction using the trained Random Forest model.
The prediction estimates whether a customer is likely to leave a
positive review based on order, delivery and payment information.
""")

# ----------------------------------------------------------
# Load Model
# ----------------------------------------------------------

@st.cache_resource
def load_model():

    model = joblib.load(
        "customer_satisfaction_model.pkl"
    )

    features = joblib.load(
        "customer_satisfaction_features.pkl"
    )

    return model, features


model, feature_list = load_model()

# ----------------------------------------------------------
# Sidebar Inputs
# ----------------------------------------------------------

st.sidebar.header("Customer Information")

price = st.sidebar.number_input(
    "Product Price (R$)",
    0.0,
    5000.0,
    100.0
)

freight = st.sidebar.number_input(
    "Freight Cost (R$)",
    0.0,
    500.0,
    20.0
)

payment = st.sidebar.number_input(
    "Payment Value (R$)",
    0.0,
    5000.0,
    120.0
)

installments = st.sidebar.slider(
    "Payment Installments",
    1,
    24,
    3
)

delivery_days = st.sidebar.slider(
    "Delivery Days",
    1,
    40,
    10
)

product_weight = st.sidebar.number_input(
    "Product Weight (g)",
    1.0,
    50000.0,
    800.0
)

product_volume = st.sidebar.number_input(
    "Product Volume (cm³)",
    1.0,
    500000.0,
    2500.0
)

name_length = st.sidebar.slider(
    "Product Name Length",
    1,
    100,
    40
)

description_length = st.sidebar.slider(
    "Description Length",
    1,
    4000,
    600
)

photos = st.sidebar.slider(
    "Number of Photos",
    1,
    20,
    5
)

# ----------------------------------------------------------
# Build Feature Vector
# ----------------------------------------------------------

data = {}

for col in feature_list:
    data[col] = 0

numeric = {

    "price":price,

    "freight_value":freight,

    "payment_value":payment,

    "payment_installments":installments,

    "delivery_days":delivery_days,

    "product_weight_g":product_weight,

    "product_volume_cm3":product_volume,

    "product_name_lenght":name_length,

    "product_description_lenght":description_length,

    "product_photos_qty":photos

}

for key,value in numeric.items():

    if key in data:

        data[key]=value

X = pd.DataFrame([data])

X = X[feature_list]

# ----------------------------------------------------------
# Prediction
# ----------------------------------------------------------

if st.button("Predict Satisfaction"):

    prediction = model.predict(X)[0]

    probability = model.predict_proba(X)[0]

    confidence = np.max(probability)*100

    st.subheader("Prediction")

    if prediction == 1:

        st.success("😊 Customer is likely to be SATISFIED")

    else:

        st.error("☹ Customer is likely to be UNSATISFIED")

    st.metric(

        "Prediction Confidence",

        f"{confidence:.2f}%"

    )

    col1,col2 = st.columns(2)

    col1.metric(

        "Unsatisfied",

        f"{probability[0]*100:.2f}%"

    )

    col2.metric(

        "Satisfied",

        f"{probability[1]*100:.2f}%"

    )

    st.divider()

    st.subheader("Prediction Inputs")

    st.dataframe(

        X.T.rename(columns={0:"Value"}),

        use_container_width=True

    )