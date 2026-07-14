#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ==========================================================
# NovaMart AI Retail Intelligence Platform
# Sales Analytics Dashboard
# ==========================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os

# ----------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------

st.set_page_config(
    page_title="Sales Analytics",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Sales Analytics")

st.markdown("""
This dashboard provides an overview of sales performance,
revenue trends and future revenue forecasting.
""")

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv("retail_master_dataset.csv")

retail = load_data()

retail["order_purchase_timestamp"] = pd.to_datetime(
    retail["order_purchase_timestamp"]
)

# ----------------------------------------------------------
# Sidebar Filters
# ----------------------------------------------------------

st.sidebar.header("Filters")

years = sorted(
    retail["order_purchase_timestamp"].dt.year.unique()
)

selected_year = st.sidebar.selectbox(
    "Select Year",
    years
)

filtered = retail[
    retail["order_purchase_timestamp"].dt.year == selected_year
]

# ----------------------------------------------------------
# Daily Revenue
# ----------------------------------------------------------

daily_sales = (

    filtered

    .groupby(
        filtered["order_purchase_timestamp"].dt.date
    )["payment_value"]

    .sum()

    .reset_index()

)

daily_sales.columns = ["Date","Revenue"]

daily_sales["Date"] = pd.to_datetime(
    daily_sales["Date"]
)

# ----------------------------------------------------------
# Moving Averages
# ----------------------------------------------------------

daily_sales["MA7"] = (
    daily_sales["Revenue"]
    .rolling(7)
    .mean()
)

daily_sales["MA30"] = (
    daily_sales["Revenue"]
    .rolling(30)
    .mean()
)

# ----------------------------------------------------------
# KPI Cards
# ----------------------------------------------------------

total_revenue = daily_sales["Revenue"].sum()

average_daily = daily_sales["Revenue"].mean()

maximum_day = daily_sales["Revenue"].max()

minimum_day = daily_sales["Revenue"].min()

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "Revenue",
    f"R$ {total_revenue:,.2f}"
)

c2.metric(
    "Average Daily",
    f"R$ {average_daily:,.2f}"
)

c3.metric(
    "Highest Day",
    f"R$ {maximum_day:,.2f}"
)

c4.metric(
    "Lowest Day",
    f"R$ {minimum_day:,.2f}"
)

st.divider()

# ----------------------------------------------------------
# Daily Revenue Trend
# ----------------------------------------------------------

st.subheader("Daily Revenue")

fig, ax = plt.subplots(figsize=(14,5))

ax.plot(
    daily_sales["Date"],
    daily_sales["Revenue"],
    label="Revenue"
)

ax.plot(
    daily_sales["Date"],
    daily_sales["MA7"],
    linewidth=3,
    label="7-Day MA"
)

ax.plot(
    daily_sales["Date"],
    daily_sales["MA30"],
    linewidth=3,
    label="30-Day MA"
)

ax.legend()

ax.set_ylabel("Revenue")

ax.set_xlabel("Date")

st.pyplot(fig)

# ----------------------------------------------------------
# Monthly Revenue
# ----------------------------------------------------------

monthly = (

    filtered

    .groupby(
        filtered["order_purchase_timestamp"].dt.month_name()
    )["payment_value"]

    .sum()

)

months = [

'January','February','March','April','May','June',

'July','August','September','October','November','December'

]

monthly = monthly.reindex(months)

st.subheader("Revenue by Month")

fig, ax = plt.subplots(figsize=(10,5))

sns.barplot(

    x=monthly.index,

    y=monthly.values,

    palette="viridis",

    ax=ax

)

plt.xticks(rotation=45)

ax.set_ylabel("Revenue")

st.pyplot(fig)

# ----------------------------------------------------------
# Weekday Revenue
# ----------------------------------------------------------

weekday = (

    filtered

    .groupby(
        filtered["order_purchase_timestamp"].dt.day_name()
    )["payment_value"]

    .sum()

)

days = [

'Monday',

'Tuesday',

'Wednesday',

'Thursday',

'Friday',

'Saturday',

'Sunday'

]

weekday = weekday.reindex(days)

st.subheader("Revenue by Weekday")

fig, ax = plt.subplots(figsize=(10,5))

sns.barplot(

    x=weekday.index,

    y=weekday.values,

    palette="rocket",

    ax=ax

)

plt.xticks(rotation=45)

st.pyplot(fig)

# ----------------------------------------------------------
# Weekend vs Weekday
# ----------------------------------------------------------

filtered["Weekend"] = (

    filtered["order_purchase_timestamp"]

    .dt.dayofweek >=5

)

weekend = (

    filtered

    .groupby("Weekend")

    ["payment_value"]

    .sum()

)

weekend.index = [

"Weekday",

"Weekend"

]

st.subheader("Weekend vs Weekday Revenue")

fig, ax = plt.subplots(figsize=(6,6))

ax.pie(

    weekend.values,

    labels=weekend.index,

    autopct="%1.1f%%",

    startangle=90

)

st.pyplot(fig)

# ----------------------------------------------------------
# Revenue Distribution
# ----------------------------------------------------------

st.subheader("Revenue Distribution")

fig, ax = plt.subplots(figsize=(10,5))

sns.histplot(

    daily_sales["Revenue"],

    bins=30,

    kde=True,

    color="green",

    ax=ax

)

st.pyplot(fig)

# ----------------------------------------------------------
# ARIMA Forecast
# ----------------------------------------------------------

st.subheader("30-Day Revenue Forecast")

forecast_file = "../data/arima_forecast.csv"

if os.path.exists(forecast_file):

    forecast = pd.read_csv(forecast_file)

    st.line_chart(forecast)

else:

    st.warning("Forecast file not found.")

# ----------------------------------------------------------
# Download
# ----------------------------------------------------------

st.download_button(

    "Download Daily Revenue",

    daily_sales.to_csv(index=False),

    file_name="daily_revenue.csv",

    mime="text/csv"

)

# ----------------------------------------------------------
# Footer
# ----------------------------------------------------------

st.divider()

st.success("Sales Analytics Loaded Successfully")

