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