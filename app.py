import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("gnat_real_model.pkl")

st.title("🧬 GNAT Protein Solubility Predictor")

st.markdown("Input the biochemical features below to predict solubility of a GNAT variant:")

# Input fields
hydrophobicity = st.slider("Hydrophobicity", -1.0, 1.0, 0.0)
isoelectric_point = st.slider("Isoelectric Point", 4.0, 10.0, 7.0)
molecular_weight = st.number_input("Molecular Weight (Da)", min_value=10000, max_value=100000, value=30000)
aromaticity = st.slider("Aromaticity", 0.0, 0.2, 0.1)
instability_index = st.slider("Instability Index", 10.0, 100.0, 40.0)
aliphatic_index = st.slider("Aliphatic Index", 50.0, 120.0, 85.0)

# Predict button
if st.button("Predict Solubility"):
    features = np.array([[hydrophobicity, isoelectric_point, molecular_weight,
                          aromaticity, instability_index, aliphatic_index]])
    solubility = model.predict(features)[0]
    st.success(f"🧪 Predicted Solubility: **{solubility:.2f}**")
