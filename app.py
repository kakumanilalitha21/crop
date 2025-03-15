# app.py
import streamlit as st
import joblib
import pandas as pd
import os

# Print current directory and files (for debugging)
print("Current Working Directory:", os.getcwd())
print("Files in Directory:", os.listdir())

# Load model 
model_path = "crop_yield_model.pkl"
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    raise FileNotFoundError("Model file not found. Ensure model.pkl is uploaded correctly.")

# Define feature names 
feature_columns = [
    "Region", "Soil_Type", "Crop", "Rainfall_mm", "Temperature_Celsius", 
    "Fertilizer_Used", "Irrigation_Used", "Weather_Condition", "Days_to_Harvest"
]

# Streamlit App UI
st.title("🌾 Crop Yield Predictor")
st.markdown("Predict crop yield based on agricultural parameters")

# Input Form
with st.form("input_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        region = st.selectbox("Region", ["North", "East", "South", "West"])
        soil_type = st.selectbox("Soil Type", ["Clay", "Sandy", "Loam", "Silt", "Peaty", "Chalky"])
        crop = st.selectbox("Crop", ["Wheat", "Rice", "Maize", "Barley", "Soybean", "Cotton"])
        weather = st.selectbox("Weather Condition", ["Sunny", "Rainy", "Cloudy"])
        
    with col2:
        rainfall = st.slider("Rainfall (mm)", 0, 1500, 500)
        temp = st.slider("Temperature (°C)", 10, 45, 25)
        days_to_harvest = st.number_input("Days to Harvest", 50, 200, 120)
        fertilizer = st.checkbox("Fertilizer Used")
        irrigation = st.checkbox("Irrigation Used")
    
    if st.form_submit_button("Predict Yield"):
        # Convert categorical variables to match training format
        input_data = pd.DataFrame([[
            region, soil_type, crop, rainfall, temp, 
            int(fertilizer), int(irrigation), weather, days_to_harvest
        ]], columns=feature_columns)
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        st.success(f"🌱 **Predicted Yield:** {prediction:.2f} tons/hectare")
