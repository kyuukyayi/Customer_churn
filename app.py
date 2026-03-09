# Import streamlit
import streamlit as st

# Import pandas
import pandas as pd

# Import pickle to load model
import pickle

# Load saved model
model = pickle.load(open("model/churn_model.pkl", "rb"))

# App title
st.title("Customer Churn Prediction")

# User input example
tenure = st.slider("Tenure (months)", 0, 72)

monthly = st.number_input("Monthly Charges")

# Predict button
if st.button("Predict Churn"):
    
    # Example input dataframe
    input_data = pd.DataFrame({
        "tenure":[tenure],
        "MonthlyCharges":[monthly]
    })
    
    # Prediction
    prediction = model.predict(input_data)
    
    if prediction == 1:
        st.error("Customer likely to churn")
    else:
        st.success("Customer likely to stay")