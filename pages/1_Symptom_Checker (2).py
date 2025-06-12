
import streamlit as st
import joblib
import numpy as np
import json

model = joblib.load("model.pkl")
disease_encoder = joblib.load("disease_encoder.pkl")
ethnicity_encoder = joblib.load("ethnicity_encoder.pkl")

st.title("🩺 Symptom Checker")

st.markdown("Enter your lab values and symptoms below:")

hemoglobin = st.number_input("Hemoglobin (g/dL)", min_value=1.0, max_value=20.0, value=10.0)
platelet = st.number_input("Platelet Count (lakhs/microliter)", min_value=0.5, max_value=5.0, value=2.5)
bleeding_time = st.number_input("Bleeding Time (minutes)", min_value=1, max_value=20, value=10)

fatigue = st.checkbox("Fatigue")
joint_pain = st.checkbox("Joint or Bone Pain")
dark_urine = st.checkbox("Dark-colored Urine")
infections = st.checkbox("Frequent Infections")
bruising = st.checkbox("Abnormal Bruising")
growth_delay = st.checkbox("Growth Delay")

ethnicity = st.selectbox("Ethnicity", ethnicity_encoder.classes_)

if st.button("Predict Disease"):
    input_data = np.array([
        [
            hemoglobin,
            platelet,
            bleeding_time,
            int(fatigue),
            int(joint_pain),
            int(dark_urine),
            int(infections),
            int(bruising),
            int(growth_delay),
            ethnicity_encoder.transform([ethnicity])[0]
        ]
    ])

    prediction = model.predict(input_data)[0]
    disease_name = disease_encoder.inverse_transform([prediction])[0]

    st.success(f"You may want to learn more about: **{disease_name}**")
    st.page_link("pages/2_Disease_Info.py", label=f"Click here to learn more about {disease_name}", icon="📖")
