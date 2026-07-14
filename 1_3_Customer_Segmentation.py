# ==========================================================
# NovaMart AI Retail Intelligence Platform
# Customer Segmentation Dashboard
# ==========================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------

st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="👥",
    layout="wide"
)

st.title("👥 Customer Segmentation")

st.markdown("""
This dashboard provides insights into customer behaviour using
K-Means clustering. Customers are grouped based on purchasing
patterns, spending behaviour and order characteristics.
""")

# ----------------------------------------------------------
# Load Data
# ----------------------------------------------------------

@st.cache_data
def load_data():

    customer_df = pd.read_csv("customer_segments.csv")

    cluster_profile = pd.read_csv(
        "customer_cluster_profiles.csv"
    )

    return customer_df, cluster_profile

customer_df, cluster_profile = load_data()

# ----------------------------------------------------------
# Sidebar
# ----------------------------------------------------------

st.sidebar.header("Customer Filters")

clusters = sorted(customer_df["Cluster"].unique())

selected_cluster = st.sidebar.selectbox(
    "Select Cluster",
    clusters
)

filtered = customer_df[
    customer_df["Cluster"] == selected_cluster
]

# ----------------------------------------------------------
# KPI Cards
# ----------------------------------------------------------

st.subheader("Customer KPIs")

total_customers = customer_df.shape[0]

number_of_clusters = customer_df["Cluster"].nunique()

average_spending = customer_df["Monetary"].mean()

average_orders = customer_df["Frequency"].mean()

average_recency = customer_df["Recency"].mean()

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Customers",
    f"{total_customers:,}"
)

col2.metric(
    "Clusters",
    number_of_clusters
)

col3.metric(
    "Avg Spending",
    f"R$ {average_spending:,.2f}"
)

col4.metric(
    "Avg Orders",
    f"{average_orders:.2f}"
)

col5.metric(
    "Avg Recency",
    f"{average_recency:.1f} Days"
)

st.divider()

# ----------------------------------------------------------
# Customer Search
# ----------------------------------------------------------

st.subheader("Customer Lookup")

customer_id = st.selectbox(

    "Select Customer",

    customer_df["customer_unique_id"]

)

customer = customer_df[
    customer_df["customer_unique_id"] == customer_id
]

st.dataframe(
    customer,
    use_container_width=True
)

st.divider()

# ----------------------------------------------------------
# Cluster Distribution
# ----------------------------------------------------------

st.subheader("Customer Distribution by Cluster")

cluster_counts = (

    customer_df

    .groupby("Cluster")

    .size()

    .reset_index(name="Customers")

)

fig, ax = plt.subplots(figsize=(8,5))

sns.barplot(

    data=cluster_counts,

    x="Cluster",

    y="Customers",

    palette="viridis",

    ax=ax

)

ax.set_title("Customer Distribution")

st.pyplot(fig)

# ----------------------------------------------------------
# Pie Chart
# ----------------------------------------------------------

fig, ax = plt.subplots(figsize=(6,6))

ax.pie(

    cluster_counts["Customers"],

    labels=cluster_counts["Cluster"],

    autopct="%1.1f%%",

    startangle=90

)

ax.set_title("Cluster Composition")

st.pyplot(fig)

st.divider()

# ----------------------------------------------------------
# Cluster Overview
# ----------------------------------------------------------

st.subheader("Selected Cluster Overview")

st.dataframe(

    filtered.head(20),

    use_container_width=True

)
# ==========================================================
# Cluster Profiles
# ==========================================================

st.subheader("📋 Cluster Profiles")

st.markdown("""
The table below summarizes the characteristics of each customer cluster.
These profiles help identify high-value customers, frequent shoppers,
and customers that may require retention strategies.
""")

st.dataframe(
    cluster_profile,
    use_container_width=True
)

st.divider()

# ==========================================================
# Best Customer Cluster
# ==========================================================

st.subheader("🏆 Highest Value Customer Cluster")

best_cluster = customer_df.groupby("Cluster")["Monetary"].mean().idxmax()

best_value = customer_df.groupby("Cluster")["Monetary"].mean().max()

st.success(f"""
Cluster **{best_cluster}** has the highest average spending.

Average Spending: **R$ {best_value:,.2f}**
""")

