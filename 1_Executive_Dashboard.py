#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ==========================================================
# NovaMart AI Retail Intelligence Platform
# Executive Dashboard
# ==========================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------

st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Executive Dashboard")

st.markdown(
"""
Executive dashboard showing the key performance indicators (KPIs)
for the NovaMart AI Retail Intelligence Platform.
"""
)

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

@st.cache_data
def load_data():

    return pd.read_csv("retail_master_dataset.csv")

retail = load_data()

# ----------------------------------------------------------
# Data Preparation
# ----------------------------------------------------------

retail["order_purchase_timestamp"] = pd.to_datetime(
    retail["order_purchase_timestamp"]
)

# Revenue

total_revenue = retail["payment_value"].sum()

# Orders

total_orders = retail["order_id"].nunique()

# Customers

total_customers = retail["customer_unique_id"].nunique()

# Average Review

average_review = retail["review_score"].mean()

# Average Delivery Days

average_delivery = retail["delivery_days"].mean()

# ----------------------------------------------------------
# KPI Cards
# ----------------------------------------------------------

st.subheader("Key Performance Indicators")

col1,col2,col3,col4,col5 = st.columns(5)

col1.metric(
    "Revenue",
    f"R$ {total_revenue:,.2f}"
)

col2.metric(
    "Orders",
    f"{total_orders:,}"
)

col3.metric(
    "Customers",
    f"{total_customers:,}"
)

col4.metric(
    "Avg Review",
    f"{average_review:.2f}"
)

col5.metric(
    "Avg Delivery",
    f"{average_delivery:.1f} Days"
)

st.divider()

# ----------------------------------------------------------
# Revenue by Month
# ----------------------------------------------------------

monthly = (

    retail

    .groupby(
        retail["order_purchase_timestamp"].dt.month_name()
    )["payment_value"]

    .sum()

)

months = [

'January','February','March','April','May','June',

'July','August','September','October','November','December'

]

monthly = monthly.reindex(months)

fig, ax = plt.subplots(figsize=(12,5))

ax.plot(

    monthly.index,

    monthly.values,

    marker="o",

    linewidth=3

)

ax.set_title("Monthly Revenue")

ax.set_xlabel("Month")

ax.set_ylabel("Revenue (R$)")

plt.xticks(rotation=45)

st.pyplot(fig)

# ----------------------------------------------------------
# Orders by State
# ----------------------------------------------------------

state = (

    retail

    .groupby("customer_state")

    ["order_id"]

    .nunique()

    .sort_values(ascending=False)

    .head(10)

)

fig, ax = plt.subplots(figsize=(10,6))

sns.barplot(

    x=state.values,

    y=state.index,

    palette="Blues_r",

    ax=ax

)

ax.set_title("Top 10 Customer States")

st.pyplot(fig)

# ----------------------------------------------------------
# Top Product Categories
# ----------------------------------------------------------

category = (

    retail

    .groupby("product_category_name_english")

    ["payment_value"]

    .sum()

    .sort_values(ascending=False)

    .head(10)

)

fig, ax = plt.subplots(figsize=(10,6))

sns.barplot(

    x=category.values,

    y=category.index,

    palette="Greens_r",

    ax=ax

)

ax.set_title("Top Product Categories")

st.pyplot(fig)

# ----------------------------------------------------------
# Average Review Score
# ----------------------------------------------------------

fig, ax = plt.subplots(figsize=(8,5))

sns.countplot(

    x="review_score",

    data=retail,

    palette="viridis",

    ax=ax

)

ax.set_title("Customer Review Distribution")

st.pyplot(fig)

# ----------------------------------------------------------
# Revenue Summary
# ----------------------------------------------------------

st.subheader("Revenue Summary")

summary = pd.DataFrame({

    "Metric":[

        "Total Revenue",

        "Orders",

        "Customers",

        "Average Review",

        "Average Delivery Days"

    ],

    "Value":[

        round(total_revenue,2),

        total_orders,

        total_customers,

        round(average_review,2),

        round(average_delivery,2)

    ]

})

st.dataframe(
    summary,
    use_container_width=True
)

# ----------------------------------------------------------
# Footer
# ----------------------------------------------------------

st.divider()

st.success("Executive Dashboard Loaded Successfully")

