# streamlit_app.py
import streamlit as st
import pandas as pd
import pickle
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load model, column list, and images
model = pickle.load(open("model.pkl", "rb"))
expected_cols = pickle.load(open("input_columns.pkl", "rb"))
df = pd.read_csv("data/Marketing_AB_Testing.csv")

# Load images
conf_matrix_img = Image.open("images/LogisticReg_confusion_matrix.png")
roc_curve_img = Image.open("images/LogisticReg_roc_curve.png")
conversion_by_hour_day_img = Image.open("images/Conversion_by_hour&Conversion_by_day.png")
ab_test_plot_img = Image.open("images/AB Testing Groups plot.png")
classification_report_img = Image.open("images/LogisticReg_classification_report.png")

# Title
st.title("📊 Marketing A/B Testing + ML Conversion Prediction App")

st.markdown("""
This dashboard helps analyze:
- 📈 A/B Testing Results between PSA and Paid Ads
- 🤖 Predict Conversion Probability using Logistic Regression
- 💰 Business Impact Estimation
""")

# Section 1: A/B Testing Results
st.header("🧪 A/B Test Results Overview")

st.image(ab_test_plot_img, caption="Conversion Rates by Test Groups", use_column_width=True)

ad_conversion = df[df['test group'] == 1]['converted'].mean()
psa_conversion = df[df['test group'] == 0]['converted'].mean()
uplift = (ad_conversion - psa_conversion) * 100

st.write(f"**Ad Conversion Rate:** {ad_conversion:.2%}")
st.write(f"**PSA Conversion Rate:** {psa_conversion:.2%}")
st.write(f"**Uplift:** {uplift:.2f}% increase by Paid Ads")

from scipy import stats
ad = df[df['test group'] == 1]['converted']
psa = df[df['test group'] == 0]['converted']
t_stat, p_value = stats.ttest_ind(ad, psa)
st.write(f"**T-test p-value:** {p_value:.4f}")

if p_value < 0.05:
    st.success("✅ Statistically significant difference — Paid Ads perform better.")
else:
    st.warning("⚠️ No statistically significant difference detected.")

# Section 2: Peak Hours and Days
st.header("📅 Conversion by Hour and Day")

st.image(conversion_by_hour_day_img, caption="Conversion Rates by Hour and Day", use_column_width=True)

# Section 3: Conversion Prediction (ML Model)
st.header("🔮 Conversion Probability Prediction (Logistic Regression)")

test_group = st.selectbox("Test Group", options=["psa", "ad"])
total_ads = st.slider("Total Ads Viewed", min_value=0, max_value=1000, value=10)
most_ads_hour = st.slider("Most Ads Hour (24h)", min_value=0, max_value=23, value=18)
most_ads_day = st.selectbox("Most Ads Day", options=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

# Prepare input for model
input_data = {col: 0 for col in expected_cols}
input_data['test group'] = 1 if test_group == 'ad' else 0
input_data['total ads'] = total_ads
input_data['most ads hour'] = most_ads_hour
day_feature = f'most ads day_{most_ads_day}'
if day_feature in input_data:
    input_data[day_feature] = 1

X_input = pd.DataFrame([input_data])

if st.button("Predict Conversion Probability"):
    proba = model.predict_proba(X_input)[0][1]
    st.metric(label="🔮 Predicted Conversion Probability", value=f"{proba:.2%}")
    if proba > 0.75:
        st.success("Highly likely to convert! Prioritize.")
    elif proba > 0.5:
        st.info("Moderate chance to convert. Monitor.")
    else:
        st.warning("Low chance of conversion.")

# Section 4: Model Evaluation
st.header("🧪 Model Evaluation (Logistic Regression)")

st.subheader("Confusion Matrix")
st.image(conf_matrix_img, use_column_width=True)

st.subheader("ROC Curve (AUC = 0.85)")
st.image(roc_curve_img, use_column_width=True)

st.subheader("Classification Report Summary")
st.image(classification_report_img, use_column_width=True)

# Footer
st.markdown("---")
st.caption("© 2025 Sweety Seelam | Powered by Logistic Regression | Optimized for Marketing Strategy")