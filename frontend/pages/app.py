import streamlit as st
import requests
import json
import os
# API URL (replace with your actual endpoint)
API_URL = os.getenv("API_URL", "https://heart-attack-predictor-c7gt.onrender.com/predict")
# Streamlit UI
st.title("AI Healthcare Disease Prediction")
st.write("Enter your symptoms to check for possible disease.")

# Input fields for 13 features
feature_names = [
    "Age", "Sex", "Chest Pain Type", "Resting Blood Pressure",
    "Cholesterol", "Fasting Blood Sugar", "Resting ECG",
    "Max Heart Rate", "Exercise Induced Angina", "Oldpeak",
    "Slope", "Number of Major Vessels", "Thalassemia"
]

features = []
for name in feature_names:
    value = st.number_input(f"{name}:", value=0.0)
    features.append(value)

# Prediction button
if st.button("Predict"):
    data = {"features": features}
    
    try:
        response = requests.post(API_URL, json=data)
        result = response.json()
        
        # Interpret result
        if "prediction" in result:
            prediction = result["prediction"]
            if prediction == 1:
                st.error("High risk of disease. Consult a doctor.")
            else:
                st.success("Low risk of disease. Stay healthy!")
        else:
            st.warning("Error in prediction. Check API.")

    except Exception as e:
        st.error(f"Error connecting to API: {e}")

# Google Form Feedback Link
feedback_url = "https://docs.google.com/forms/d/e/1FAIpQLSeuQTgRd8heAxNuYYitS3QzJTWyGHtp1TNsLG9Fxl1GUWJpTQ/viewform?usp=dialog"

st.title("💬 User Feedback")
st.write("We'd love to hear your thoughts! Your feedback helps us improve.")

# Button to redirect to Google Form
if st.button("Give Feedback"):
    st.markdown(f"[Click here to submit feedback]({feedback_url})", unsafe_allow_html=True)

