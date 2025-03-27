import streamlit as st
import time

# Page Configuration
st.set_page_config(page_title="AI Symptom Checker", page_icon="🩺", layout="centered")

# Custom CSS (Fixed Styling)
st.markdown(
    """
    <style>
        .title { font-size: 40px; font-weight: bold; text-align: center; color: #2E3B55; }
        .subheader { font-size: 20px; text-align: center; color: #555; }
        .feature-box { background-color: #f9f9f9; padding: 15px; border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); margin-bottom: 10px;color: #333; }
        .data-source { font-size: 16px; text-align: center; color: #888; }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Subtitle
st.markdown("<h1 class='title'>Welcome to AI Symptom Checker 🩺</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheader'>A Smart AI-Powered Healthcare Assistant</p>", unsafe_allow_html=True)

# About the Project with Loading Animation
with st.spinner("Loading AI-powered insights..."):
    time.sleep(2)  # Simulate a delay

st.write("""
This AI-driven healthcare tool helps assess your symptoms and provides an **instant health risk assessment**.
Using **Machine Learning & Medical Data**, it analyzes key health indicators to give a preliminary diagnosis.

🚀 **Disclaimer:** This tool does not replace professional medical advice. Always consult a doctor for accurate diagnosis.
""")

# Key Features
st.markdown("### 🔍 **Key Health Indicators Analyzed:**")
features = [
    "Age", "Sex (Male: 1, Female: 0)", "Chest Pain Type (4 categories)",
    "Resting Blood Pressure", "Serum Cholesterol (mg/dl)", "Fasting Blood Sugar (> 120 mg/dl) (1 = true, 0 = false)",
    "Resting ECG Results (0, 1, 2)", "Maximum Heart Rate Achieved", "Exercise Induced Angina",
    "ST Depression (Oldpeak)", "Slope of Peak Exercise ST Segment",
    "Number of Major Vessels (0-3) colored by fluoroscopy", "Thalassemia (0 = normal, 1 = fixed defect, 2 = reversible defect)"
]

for feature in features:
    st.markdown(f"<div class='feature-box'>✅ {feature}</div>", unsafe_allow_html=True)

# Data Source
st.markdown("<p class='data-source'>📊 Data Acquired from: <b>DDX Dataset - Kaggle: Heart Disease Dataset (David Lapp)</b></p>", unsafe_allow_html=True)

# CTA Button
st.markdown("---")
if st.button("🔍 Get Started with Symptom Checker"):
    st.write("Redirecting...")
    time.sleep(1)
    st.rerun()

# Footer
st.markdown("💡 **Developed with ❤️ by shariq ")
