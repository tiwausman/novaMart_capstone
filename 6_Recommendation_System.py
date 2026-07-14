# ==========================================================
# NovaMart AI Retail Intelligence Platform
# Recommendation System
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
This module recommends products using multiple recommendation strategies.

The recommendation engine combines:

- ⭐ Best Rated Products
- 🔥 Popular Products
- 👥 Cluster-Based Recommendations
- ❤️ Customer Preferences

These recommendations help improve customer experience,
increase sales, and support personalized marketing.
""")

# ----------------------------------------------------------
# Load Recommendation Engine
# ----------------------------------------------------------

@st.cache_resource
def load_recommendation_engine():

    engine = joblib.load(
        "recommendation_engine.pkl"
    )

    return engine


engine = load_recommendation_engine()

popular_products = engine["popular_products"]

best_rated_products = engine["best_rated_products"]

cluster_recommendations = engine["cluster_recommendations"]

customer_preferences = engine["customer_preferences"]

# ----------------------------------------------------------
# Sidebar
# ----------------------------------------------------------

st.sidebar.header("Recommendation Dashboard")

st.sidebar.success(
    "AI Recommendation Engine Loaded"
)

st.sidebar.markdown("""
Choose one of the recommendation strategies
using the tabs on this page.
""")

# ----------------------------------------------------------
# KPI Cards
# ----------------------------------------------------------

st.subheader("Recommendation Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Popular Products",
    len(popular_products)
)

col2.metric(
    "Best Rated",
    len(best_rated_products)
)

col3.metric(
    "Customer Clusters",
    cluster_recommendations["Cluster"].nunique()
)

col4.metric(
    "Customer Preferences",
    customer_preferences["customer_unique_id"].nunique()
)

st.divider()

# ----------------------------------------------------------
# Recommendation Tabs
# ----------------------------------------------------------

tab1, tab2, tab3, tab4, tab5 = st.tabs(

    [

        "⭐ Best Rated",

        "🔥 Popular",

        "👥 Cluster",

        "❤️ Preferences",

        "📈 Insights"

    ]

)
# ==========================================================
# TAB 1
# Best Rated Products
# ==========================================================

with tab1:

    st.subheader("⭐ Highest Rated Products")

    st.markdown("""
Products with the highest customer ratings.

These products consistently receive positive reviews
and are excellent candidates for recommendation.
""")

    top_n = st.slider(

        "Number of Products",

        min_value=5,

        max_value=50,

        value=20,

        key="best"

    )

    st.dataframe(

        best_rated_products.head(top_n),

        use_container_width=True

    )

    st.download_button(

        label="Download Best Rated Products",

        data=best_rated_products.to_csv(index=False),

        file_name="best_rated_products.csv",

        mime="text/csv"

    )
    # ==========================================================
# TAB 2
# Popular Products
# ==========================================================

with tab2:

    st.subheader("🔥 Most Popular Products")

    st.markdown("""
These products are recommended because they have
the highest purchase frequency across all customers.
""")

    top_n = st.slider(

        "Number of Products",

        5,

        50,

        20,

        key="popular"

    )

    st.dataframe(

        popular_products.head(top_n),

        use_container_width=True

    )

    st.download_button(

        label="Download Popular Products",

        data=popular_products.to_csv(index=False),

        file_name="popular_products.csv",

        mime="text/csv"

    )
    # ==========================================================
# TAB 3
# Cluster-Based Recommendations
# ==========================================================

with tab3:

    st.subheader("👥 Cluster-Based Product Recommendations")

    st.markdown("""
Products recommended for customers within the same
customer segment (cluster).

These products are the most frequently purchased by
customers belonging to each cluster.
""")

    cluster_list = sorted(
        cluster_recommendations["Cluster"].unique()
    )

    selected_cluster = st.selectbox(
        "Select Customer Cluster",
        cluster_list
    )

    cluster_result = cluster_recommendations[
        cluster_recommendations["Cluster"] == selected_cluster
    ]

    st.dataframe(
        cluster_result,
        use_container_width=True
    )

    st.download_button(
        "Download Cluster Recommendations",
        cluster_result.to_csv(index=False),
        file_name=f"cluster_{selected_cluster}_recommendations.csv",
        mime="text/csv"
    )

st.divider()

# ==========================================================
# TAB 4
# Customer Preferences
# ==========================================================

with tab4:

    st.subheader("❤️ Customer Preferred Categories")

    st.markdown("""
This recommendation strategy identifies the product
categories that each customer purchases most frequently.

These preferences can be used for personalized marketing
campaigns.
""")

    customer_list = sorted(
        customer_preferences["customer_unique_id"].unique()
    )

    selected_customer = st.selectbox(
        "Select Customer",
        customer_list
    )

    customer_result = customer_preferences[
        customer_preferences["customer_unique_id"]
        == selected_customer
    ]

    st.dataframe(
        customer_result,
        use_container_width=True
    )

    st.download_button(
        "Download Customer Preferences",
        customer_result.to_csv(index=False),
        file_name="customer_preferences.csv",
        mime="text/csv"
    )

st.divider()

# ==========================================================
# Recommendation Statistics
# ==========================================================

st.subheader("📊 Recommendation Statistics")

left, right = st.columns(2)

with left:

    st.markdown("### Products per Cluster")

    cluster_counts = (
        cluster_recommendations
        .groupby("Cluster")["product_id"]
        .count()
    )

    st.bar_chart(cluster_counts)

with right:

    st.markdown("### Customer Preference Distribution")

    category_counts = (
        customer_preferences
        ["product_category_name_english"]
        .value_counts()
        .head(10)
    )

    st.bar_chart(category_counts)

st.divider()

# ==========================================================
# Recommendation Search
# ==========================================================

st.subheader("🔍 Quick Customer Search")

search_customer = st.text_input(
    "Enter Customer ID"
)

if search_customer:

    result = customer_preferences[
        customer_preferences["customer_unique_id"]
        .str.contains(
            search_customer,
            case=False,
            na=False
        )
    ]

    if len(result):

        st.success(
            f"{len(result)} record(s) found."
        )

        st.dataframe(
            result,
            use_container_width=True
        )

    else:

        st.warning(
            "Customer not found."
        )