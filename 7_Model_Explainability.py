# ==========================================================
# NovaMart AI Retail Intelligence Platform
# Model Explainability Dashboard
# ==========================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------

st.set_page_config(
    page_title="Model Explainability",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Model Explainability")

st.markdown("""
This dashboard explains how the machine learning models make predictions.

Instead of treating the models as black boxes, feature importance analysis
shows which variables contribute most to each prediction.

The dashboard covers:

- Delivery Prediction Model
- Customer Satisfaction Model
- Business Interpretation
""")

# ----------------------------------------------------------
# Load Data
# ----------------------------------------------------------

@st.cache_data
def load_results():

    delivery = pd.read_csv(
        "delivery_feature_importance.csv"
    )

    satisfaction = pd.read_csv(
        "customer_satisfaction_feature_importance.csv"
    )

    summary = pd.read_csv(
        "model_explainability_summary.csv"
    )

    return delivery, satisfaction, summary


delivery_importance, satisfaction_importance, summary = load_results()

# ----------------------------------------------------------
# KPI Cards
# ----------------------------------------------------------

st.subheader("Explainability Overview")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Delivery Features",
    len(delivery_importance)
)

col2.metric(
    "Satisfaction Features",
    len(satisfaction_importance)
)

col3.metric(
    "Models Explained",
    2
)

st.divider()

# ----------------------------------------------------------
# Tabs
# ----------------------------------------------------------

tab1, tab2, tab3 = st.tabs([

    "🚚 Delivery Model",

    "😊 Satisfaction Model",

    "📋 Executive Summary"

])
# ==========================================================
# TAB 1
# Delivery Prediction
# ==========================================================

with tab1:

    st.subheader("🚚 Delivery Prediction Feature Importance")

    st.markdown("""
The Random Forest model identifies the variables that most strongly
influence whether an order will be delivered on time or late.
""")

    top = st.slider(

        "Number of Features",

        5,

        20,

        10,

        key="delivery"

    )

    top_delivery = delivery_importance.head(top)

    fig, ax = plt.subplots(figsize=(10,6))

    sns.barplot(

        data=top_delivery,

        x="Importance",

        y="Feature",

        palette="viridis",

        ax=ax

    )

    ax.set_title("Top Features Influencing Delivery Prediction")

    st.pyplot(fig)

    st.dataframe(

        top_delivery,

        use_container_width=True

    )

    st.download_button(

        "Download Delivery Feature Importance",

        delivery_importance.to_csv(index=False),

        file_name="delivery_feature_importance.csv",

        mime="text/csv"

    )
# ==========================================================
# TAB 2
# Customer Satisfaction
# ==========================================================

with tab2:

    st.subheader("😊 Customer Satisfaction Feature Importance")

    st.markdown("""
The Random Forest model identifies the variables that contribute
most to predicting customer satisfaction.
""")

    top = st.slider(

        "Number of Features",

        5,

        20,

        10,

        key="satisfaction"

    )

    top_satisfaction = satisfaction_importance.head(top)

    fig, ax = plt.subplots(figsize=(10,6))

    sns.barplot(

        data=top_satisfaction,

        x="Importance",

        y="Feature",

        palette="rocket",

        ax=ax

    )

    ax.set_title("Top Features Influencing Customer Satisfaction")

    st.pyplot(fig)

    st.dataframe(

        top_satisfaction,

        use_container_width=True

    )

    st.download_button(

        "Download Satisfaction Feature Importance",

        satisfaction_importance.to_csv(index=False),

        file_name="customer_satisfaction_feature_importance.csv",

        mime="text/csv"

    )
# ==========================================================
# TAB 3
# Executive Summary
# ==========================================================

with tab3:

    st.subheader("📋 Executive Summary")

    st.markdown("""
This section summarizes the most influential features identified by
the machine learning models and explains their business significance.
""")

    st.dataframe(
        summary,
        use_container_width=True
    )

    st.download_button(
        label="⬇ Download Executive Summary",
        data=summary.to_csv(index=False),
        file_name="model_explainability_summary.csv",
        mime="text/csv"
    )

st.divider()

# ==========================================================
# Business Insights
# ==========================================================

st.subheader("💡 Business Insights")

