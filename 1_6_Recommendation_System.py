# ==========================================================
# NovaMart AI Retail Intelligence Platform
# Product Recommendation System
# ==========================================================

import streamlit as st
import pandas as pd
import joblib

# ----------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------

st.set_page_config(
    page_title="Recommendation System",
    page_icon="🛍️",
    layout="wide"
)

st.title("🛍️ AI Product Recommendation System")

st.markdown("""
Generate personalized product recommendations using customer behaviour,
purchase history and customer segmentation.
""")

# ----------------------------------------------------------
# Load Recommendation Files
# ----------------------------------------------------------

@st.cache_resource
def load_data():

    popular_products = joblib.load(
        "popular_products.pkl"
    )

    best_rated_products = joblib.load(
        "best_rated_products.pkl"
    )

    cluster_recommendations = joblib.load(
        "cluster_recommendations.pkl"
    )

    customer_preferences = joblib.load(
        "customer_preferences.pkl"
    )

    return (
        popular_products,
        best_rated_products,
        cluster_recommendations,
        customer_preferences
    )

(
popular_products,
best_rated_products,
cluster_recommendations,
customer_preferences

) = load_data()

# ----------------------------------------------------------
# Sidebar
# ----------------------------------------------------------

st.sidebar.header("Recommendation Options")

recommendation_type = st.sidebar.selectbox(

    "Recommendation Strategy",

    [

        "Popular Products",

        "Best Rated Products",

        "Cluster Recommendations",

        "Customer Preferences"

    ]

)

# ----------------------------------------------------------
# Popular Products
# ----------------------------------------------------------

if recommendation_type == "Popular Products":

    st.subheader("🔥 Most Popular Products")

    st.dataframe(

        popular_products,

        use_container_width=True

    )

# ----------------------------------------------------------
# Best Rated
# ----------------------------------------------------------

elif recommendation_type == "Best Rated Products":

    st.subheader("⭐ Highest Rated Products")

    st.dataframe(

        best_rated_products,

        use_container_width=True

    )

# ----------------------------------------------------------
# Cluster Recommendations
# ----------------------------------------------------------

elif recommendation_type == "Cluster Recommendations":

    st.subheader("👥 Recommendations by Customer Cluster")

    clusters = sorted(

        cluster_recommendations["Cluster"].unique()

    )

    selected = st.selectbox(

        "Select Customer Cluster",

        clusters

    )

    recommendations = cluster_recommendations[

        cluster_recommendations["Cluster"] == selected

    ]

    st.dataframe(

        recommendations,

        use_container_width=True

    )

# ----------------------------------------------------------
# Customer Preferences
# ----------------------------------------------------------

else:

    st.subheader("❤️ Customer Preferred Categories")

    customer_ids = sorted(

        customer_preferences["customer_unique_id"].unique()

    )

    customer = st.selectbox(

        "Select Customer",

        customer_ids

    )

    preference = customer_preferences[

        customer_preferences["customer_unique_id"] == customer

    ]

    st.dataframe(

        preference,

        use_container_width=True

    )