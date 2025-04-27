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
conf_matrix_img = Image.open("images/LogisticReg_confusion_matrix.png")
roc_curve_img = Image.open("images/LogisticReg_roc_curve.png")

# Title and intro
st.title("📊 Advanced Marketing A/B Testing + Conversion Prediction")
st.markdown("""
Welcome to the Enhanced Marketing Intelligence App — powered by Random Forests for enterprise-level decision making:
- 📈 A/B test insights
- 🤖 Conversion probability scoring
- 🧠 Behavioral targeting
""")

# A/B Testing Results
st.header("🧪 A/B Test Results")

df['test group'] = df['test group'].map({'psa': 0, 'ad': 1})
df['converted'] = df['converted'].astype(int)
group_rates = df.groupby('test group')['converted'].mean().rename({0: 'PSA', 1: 'Ad'})
rate_diff = (group_rates['Ad'] - group_rates['PSA']) * 100

st.write("**Conversion Rates:**")
st.write(f"- Ad group: {group_rates['Ad']:.2%}")
st.write(f"- PSA group: {group_rates['PSA']:.2%}")
st.write(f"- 📊 Uplift: {rate_diff:.2f}%")

from scipy import stats
ad = df[df['test group'] == 1]['converted']
psa = df[df['test group'] == 0]['converted']
t_stat, p_value = stats.ttest_ind(ad, psa)
st.write(f"**T-test p-value:** {p_value:.4f}")

if p_value < 0.05:
    st.success("✅ Statistically significant uplift. Deploy the ad strategy.")
else:
    st.warning("⚠️ No significant difference detected.")

# Conversion Prediction
st.header("🤖 Conversion Probability Predictor")

test_group = st.selectbox("Test Group", options=["psa", "ad"])
total_ads = st.slider("Total Ads Viewed", min_value=0, max_value=1000, value=10)
most_ads_hour = st.slider("Most Ads Hour (24h)", min_value=0, max_value=23, value=18)
most_ads_day = st.selectbox("Most Ads Day", options=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])

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
    st.metric(label="🔮 Conversion Probability", value=f"{proba:.2%}")
    if proba > 0.75:
        st.success("High conversion likelihood — prioritize user.")
    elif proba > 0.5:
        st.info("Moderate conversion potential — monitor and engage.")
    else:
        st.warning("Low likelihood — low ROI segment.")

# Evaluation Visuals
st.header("📉 Model Evaluation")
st.subheader("Confusion Matrix")
st.image(conf_matrix_img, use_column_width=True)

st.subheader("ROC Curve")
st.image(roc_curve_img, use_column_width=True)

# Footer
st.markdown("---")
st.caption("© 2025 Sweety Seelam | Enterprise-ready ML App | Protected under CC BY-NC 4.0")