# prediction.py
import streamlit as st
import pandas as pd
import pickle

def show_prediction():
    st.title("Loan Status Prediction")

    # Load the model (replace 'best_model.pkl' with your actual model file path)
    model = pickle.load(open('best_model.pkl', 'rb'))

    # Input fields
    no_of_dependents = st.number_input("Number of Dependents", min_value=0)
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["Yes", "No"])
    income_annum = st.number_input("Annual Income", min_value=0)
    loan_amount = st.number_input("Loan Amount", min_value=0)
    loan_term = st.number_input("Loan Term", min_value=0)
    cibil_score = st.number_input("CIBIL Score", min_value=0)
    residential_assets_value = st.number_input("Residential Assets Value", min_value=0)
    commercial_assets_value = st.number_input("Commercial Assets Value", min_value=0)
    luxury_assets_value = st.number_input("Luxury Assets Value", min_value=0)
    bank_asset_value = st.number_input("Bank Asset Value", min_value=0)

    # Create a DataFrame with user inputs
    input_data = pd.DataFrame({
        'no_of_dependents': [no_of_dependents],
        'education': [education],
        'self_employed': [self_employed],
        'income_annum': [income_annum],
        'loan_amount': [loan_amount],
        'loan_term': [loan_term],
        'cibil_score': [cibil_score],
        'residential_assets_value': [residential_assets_value],
        'commercial_assets_value': [commercial_assets_value],
        'luxury_assets_value': [luxury_assets_value],
        'bank_asset_value': [bank_asset_value],
    })

    # Predict button
    if st.button("Predict"):
        prediction = model.predict(input_data)
        st.write(f"Loan Status: {prediction[0]}")