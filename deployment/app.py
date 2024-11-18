import streamlit as st

# Import your separate EDA and Prediction scripts
import eda
import prediction

# Create a sidebar menu for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["EDA", "Prediction"])

# Show the selected page
if page == "EDA":
    eda.show_eda()  # Call the function from eda.py to display EDA
elif page == "Prediction":
    prediction.show_prediction()  # Call the function from prediction.py to display prediction
