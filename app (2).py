
import streamlit as st

st.set_page_config(page_title="Rare Disease Detection", layout="centered")

st.title("🧬 Rare Disease Detection")
st.markdown("### Check your symptoms now")

st.write("Welcome! This tool uses AI to help detect signs of rare blood diseases based on your symptoms and test results.")

st.page_link("pages/1_Symptom_Checker.py", label="👉 Start Symptom Checker", icon="🩺")
