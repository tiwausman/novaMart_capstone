# ==========================================================
# NovaMart AI Retail Intelligence Platform
# Landing Page
# ==========================================================

import streamlit as st

# ----------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------

st.set_page_config(
    page_title="NovaMart AI Retail Intelligence Platform",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------------
# Custom CSS
# ----------------------------------------------------------

st.markdown("""

<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.block-container{

padding-top:2rem;

padding-bottom:2rem;

padding-left:3rem;

padding-right:3rem;

}

.hero{

background:linear-gradient(135deg,#0F62FE,#4F8EF7);

padding:45px;

border-radius:18px;

color:white;

margin-bottom:30px;

}

.hero h1{

font-size:48px;

font-weight:bold;

margin-bottom:10px;

}

.hero p{

font-size:20px;

}

.card{

background:white;

padding:25px;

border-radius:15px;

box-shadow:0 4px 12px rgba(0,0,0,0.12);

text-align:center;

height:210px;

}

.card h3{

color:#0F62FE;

}

.footer{

text-align:center;

color:gray;

font-size:14px;

margin-top:30px;

}

</style>

""", unsafe_allow_html=True)

# ----------------------------------------------------------
# Sidebar
# ----------------------------------------------------------

st.sidebar.title("🛍️ NovaMart AI")

st.sidebar.success("Retail Intelligence Platform")

st.sidebar.markdown("---")

st.sidebar.markdown("### Dashboard Modules")

st.sidebar.markdown("""
📊 Executive Dashboard

📈 Sales Analytics

👥 Customer Segmentation

🚚 Delivery Prediction

😊 Customer Satisfaction

🛍 Recommendation System

🧠 Model Explainability

ℹ About
""")

st.sidebar.markdown("---")

st.sidebar.info(
"Select any module from the Pages menu."
)

# ----------------------------------------------------------
# Hero Banner
# ----------------------------------------------------------

st.markdown("""

<div class="hero">

<h1>🛍️ NovaMart AI Retail Intelligence Platform</h1>

<p>

An AI-powered business intelligence platform for retail analytics,
sales forecasting, customer segmentation,
delivery prediction,
customer satisfaction prediction,
recommendation systems,
and explainable AI.

</p>

</div>

""", unsafe_allow_html=True)

# ----------------------------------------------------------
# Quick Statistics
# ----------------------------------------------------------

st.subheader("🚀 Platform Capabilities")

col1,col2,col3,col4=st.columns(4)

col1.metric(
"Modules",
"8"
)

col2.metric(
"AI Models",
"5"
)

col3.metric(
"Interactive Dashboards",
"8"
)

col4.metric(
"Prediction Systems",
"3"
)

st.divider()

# ----------------------------------------------------------
# Feature Cards
# ----------------------------------------------------------

st.subheader("✨ Core Features")

c1,c2,c3=st.columns(3)

with c1:

    st.markdown("""

<div class="card">

<h3>📈 Sales Analytics</h3>

Historical sales analysis

Revenue trends

Monthly performance

ARIMA Forecasting

</div>

""",unsafe_allow_html=True)

    st.markdown("<br>",unsafe_allow_html=True)

    st.markdown("""

<div class="card">

<h3>🚚 Delivery Prediction</h3>

Random Forest

Late Delivery Risk

Operational Insights

</div>

""",unsafe_allow_html=True)

with c2:

    st.markdown("""

<div class="card">

<h3>👥 Customer Segmentation</h3>

K-Means Clustering

Customer Behaviour

Business Profiling

</div>

""",unsafe_allow_html=True)

    st.markdown("<br>",unsafe_allow_html=True)

    st.markdown("""

<div class="card">

<h3>😊 Customer Satisfaction</h3>

Review Prediction

Customer Experience

AI Insights

</div>

""",unsafe_allow_html=True)

with c3:

    st.markdown("""

<div class="card">

<h3>🛍 Recommendation System</h3>

Personalized Products

Popular Products

Cluster Recommendations

</div>

""",unsafe_allow_html=True)

    st.markdown("<br>",unsafe_allow_html=True)

    st.markdown("""

<div class="card">

<h3>🧠 Explainable AI</h3>

Feature Importance

Model Transparency

Business Interpretation

</div>

""",unsafe_allow_html=True)

st.divider()

# ----------------------------------------------------------
# Machine Learning Pipeline
# ----------------------------------------------------------

st.subheader("🤖 Machine Learning Workflow")

st.markdown("""

```text

Retail Dataset

      │

      ▼

Data Cleaning

      │

      ▼

Feature Engineering

      │

      ▼

────────────────────────────────────

Sales Forecasting (ARIMA)

Customer Segmentation (KMeans)

Delivery Prediction (Random Forest)

Customer Satisfaction (Random Forest)

Recommendation Engine

────────────────────────────────────

      │

      ▼

Executive Dashboard

Notice the last line:

```python
""")