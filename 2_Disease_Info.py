
import streamlit as st
import json

with open("disease_info.json") as f:
    disease_data = json.load(f)

st.title("📖 Disease Information")

for disease, info in disease_data.items():
    with st.container():
        st.subheader(disease)
        st.write(f"**Description:** {info['description']}")
        st.write(f"**Common Symptoms:** {', '.join(info['symptoms'])}")
        st.write(f"**Treatment:** {info['treatment']}")