# ==========================================================
# Most Loyal Customers
# ==========================================================

st.subheader("❤️ Most Loyal Customer Cluster")

loyal_cluster = customer_df.groupby("Cluster")["Frequency"].mean().idxmax()

loyal_orders = customer_df.groupby("Cluster")["Frequency"].mean().max()

st.info(f"""
Cluster **{loyal_cluster}** places the highest number of repeat orders.

Average Orders: **{loyal_orders:.2f}**
""")

# ==========================================================
# Most Recent Customers
# ==========================================================

st.subheader("🕒 Most Active Customers")

recent_cluster = customer_df.groupby("Cluster")["Recency"].mean().idxmin()

recent_days = customer_df.groupby("Cluster")["Recency"].mean().min()

st.success(f"""
Cluster **{recent_cluster}** contains the most recently active customers.

Average Recency: **{recent_days:.1f} days**
""")

# ==========================================================
# Customer Profile Viewer
# ==========================================================

st.subheader("👤 Customer Profile")

customer_selected = st.selectbox(
    "Choose a Customer",
    customer_df["customer_unique_id"]
)

profile = customer_df[
    customer_df["customer_unique_id"] == customer_selected
]

st.dataframe(
    profile,
    use_container_width=True
)

st.divider()

# ==========================================================
# Cluster Business Insights
# ==========================================================

st.subheader("💡 Business Insights")

cluster_summary = customer_df.groupby("Cluster").agg({
    "Monetary":"mean",
    "Frequency":"mean",
    "Recency":"mean"
}).round(2)

highest_spending = cluster_summary["Monetary"].idxmax()
lowest_spending = cluster_summary["Monetary"].idxmin()

highest_frequency = cluster_summary["Frequency"].idxmax()

lowest_recency = cluster_summary["Recency"].idxmin()

st.markdown(f"""
### Key Findings

**Cluster {highest_spending}**
- Highest average spending
- Premium customers
- Ideal for loyalty programmes

---

**Cluster {highest_frequency}**
- Highest purchase frequency
- Strong repeat customers
- Excellent candidates for subscription offers

---

**Cluster {lowest_spending}**
- Lowest spending customers
- Opportunity for promotional campaigns
- Consider targeted discounts

---

**Cluster {lowest_recency}**
- Most recently active customers
- High engagement level
- Suitable for cross-selling
""")

st.divider()

# ==========================================================
# Executive Recommendations
# ==========================================================

st.subheader("🎯 Executive Recommendations")

recommendations = pd.DataFrame({

    "Recommendation":[

        "Reward high-value customers",

        "Target low-spending customers",

        "Cross-sell to loyal customers",

        "Retain inactive customers",

        "Improve customer engagement"

    ],

    "Expected Impact":[

        "Increase customer lifetime value",

        "Increase sales",

        "Increase average order value",

        "Reduce customer churn",

        "Improve retention"

    ]

})

st.dataframe(
    recommendations,
    use_container_width=True
)

# ==========================================================
# Download Customer Segments
# ==========================================================

st.subheader("⬇ Download Results")

st.download_button(

    label="Download Customer Segmentation Results",

    data=customer_df.to_csv(index=False).encode("utf-8"),

    file_name="customer_segments.csv",

    mime="text/csv"

)

st.download_button(

    label="Download Cluster Profiles",

    data=cluster_profile.to_csv(index=False).encode("utf-8"),

    file_name="customer_cluster_profiles.csv",

    mime="text/csv"

)

st.divider()

# ==========================================================
# Dashboard Footer
# ==========================================================

st.success("✅ Customer Segmentation Dashboard Loaded Successfully")

st.caption(
    """
    NovaMart AI Retail Intelligence Platform

    Customer Segmentation Module

    Powered by K-Means Clustering
    """
)
# ==========================================================
# Cluster Profiles
# ==========================================================

st.subheader("📋 Cluster Profiles")

st.markdown("""
The table below summarizes the characteristics of each customer cluster.
These profiles help identify high-value customers, frequent shoppers,
and customers that may require retention strategies.
""")

st.dataframe(
    cluster_profile,
    use_container_width=True
)

st.divider()