col1, col2 = st.columns(2)

with col1:

    st.success("""

### 🚚 Delivery Prediction

The model indicates that delivery performance is mainly affected by:

• Processing Time

• Shipping Time

• Freight Cost

• Product Weight

• Payment Value

**Recommendations**

✔ Reduce warehouse processing time

✔ Improve courier efficiency

✔ Optimise shipping routes

✔ Monitor heavy products

✔ Reduce logistics bottlenecks

""")

with col2:

    st.info("""

### 😊 Customer Satisfaction

Customer satisfaction is mainly influenced by:

• Delivery Performance

• Product Quality

• Freight Charges

• Payment Behaviour

• Order Value

**Recommendations**

✔ Deliver products on time

✔ Improve customer communication

✔ Improve packaging quality

✔ Reduce unnecessary freight charges

✔ Encourage customer feedback

""")

st.divider()

# ==========================================================
# Model Comparison
# ==========================================================

st.subheader("📊 AI Model Comparison")

comparison = pd.DataFrame({

    "Model":[
        "Delivery Prediction",
        "Customer Satisfaction"
    ],

    "Algorithm":[
        "Random Forest",
        "Random Forest"
    ],

    "Explainability Method":[
        "Feature Importance",
        "Feature Importance"
    ],

    "Business Objective":[
        "Predict Late Deliveries",
        "Predict Customer Satisfaction"
    ]

})

st.dataframe(
    comparison,
    use_container_width=True
)

st.divider()

# ==========================================================
# Explainability Statistics
# ==========================================================

st.subheader("📈 Explainability Statistics")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Models",
    2
)

c2.metric(
    "Delivery Features",
    len(delivery_importance)
)

c3.metric(
    "Satisfaction Features",
    len(satisfaction_importance)
)

c4.metric(
    "Top Feature",
    summary.iloc[0]["Top Feature"]
    if "Top Feature" in summary.columns
    else summary.iloc[0,1]
)

st.divider()

# ==========================================================
# AI Recommendations
# ==========================================================

st.subheader("🎯 AI Recommendations")

recommendations = pd.DataFrame({

    "Recommendation":[

        "Reduce processing time",

        "Improve delivery performance",

        "Monitor freight costs",

        "Improve customer communication",

        "Increase product quality",

        "Monitor model performance"

    ],

    "Expected Benefit":[

        "Fewer delayed deliveries",

        "Higher customer satisfaction",

        "Lower logistics costs",

        "Improved customer trust",

        "Better product reviews",

        "Reliable AI predictions"

    ]

})

st.dataframe(
    recommendations,
    use_container_width=True
)

st.divider()

# ==========================================================
# Download All Explainability Results
# ==========================================================

st.subheader("📥 Download Results")

download_choice = st.selectbox(

    "Select Report",

    [

        "Delivery Feature Importance",

        "Customer Satisfaction Feature Importance",

        "Executive Summary"

    ]

)

if download_choice == "Delivery Feature Importance":

    data = delivery_importance
    filename = "delivery_feature_importance.csv"

elif download_choice == "Customer Satisfaction Feature Importance":

    data = satisfaction_importance
    filename = "customer_satisfaction_feature_importance.csv"

else:

    data = summary
    filename = "model_explainability_summary.csv"

st.download_button(

    label="Download Report",

    data=data.to_csv(index=False),

    file_name=filename,

    mime="text/csv"

)

st.divider()

# ==========================================================
# Conclusion
# ==========================================================

st.subheader("📌 Conclusion")

st.markdown("""
The explainability analysis provides transparency into the machine
learning models used within the NovaMart AI Retail Intelligence Platform.

By identifying the most influential features affecting delivery performance
and customer satisfaction, business managers can make informed decisions
to improve operational efficiency, customer experience and overall
business performance.

These insights increase confidence in AI-driven recommendations and
support more effective strategic planning.
""")

st.divider()

# ==========================================================
# Footer
# ==========================================================

st.success("✅ Model Explainability Dashboard Loaded Successfully")

st.caption("""
NovaMart AI Retail Intelligence Platform

Model Explainability Module

Feature Importance-Based Explainable AI (XAI)

Developed by Tiwalade Modupe Usman
""")