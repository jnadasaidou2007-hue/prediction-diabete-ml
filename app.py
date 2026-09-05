import streamlit as st
import joblib
import numpy as np

# Charger le modèle
model = joblib.load('modele_diabete.pkl')

st.title("🩺 Prédiction de la progression du diabète")
st.write("Ajuste les valeurs ci-dessous pour estimer la progression de la maladie sur 1 an.")

# Sliders pour chaque variable (valeurs basées sur les plages du dataset)
age = st.slider("Âge (normalisé)", -0.15, 0.15, 0.0, 0.01)
sex = st.slider("Sexe (normalisé)", -0.05, 0.05, 0.0, 0.01)
bmi = st.slider("IMC (normalisé)", -0.10, 0.20, 0.0, 0.01)
bp = st.slider("Tension artérielle (normalisée)", -0.12, 0.13, 0.0, 0.01)
s1 = st.slider("S1 (normalisé)", -0.13, 0.15, 0.0, 0.01)
s2 = st.slider("S2 (normalisé)", -0.12, 0.20, 0.0, 0.01)
s3 = st.slider("S3 (normalisé)", -0.10, 0.18, 0.0, 0.01)
s4 = st.slider("S4 (normalisé)", -0.08, 0.19, 0.0, 0.01)
s5 = st.slider("S5 (normalisé)", -0.13, 0.13, 0.0, 0.01)
s6 = st.slider("S6 (normalisé)", -0.14, 0.14, 0.0, 0.01)

# Bouton de prédiction
if st.button("Prédire la progression"):
    features = np.array([[age, sex, bmi, bp, s1, s2, s3, s4, s5, s6]])
    prediction = model.predict(features)
    st.success(f"Score de progression estimé : {prediction[0]:.2f}")