# ==========================================================
# Delivery Risk Assessment
# ==========================================================

st.divider()

st.subheader("📊 Delivery Risk Assessment")

if "prediction" in locals():

    risk_score = probability[1] * 100

    if risk_score < 30:

        st.success("🟢 Low Risk of Late Delivery")

    elif risk_score < 70:

        st.warning("🟡 Moderate Risk of Late Delivery")

    else:

        st.error("🔴 High Risk of Late Delivery")

    st.progress(int(risk_score))

    st.write(f"**Risk Score:** {risk_score:.2f}%")

else:

    st.info("Click **Predict Delivery** to view the delivery risk.")

# ==========================================================
# Feature Importance
# ==========================================================

st.divider()

st.subheader("📈 Model Explainability")

try:

    importance = pd.read_csv(
        "delivery_feature_importance.csv"
    )

    top_features = importance.head(10)

    fig, ax = plt.subplots(figsize=(10,6))

    sns.barplot(
        data=top_features,
        x="Importance",
        y="Feature",
        palette="viridis",
        ax=ax
    )

    ax.set_title("Top 10 Features Influencing Delivery Prediction")

    st.pyplot(fig)

except:

    st.warning(
        "Feature importance file not found."
    )

# ==========================================================
# Business Recommendations
# ==========================================================

st.divider()

st.subheader("💡 AI Business Recommendations")

if "prediction" in locals():

    if prediction == 1:

        st.error("""

### High Delivery Risk

Recommended Actions

- Prioritize this order.

- Use a faster courier service.

- Notify the customer about possible delays.

- Monitor shipment status frequently.

- Escalate if processing exceeds expected time.

""")

    else:

        st.success("""

### Low Delivery Risk

Recommended Actions

- Continue with standard delivery process.

- Maintain current logistics workflow.

- Send automated delivery notifications.

- Monitor customer feedback after delivery.

""")

else:

    st.info(
        "Run a prediction to generate recommendations."
    )

# ==========================================================
# Prediction Report
# ==========================================================

st.divider()

st.subheader("📄 Prediction Report")

if "prediction" in locals():

    report = pd.DataFrame({

        "Feature": X.columns,

        "Value": X.iloc[0].values

    })

    report.loc[len(report)] = [

        "Prediction",

        "Late Delivery" if prediction == 1 else "On-Time Delivery"

    ]

    report.loc[len(report)] = [

        "Confidence",

        f"{confidence:.2f}%"

    ]

    st.download_button(

        label="⬇ Download Prediction Report",

        data=report.to_csv(index=False),

        file_name="delivery_prediction_report.csv",

        mime="text/csv"

    )

# ==========================================================
# Prediction History
# ==========================================================

st.divider()

st.subheader("📋 Prediction History")

if "history" not in st.session_state:

    st.session_state.history = []

if "prediction" in locals():

    st.session_state.history.append({

        "Price": price,

        "Freight": freight_value,

        "Prediction":

            "Late"

            if prediction == 1

            else "On-Time",

        "Confidence":

            round(confidence,2)

    })

history_df = pd.DataFrame(

    st.session_state.history

)

if len(history_df):

    st.dataframe(

        history_df,

        use_container_width=True

    )

else:

    st.info("No predictions made yet.")

# ==========================================================
# Dashboard Footer
# ==========================================================

st.divider()

st.success(
    "✅ Delivery Prediction Module Loaded Successfully"
)

st.caption(
"""
NovaMart AI Retail Intelligence Platform

Delivery Prediction Module

Powered by Random Forest Machine Learning
"""
)