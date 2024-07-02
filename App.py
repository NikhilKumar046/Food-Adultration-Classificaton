import streamlit as st
import numpy as np
import joblib
import pandas as pd

# Load the saved model
model = joblib.load("logistic_regression_model.pkl")

# Define the Streamlit app


def main():
    st.title("Food Adulteration Detection")

    st.write("Enter the quantities per 100 grams of the food product:")

    carbohydrates = st.number_input(
        "Carbohydrates (grams)", min_value=0.0, max_value=100.0, step=0.1)
    protein = st.number_input(
        "Protein (grams)", min_value=0.0, max_value=100.0, step=0.1)
    fat = st.number_input("Fat (grams)", min_value=0.0,
                          max_value=100.0, step=0.1)
    preservatives = st.number_input(
        "Preservatives (grams)", min_value=0.0, max_value=10.0, step=0.1)
    artificial_sweeteners = st.number_input(
        "Artificial Sweeteners (grams)", min_value=0.0, max_value=5.0, step=0.1)
    sugar = st.number_input(
        "Sugar (grams)", min_value=0.0, max_value=50.0, step=0.1)

    if st.button("Predict"):
        input_data = np.array(
            [[carbohydrates, protein, fat, preservatives, artificial_sweeteners, sugar]])
        prediction = model.predict(input_data)
        prediction_label = "Adulterated" if prediction[0] == 1 else "Not Adulterated"

        st.write(f"The food product is: *{prediction_label}*")


if __name__ == "__main__":
    main()
