import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline
model = joblib.load("models/food_prep_model.pkl")

st.set_page_config(
    page_title="Food Preparation Time Predictor",
    page_icon="🍽️",
    layout="centered"
)

st.title("🍽️ Food Preparation Time Prediction")
st.write("Zomato-inspired Machine Learning Regression Project")

number_of_items = st.number_input(
    "Number of Items",
    min_value=1,
    max_value=20,
    value=3
)

cuisine_type = st.selectbox(
    "Cuisine Type",
    ["Indian", "Chinese", "Fast Food", "South Indian", "Italian"]
)

order_hour = st.slider(
    "Order Hour",
    min_value=8,
    max_value=23,
    value=19
)

day_of_week = st.selectbox(
    "Day of Week",
    ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
)

restaurant_load = st.selectbox(
    "Restaurant Load",
    ["Low", "Medium", "High"]
)

historical_avg_prep_time = st.number_input(
    "Historical Average Preparation Time (Minutes)",
    min_value=5,
    max_value=60,
    value=20
)

if st.button("Predict Preparation Time"):

    input_data = pd.DataFrame({
        "number_of_items": [number_of_items],
        "cuisine_type": [cuisine_type],
        "order_hour": [order_hour],
        "day_of_week": [day_of_week],
        "restaurant_load": [restaurant_load],
        "historical_avg_prep_time": [historical_avg_prep_time]
    })

    prediction = model.predict(input_data)[0]

    st.success(
        f"Estimated Food Preparation Time: {prediction:.1f} minutes"
    )