# ==========================================================
# Best Customer Cluster
# ==========================================================

st.subheader("🏆 Highest Value Customer Cluster")

best_cluster = customer_df.groupby("Cluster")["Monetary"].mean().idxmax()

best_value = customer_df.groupby("Cluster")["Monetary"].mean().max()

st.success(f"""
Cluster **{best_cluster}** has the highest average spending.

Average Spending: **R$ {best_value:,.2f}**
""")

# ==========================================================
# Most Loyal Customers
# ==========================================================

st.subheader("❤️ Most Loyal Customer Cluster")

loyal_cluster = customer_df.groupby("Cluster")["Frequency"].mean().idxmax()

loyal_orders = customer_df.groupby("Cluster")["Frequency"].mean().max()

st.info(f"""
Cluster **{loyal_cluster}** places the highest number of repeat orders.

Average Orders: **{loyal_orders:.2f}**
""")

# ==========================================================
# Most Recent Customers
# ==========================================================

st.subheader("🕒 Most Active Customers")

recent_cluster = customer_df.groupby("Cluster")["Recency"].mean().idxmin()

recent_days = customer_df.groupby("Cluster")["Recency"].mean().min()

st.success(f"""
Cluster **{recent_cluster}** contains the most recently active customers.

Average Recency: **{recent_days:.1f} days**
""")

# ==========================================================
# Customer Profile Viewer
# ==========================================================

st.subheader("👤 Customer Profile")

customer_selected = st.selectbox(
    "Choose a Customer",
    customer_df["customer_unique_id"]
)

profile = customer_df[
    customer_df["customer_unique_id"] == customer_selected
]

st.dataframe(
    profile,
    use_container_width=True
)

st.divider()

# ==========================================================
# Cluster Business Insights
# ==========================================================

st.subheader("💡 Business Insights")

cluster_summary = customer_df.groupby("Cluster").agg({
    "Monetary":"mean",
    "Frequency":"mean",
    "Recency":"mean"
}).round(2)

highest_spending = cluster_summary["Monetary"].idxmax()
lowest_spending = cluster_summary["Monetary"].idxmin()

highest_frequency = cluster_summary["Frequency"].idxmax()

lowest_recency = cluster_summary["Recency"].idxmin()

st.markdown(f"""
### Key Findings

**Cluster {highest_spending}**
- Highest average spending
- Premium customers
- Ideal for loyalty programmes

---

**Cluster {highest_frequency}**
- Highest purchase frequency
- Strong repeat customers
- Excellent candidates for subscription offers

---

**Cluster {lowest_spending}**
- Lowest spending customers
- Opportunity for promotional campaigns
- Consider targeted discounts

---

**Cluster {lowest_recency}**
- Most recently active customers
- High engagement level
- Suitable for cross-selling
""")

st.divider()

# ==========================================================
# Executive Recommendations
# ==========================================================

st.subheader("🎯 Executive Recommendations")

recommendations = pd.DataFrame({

    "Recommendation":[

        "Reward high-value customers",

        "Target low-spending customers",

        "Cross-sell to loyal customers",

        "Retain inactive customers",

        "Improve customer engagement"

    ],

    "Expected Impact":[

        "Increase customer lifetime value",

        "Increase sales",

        "Increase average order value",

        "Reduce customer churn",

        "Improve retention"

    ]

})

st.dataframe(
    recommendations,
    use_container_width=True
)

# ==========================================================
# Download Customer Segments
# ==========================================================

st.subheader("⬇ Download Results")

st.download_button(

    label="Download Customer Segmentation Results",

    data=customer_df.to_csv(index=False).encode("utf-8"),

    file_name="customer_segments.csv",

    mime="text/csv"

)

st.download_button(

    label="Download Cluster Profiles",

    data=cluster_profile.to_csv(index=False).encode("utf-8"),

    file_name="customer_cluster_profiles.csv",

    mime="text/csv"

)

st.divider()

# ==========================================================
# Dashboard Footer
# ==========================================================

st.success("✅ Customer Segmentation Dashboard Loaded Successfully")

st.caption(
    """
    NovaMart AI Retail Intelligence Platform

    Customer Segmentation Module

    Powered by K-Means Clustering
    """
)