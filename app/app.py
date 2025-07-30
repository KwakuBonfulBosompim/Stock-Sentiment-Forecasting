import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("rf_model.pkl")

# App title
st.title("📈 Stock Price Prediction with News Sentiment")
st.markdown("Predict the next day's closing price based on financial inputs and sentiment score.")

# Input fields
open_price = st.number_input("Open Price", value=100.0)
high_price = st.number_input("High Price", value=105.0)
low_price = st.number_input("Low Price", value=95.0)
volume = st.number_input("Volume", value=50000000)
sentiment = st.slider("VADER Sentiment Score", min_value=-1.0, max_value=1.0, value=0.0)

# Prepare input
input_df = pd.DataFrame({
    'Open': [open_price],
    'High': [high_price],
    'Low': [low_price],
    'Volume': [volume],
    'VADER_compound': [sentiment]
})

# Prediction
if st.button("Predict Close Price"):
    prediction = model.predict(input_df)[0]
    st.success(f"📊 Predicted Close Price: ${prediction:.2f}")

