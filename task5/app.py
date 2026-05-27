import streamlit as st
import numpy as np
import joblib


model = joblib.load("random_forest_model.pkl")
scaler = joblib.load("scaler.pkl")


st.set_page_config(
    page_title="Ensemble Learning Project",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 Ensemble Learning Techniques Project")

st.subheader("Random Forest Classifier")

st.write(
    """
    This project demonstrates Ensemble Learning using
    Random Forest Classification on the Breast Cancer Dataset.
    """
)

st.markdown("---")


st.header("Enter Feature Values")

inputs = []

for i in range(30):
    value = st.number_input(
        f"Feature {i+1}",
        value=0.0,
        step=0.1
    )
    inputs.append(value)


if st.button("Predict"):

    input_array = np.array(inputs).reshape(1, -1)

    input_scaled = scaler.transform(input_array)

    prediction = model.predict(input_scaled)

    st.markdown("---")

    st.header("Prediction Result")

    if prediction[0] == 1:
        st.success("Benign Tumor Detected")
    else:
        st.error("Malignant Tumor Detected")