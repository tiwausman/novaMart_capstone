# ==========================================================
# NovaMart AI Retail Intelligence Platform
# About
# ==========================================================

import streamlit as st

# ----------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

# ----------------------------------------------------------
# Title
# ----------------------------------------------------------

st.title("ℹ️ About NovaMart AI Retail Intelligence Platform")

st.markdown("""
Welcome to the **NovaMart AI Retail Intelligence Platform**.

This platform demonstrates how Artificial Intelligence and Machine Learning
can be applied to retail data to improve business decision-making,
customer experience and operational efficiency.
""")

st.divider()

# ==========================================================
# Project Overview
# ==========================================================

st.header("📖 Project Overview")

st.markdown("""
The NovaMart AI Retail Intelligence Platform is an end-to-end
business intelligence solution developed using Python,
Machine Learning and Streamlit.

The platform combines descriptive analytics,
predictive analytics and recommendation systems
to support data-driven decision making within a retail environment.

The project integrates multiple machine learning models into
a single interactive dashboard capable of forecasting sales,
predicting delivery performance, estimating customer satisfaction,
segmenting customers and recommending products.
""")

st.divider()

# ==========================================================
# Project Objectives
# ==========================================================

st.header("🎯 Project Objectives")

objectives = [
    "Analyse historical retail sales data.",
    "Forecast future sales using ARIMA.",
    "Segment customers using K-Means clustering.",
    "Predict late deliveries using Random Forest.",
    "Predict customer satisfaction using Random Forest.",
    "Recommend products using customer behaviour analytics.",
    "Provide explainable AI insights through feature importance.",
    "Develop an interactive business intelligence dashboard."
]

for obj in objectives:
    st.markdown(f"✅ {obj}")

st.divider()

# ==========================================================
# Dashboard Modules
# ==========================================================

st.header("📊 Dashboard Modules")

modules = {
    "📈 Sales Analytics":
        "Interactive analysis of historical sales trends and revenue.",

    "👥 Customer Segmentation":
        "Customer profiling using K-Means clustering.",

    "🚚 Delivery Prediction":
        "Prediction of late deliveries using Random Forest.",

    "😊 Customer Satisfaction":
        "Prediction of customer satisfaction from order characteristics.",

    "🛍️ Recommendation System":
        "Personalized product recommendations using customer behaviour.",

    "🧠 Model Explainability":
        "Visualization of feature importance to explain AI model decisions."
}

for title, description in modules.items():
    st.subheader(title)
    st.write(description)

st.divider()

# ==========================================================
# Machine Learning Models
# ==========================================================

st.header("🤖 Machine Learning Models")

models = {
    "Customer Segmentation": "K-Means Clustering",
    "Sales Forecasting": "ARIMA",
    "Delivery Prediction": "Random Forest Classifier",
    "Customer Satisfaction": "Random Forest Classifier",
    "Recommendation Engine": "Hybrid Recommendation Approach"
}

for module, algorithm in models.items():
    st.markdown(f"**{module}** — {algorithm}")

st.divider()

# ==========================================================
# Technologies
# ==========================================================

st.header("🛠️ Technologies Used")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
### Programming

- Python
- Pandas
- NumPy
- Joblib
""")

with col2:
    st.markdown("""
### Machine Learning

- Scikit-learn
- ARIMA
- Random Forest
- K-Means
""")

with col3:
    st.markdown("""
### Dashboard

- Streamlit
- Matplotlib
- Seaborn
""")

st.divider()

# ==========================================================
# Dataset
# ==========================================================

st.header("🗂 Dataset")

st.markdown("""
This project is based on the **Brazilian Olist E-Commerce Public Dataset**.

The dataset contains information on:

- Customers
- Orders
- Products
- Sellers
- Payments
- Product Reviews
- Delivery Information
- Product Categories

The integrated dataset was cleaned, transformed and engineered
to support predictive modelling and business intelligence.
""")

st.divider()

# ==========================================================
# Key Features
# ==========================================================

st.header("✨ Key Features")

features = [
    "Executive Dashboard",
    "Interactive KPI Cards",
    "Sales Forecasting",
    "Customer Segmentation",
    "Delivery Prediction",
    "Customer Satisfaction Prediction",
    "Recommendation Engine",
    "Explainable AI",
    "Interactive Visualizations",
    "CSV Report Downloads"
]

for feature in features:
    st.markdown(f"⭐ {feature}")

st.divider()

# ==========================================================
# Developer
# ==========================================================

st.header("👩‍💻 Developer")

st.markdown("""
**Dr. Tiwalade Modupe Usman**

Postgraduate Diploma in Artificial Intelligence & Machine Learning

CIMT College, Toronto, Canada

Research Interests:

- Artificial Intelligence
- Machine Learning
- Computer Vision
- Health Informatics
- Explainable AI
- Business Intelligence
""")

st.divider()

# ==========================================================
# Acknowledgements
# ==========================================================

st.header("🙏 Acknowledgements")

st.markdown("""
Special appreciation to:

- CIMT College
- Course Instructors
- Olist for providing the public retail dataset
- The open-source Python community
- Developers of Streamlit and Scikit-learn
""")

st.divider()

# ==========================================================
# Future Improvements
# ==========================================================

st.header("🚀 Future Enhancements")

future = [
    "Deep Learning forecasting models",
    "Real-time data streaming",
    "Cloud deployment",
    "Inventory optimisation",
    "Demand forecasting",
    "Dynamic pricing analytics",
    "Customer churn prediction",
    "Fraud detection"
]

for item in future:
    st.markdown(f"🔹 {item}")

st.divider()

# ==========================================================
# Footer
# ==========================================================

st.success("✅ NovaMart AI Retail Intelligence Platform")

st.caption("""
Version 1.0

Developed by Tiwalade Modupe Usman

Postgraduate Diploma in Artificial Intelligence & Machine Learning

CIMT College

© 2026
""")